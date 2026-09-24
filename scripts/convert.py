# python scripts/convert.py sample.tsv (tag)

import csv
import sys
from pathlib import Path



def convert_google(input_file: str, target_tag: str | None = None):
    print(f"{input_file} ... {target_tag}")

    input_path = Path(input_file)

    if not input_path.exists():
        print(f"Error: ファイルが見つかりません: {input_path}")
        sys.exit(1)




if __name__ == "__main__":
    args = sys.argv[1:] # 引数のみ

    if not args:
        print("使い方: python convert.py ***.tsv [タグ]")
        print("例1: python convert.py sample.tsv")
        print("例2: python convert.py sample.tsv 役")
        sys.exit(1)

    input_file = args[0]
    target_tag = args[1] if len(args) > 1 else None

    # とりあえずgoogle
    convert_google(input_file, target_tag)
