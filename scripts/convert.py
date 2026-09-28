# python scripts/convert.py data/sample.tsv (tag)

import csv
import os
import sys
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from xml.dom import minidom

# 各IMEごとの品詞変換テーブル
IME_CONFIGS = {
    "ms": {
        "name": "Microsoft IME",
        "filename_suffix": "_ms.txt",
        "encoding": "utf-16",
        "lineterminator": "\r\n",
        "delimiter": "\t",
        "header": (
            "!Microsoft IME Dictionary Tool\r\n"
            "!Version:\r\n"
            "!Format:WORDLIST\r\n"
            "!User Dictionary Name:\r\n"
            "!Output File Name:\r\n"
            "!DateTime:\r\n"
            "\r\n"
        ),
        "pos_map": {
            "PERSON": "人名",
            "LOCATION": "地名その他",
            "NOUN": "名詞",
            "PROPER_NOUN": "固有名詞"
        },
        "default_pos": "名詞"
    },
    "atok": {
        "name": "ATOK",
        "filename_suffix": "_atok.txt",
        "encoding": "cp932", # Shift_JIS
        "lineterminator": "\r\n",
        "delimiter": "\t",
        "header": "!!ATOK_TANGO_TEXT_HEADER_1\r\n",
        "pos_map": {
            "PERSON": "固有人他",
            "LOCATION": "固有地名",
            "NOUN": "名詞",
            "PROPER_NOUN": "固有一般"
        },
        "default_pos": "名詞"
    },
    "google": {
        "name": "Google 日本語入力",
        "filename_suffix": "_google.txt",
        "encoding": "utf-8",
        "lineterminator": "\r\n",
        "delimiter": "\t",
        "header": None,
        "pos_map": {
            "PERSON": "人名",
            "LOCATION": "地名",
            "NOUN": "名詞",
            "PROPER_NOUN": "固有名詞"
        },
        "default_pos": "名詞"
    },
    "macos": {
        "name": "macOS 日本語入力",
        "filename_suffix": "_macos.txt",
        "encoding": "utf-8",
        "lineterminator": "\n",
        "delimiter": ",", # カンマ
        "header": None,
        "pos_map": {
            "PERSON": "人名",
            "LOCATION": "地名",
            "NOUN": "普通名詞",
            "PROPER_NOUN": "その他の固有名詞"
        },
        "default_pos": "普通名詞"
    },
    "gboard": {
        "name": "Gboard",
        "filename_suffix": "_gboard.txt", # あとでzip圧縮
        "encoding": "utf-8",
        "lineterminator": "\n",
        "delimiter": "\t",
        "header": (
            "# Gboard Dictionary version:2\n"
            "# Gboard Dictionary format:shortcut\tword\tlanguage_tag\tpos_tag\n"
        ),
        "pos_map": {
            "PERSON": "人名",
            "LOCATION": "地名",
            "NOUN": "名詞",
            "PROPER_NOUN": "固有名詞"
        },
        "default_pos": "名詞"
    }
}

def convert_all(input_file: str, target_tag: str | None = None, is_ci: bool = False):
    print(f"対象ファイル: {input_file} タグ: '{target_tag}' (CIモード: {is_ci})")

    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: ファイルが見つかりません: {input_path}")
        sys.exit(1)

    # 出力先ディレクトリがなければ作成
    output_dir = Path(f"dist/{input_path.stem}")
    output_dir.mkdir(parents=True, exist_ok=True)

    # 配列初期化
    output_files = {}
    writers = {}
    plist_entries = [] # plist用

    try:
        # 入力ファイルと全出力ファイルを一括オープン
        # TODO: 将来的なPagesによるコンバータ時に修正
        with open(input_path, "r", encoding="utf-8-sig", newline="") as infile:
            for ime_key, config in IME_CONFIGS.items():
                out_path = output_dir / f"{input_path.stem}{config['filename_suffix']}"
                f = open(out_path, "w", encoding=config["encoding"], errors="strict", newline="")

                # ヘッダー書き込み
                if config["header"]:
                    f.write(config["header"])

                output_files[ime_key] = f
                writers[ime_key] = csv.writer(f, delimiter=config["delimiter"], lineterminator=config["lineterminator"])

            reader = csv.reader(infile, delimiter="\t")

            if target_tag:
                # 引数タグを分解
                target_tags = [t.strip() for t in target_tag.split(",") if t.strip()]

            for row in reader:
                # 空行スキップ
                if not row:
                    continue
                elif len(row) < 3: # 3個は必須なのでなかったらエラースキップ
                    print(f"必須項目が足りない {row}")
                    continue

                # 書いて無い項目は空文字にする
                reading = row[0]
                word = row[1]
                pos = row[2]
                comment = row[3] if len (row) >= 4 else "" # 任意
                tags_raw = row[4] if len (row) >= 5 else "" # 任意

                if target_tag:
                    # 元データタグを分解
                    tags = [t.strip() for t in tags_raw.split(",") if t.strip()] # ifは空文字防止

                    # 引数のタグどれか1つが該当したらbreak
                    if not any(tag in tags for tag in target_tags):
                        continue

                # plist配列準備
                plist_entries.append({"phrase": word, "shortcut": reading})

                # 品詞変換処理(不明なposはデフォルト設定)
                for ime_key, config in IME_CONFIGS.items():
                    target_pos = config["pos_map"].get(pos, config["default_pos"])

                    # IMEごとに合わせる
                    if ime_key == "gboard":
                        # Gboard: 読み・単語・言語・品詞
                        writers[ime_key].writerow([reading, word, "ja-JP", target_pos])
                    elif ime_key == "macos":
                        # macOS追加辞書: 読み・単語・品詞
                        writers[ime_key].writerow([reading, word, target_pos])
                    elif ime_key in ("ms", "atok"):
                        # MS-IME: 読み・単語・品詞[・コメント] コメントがなければ最後のタブなし
                        if comment:
                            writers[ime_key].writerow([reading, word, target_pos, comment])
                        else:
                            writers[ime_key].writerow([reading, word, target_pos])
                    else:
                        # 読み・単語・品詞・コメント
                        writers[ime_key].writerow([reading, word, target_pos, comment])

            # macOS iCloud用 plist書き出し
            generate_macos_plist(output_dir / f"{input_path.stem}_macos_user.plist", plist_entries)

    finally:
        # 開いたファイルを閉じる
        for f in output_files.values():
            f.close()

    # ActionsはGboardテキストzip圧縮
    if is_ci:
        gboard_config = IME_CONFIGS["gboard"]
        gboard_txt_path = output_dir / f"{input_path.stem}{gboard_config['filename_suffix']}"
        
        if gboard_txt_path.exists():
            gboard_zip_path = output_dir / f"{input_path.stem}_gboard.zip"

            with zipfile.ZipFile(gboard_zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
                zf.write(gboard_txt_path, arcname="dictionary.txt")
        
            # ファイル削除
            gboard_txt_path.unlink()

    print("--- 生成完了 ---")

# macOS iCloud plist生成
def generate_macos_plist(output_path: Path, entries: list[dict]):
    plist = ET.Element("plist", version="1.0")
    array = ET.SubElement(plist, "array")

    for entry in entries:
        dict_elm = ET.SubElement(array, "dict")

        key_phrase = ET.SubElement(dict_elm, "key")
        key_phrase.text = "phrase"
        str_phrase = ET.SubElement(dict_elm, "string")
        str_phrase.text = entry["phrase"]

        key_shortcut = ET.SubElement(dict_elm, "key")
        key_shortcut.text = "shortcut"
        str_shortcut = ET.SubElement(dict_elm, "string")
        str_shortcut.text = entry["shortcut"]

    xml_str = minidom.parseString(ET.tostring(plist, encoding="utf-8")).toprettyxml(indent="\t", encoding="UTF-8").decode("utf-8")

    # DOCTYPE付与してまとめる
    doctype = '<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">\n'
    lines = xml_str.split("\n")
    lines.insert(1, doctype.strip())

    # 書き込み
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines))


if __name__ == "__main__":
    args = sys.argv[1:] # 引数のみ

    if not args:
        print("使い方: python convert.py ***.tsv [タグ] [--ci]")
        print("複数タグ指定はOR検索: [タグ1,タグ2]")
        print("例1: python convert.py sample.tsv")
        print("例2: python convert.py sample.tsv 役満")
        print("例3: python convert.py sample.tsv 満貫,役満")
        sys.exit(1)

    # GITHUB ACTIONSによるスイッチ(テスト用フラグ)
    is_ci = os.environ.get("GITHUB_ACTIONS") == "true" or "--ci" in args

    # argsから--ciがあれば取り除く
    clean_args = [arg for arg in args if arg != "--ci"]

    if not clean_args:
        print("Error: ファイル名がありません")
        sys.exit(1)
        
    input_file = clean_args[0]
    target_tag = clean_args[1] if len(clean_args) > 1 else None

    # convert関数に渡す
    convert_all(input_file, target_tag, is_ci=is_ci)
