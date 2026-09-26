# python scripts/convert.py sample.tsv (tag)

import csv
import sys
from pathlib import Path

# 品詞変換テーブル ZLex -> Google
POS_MAP = {
    "PERSON": "人名",
    "LOCATION": "地名",
    "NOUN": "名詞",
    "PROPER_NOUN": "固有名詞"
}

def convert_google(input_file: str, target_tag: str | None = None):
    print(f"{input_file} ... {target_tag}")

    input_path = Path(input_file)

    print(f"input_path: {input_path}")

    if not input_path.exists():
        print(f"Error: ファイルが見つかりません: {input_path}")
        sys.exit(1)

    # 出力先ディレクトリ(/dist)がなければ作成
    output_dir = Path("dist")
    output_dir.mkdir(exist_ok=True)

    # 出力ファイル名
    output_path = output_dir / f"{input_path.stem}_google.txt"

    print(f"output_path: {output_path}")

    # 出力件数
    converted_count = 0

    with open(input_path, "r", encoding="utf-8", newline="") as infile, \
        open(output_path, "w", encoding="utf-8", newline="") as outfile:

        reader = csv.reader(infile, delimiter="\t")
        writer = csv.writer(
            outfile,
            delimiter="\t",
            lineterminator="\n"
        )

        for row in reader:
            # 空行スキップ
            if not row:
                continue
            elif len(row) < 3: # 3個は必須なのでなかったらエラースキップ
                print(f"必須項目が足りない {row}")
                continue

            # print(f"{row}")
            # 書いて無い項目は空文字にする
            reading = row[0]
            word = row[1]
            pos = row[2]
            comment = row[3] if len (row) >= 4 else "" # 任意
            tags_raw = row[4] if len (row) >= 5 else "" # 任意

            # タグフィルタリング
            if target_tag:
                # 元データタグを分解
                tags = [t.strip() for t in tags_raw.split(",") if t.strip()] # ifは空文字防止

                # 引数タグを分解
                target_tags = [t.strip() for t in target_tag.split(",") if t.strip()]

                # 引数のタグどれか1つが該当したらbreak
                if not any(tag in tags for tag in target_tags):
                    continue

            # 品詞変換処理(不明なposは名詞扱い)
            google_pos = POS_MAP.get(pos, "名詞")

            # print(f"出力予定: {row}")

            # 書き込み
            writer.writerow([
                reading,
                word,
                google_pos,
                comment
            ])

            converted_count += 1 # 出力カウント


    tag_info = f" (タグフィルタ: '{target_tag}')" if target_tag else ""
    print(f"生成完了: {output_path} ({converted_count}件出力){tag_info}")









if __name__ == "__main__":
    args = sys.argv[1:] # 引数のみ

    if not args:
        print("使い方: python convert.py ***.tsv [タグ]")
        print("複数タグ指定はOR検索: [タグ1,タグ2]")
        print("例1: python convert.py sample.tsv")
        print("例2: python convert.py sample.tsv 役満")
        print("例3: python convert.py sample.tsv 満貫,役満")
        sys.exit(1)

    input_file = args[0]
    target_tag = args[1] if len(args) > 1 else None

    # とりあえずgoogle
    convert_google(input_file, target_tag)
