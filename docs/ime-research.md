# 各IME仕様調査

## Microsoft IME(MS-IME)

### 使用品詞

<table>
    <tr>
        <th>名詞</th>
        <th colspan="3">人名</th>
        <th>地名</th>
        <th>短縮よみ</th>
        <th>顔文字</th>
    </tr>
    <tr>
        <td>名詞</td>
        <td>姓</td><td>名</td><td>人名</td>
        <td>地名その他</td>
        <td>短縮よみ</td>
        <td>顔文字</td>
    </tr>
</table>

<table>
    <tr>
        <th colspan="10">その他</th>
    </tr>
    <tr>
        <td>さ変形動名詞</td><td>固有名詞</td><td>形容詞</td><td>形容動詞</td><td>副詞</td><td>連体詞</td><td>接続詞</td><td>感動詞</td><td>慣用句</td><td>さ変名詞</td>
    </tr>
    <tr>
        <td>ざ変名詞</td><td>形動名詞</td><td>副詞的名詞</td><td>接頭語</td><td>姓名接頭語</td><td>地名接頭語</td><td>接尾語</td><td>姓名接尾語</td><td>地名接尾語</td><td>助数詞</td>
    </tr>
    <tr>
        <td>あわ行五段</td><td>か行五段</td><td>が行五段</td><td>さ行五段</td><td>た行五段</td><td>な行五段</td><td>ば行五段</td><td>ま行五段</td><td>ら行五段</td><td>一段動詞</td>
    </tr>
</table>

### インポートフォーマット
* **区切り文字**: タブ区切り (.txt)
* **文字コード**: UTF-16 LE
<table>
    <tr>
        <th>並び順</th><th>項目</th><th>例</th>
    </tr>
    <tr>
        <td>1</td><td>読み</td><td>とうきょう</td>
    </tr>
    <tr>
        <td>2</td><td>単語</td><td>東京</td>
    </tr>
    <tr>
        <td>3</td><td>品詞</td><td>地名その他</td>
    </tr>
    <tr>
        <td>4(任意)</td><td>コメント</td><td>日本の首都</td>
    </tr>
</table>
コメントがある行だけタブ区切りが増える

### サンプル
```
!Microsoft IME Dictionary Tool
!Version:
!Format:WORDLIST
!User Dictionary Name:
!Output File Name:
!DateTime:

とうきょう	東京	地名その他
とうきょう	東京	地名その他	日本の首都
```

<br/>

## ATOK

### 使用品詞

<table>
    <tr>
        <th colspan="6">名詞</th>
    </tr>
    <tr>
        <td>名詞</td><td>固有人姓</td><td>固有人名</td><td>固有人他</td><td>固有地名</td><td>固有組織</td>
    </tr>
    <tr>
        <td>固有商品</td><td>固有一般</td><td>名詞サ変</td><td>名詞ザ変</td><td>名詞形動</td><td>名サ形動</td>
    </tr>
</table>
<table>
    <tr>
        <th colspan="6">形容詞・形容動詞</th>
    </tr>
    <tr>
        <td>形容詞</td><td>形容詞ウ</td><td>形容詞イ</td><td>形容詞エ</td><td>形容動詞</td><td>形動タリ</td>
    </tr>
</table>
<table>
    <tr>
        <th colspan="6">動詞</th>
    </tr>
    <tr>
        <td>カ行五段</td><td>ガ行五段</td><td>サ行五段</td><td>タ行五段</td><td>ナ行五段</td><td>バ行五段</td>
    </tr>
    <tr>
        <td>マ行五段</td><td>ラ行五段</td><td>ワ行五段</td><td>ハ行四段</td><td>一段動詞</td><td>カ変動詞</td>
    </tr>
    <tr>
        <td>サ変動詞</td><td>ザ変動詞</td><td>ワ行五段音便</td><td>カ行五段特殊</td><td>ラ行五段特殊</td><td>ワ行五段特殊</td>
    </tr>
    <tr>
        <td>ナ変動詞</td><td>ラ変動詞</td><td>カ行上二段</td><td>ガ行上二段</td><td>タ行上二段</td><td>ダ行上二段</td>
    </tr>
    <tr>
        <td>ハ行上二段</td><td>バ行上二段</td><td>マ行上二段</td><td>ヤ行上二段</td><td>ラ行上二段</td><td>カ行下二段</td>
    </tr>
    <tr>
        <td>ガ行下二段</td><td>サ行下二段</td><td>ザ行下二段</td><td>タ行下二段</td><td>ダ行下二段</td><td>ナ行下二段</td>
    </tr>
    <tr>
        <td>ハ行下二段</td><td>バ行下二段</td><td>マ行下二段</td><td>ヤ行下二段</td><td>ラ行下二段</td><td>ワ行下二段</td>
    </tr>
</table>

<table>
    <tr>
        <th colspan="6">その他</th>
    </tr>
    <tr>
        <td>顔文字</td><td>短縮読み</td><td>数詞</td><td>副詞</td><td>連体詞</td><td>接続詞</td>
    </tr>
    <tr>
        <td>感動詞</td><td>独立語</td><td>接頭語</td><td>冠数詞</td><td>接尾語</td><td>助数詞</td>
    </tr>
    <tr>
        <td>単漢字</td><td>終助詞</td><td></td><td></td><td></td><td></td>
    </tr>
</table>

### インポートフォーマット
* **区切り文字**: タブ区切り (.txt)
* **文字コード**: Shift-JIS
<table>
    <tr>
        <th>並び順</th><th>項目</th><th>例</th>
    </tr>
    <tr>
        <td>1</td><td>読み</td><td>とうきょう</td>
    </tr>
    <tr>
        <td>2</td><td>単語</td><td>東京</td>
    </tr>
    <tr>
        <td>3</td><td>品詞</td><td>固有地名</td>
    </tr>
    <tr>
        <td>4(任意)</td><td>コメント</td><td>日本の首都</td>
    </tr>
    <tr>
        <td>5(任意)</td><td>自動置換</td><td>する/しない</td>
    </tr>
    <tr>
        <td>6(任意)</td><td>置換候補1</td><td>首都</td>
    </tr>
    <tr>
        <td>7(任意)</td><td>置換候補2</td><td>帝都</td>
    </tr>
    <tr>
        <td>8(任意)</td><td>置換候補3</td><td>江戸</td>
    </tr>
    <tr>
        <td>9(任意)</td><td>置換候補4</td><td>東都</td>
    </tr>
    <tr>
        <td>10(任意)</td><td>置換候補5</td><td>京浜</td>
    </tr>
</table>
フィールドは途中を抜かして書けない。1-3,5など

### サンプル
```
!!ATOK_TANGO_TEXT_HEADER_1
とうきょう	東京	固有地名    日本の首都
とうきょう	東京	固有地名    日本の首都  しない  首都    帝都    江戸
```

参照：[単語ファイルを作成する](https://atok.com/other/support/howtouse/mac/dc/pgs/dc_word_file.htm)
<br/><br/>

## Google 日本語入力

### 使用品詞

<table>
    <tr>
        <td>品詞なし</td><td>名詞</td><td>短縮よみ</td><td>サジェストのみ</td><td>固有名詞</td><td>人名</td><td>姓</td><td>名</td>
    </tr>
    <tr>
        <td>組織</td><td>地名</td><td>名詞サ変</td><td>名詞形動</td><td>数</td><td>アルファベット</td><td>記号</td><td>顔文字</td>
    </tr>
    <tr>
        <td>副詞</td><td>連体詞</td><td>接続詞</td><td>感動詞</td><td>接頭語</td><td>助数詞</td><td>接尾一般</td><td>接尾人名</td>
    </tr>
    <tr>
        <td>接尾地名</td><td>動詞ワ行五段</td><td>動詞カ行五段</td><td>動詞サ行五段</td><td>動詞タ行五段</td><td>動詞ナ行五段</td><td>動詞マ行五段</td><td>動詞ラ行五段</td>
    </tr>
    <tr>
        <td>動詞ガ行五段</td><td>動詞バ行五段</td><td>動詞ハ行四段</td><td>動詞一段</td><td>動詞カ変</td><td>動詞サ変</td><td>動詞ザ変</td><td>動詞ラ変</td>
    </tr>
    <tr>
        <td>形容詞</td><td>終助詞</td><td>句読点</td><td>独立語</td><td>抑制単語</td><td></td><td></td><td></td>
    </tr>
</table>

### インポートフォーマット
* **区切り文字**: タブ区切り (.txt)
* **文字コード**: UTF-8
<table>
    <tr>
        <th>並び順</th><th>項目</th><th>例</th>
    </tr>
    <tr>
        <td>1</td><td>読み</td><td>とうきょう</td>
    </tr>
    <tr>
        <td>2</td><td>単語</td><td>東京</td>
    </tr>
    <tr>
        <td>3</td><td>品詞</td><td>地名</td>
    </tr>
    <tr>
        <td>4(任意)</td><td>コメント</td><td>日本の首都</td>
    </tr>
</table>
コメントが空欄でもタブ区切りが入る

### サンプル
```
とうきょう	東京	地名	
とうきょう	東京	地名	日本の首都
```

<br/>

## macOS 日本語入力(Japanese Input Method)

### 使用品詞(追加辞書)
<table>
    <tr>
        <th colspan="2">普通名詞</th><th>サ変名詞</th><th colspan="4">人名</th><th colspan="2">地名</th><th colspan="2">形容詞</th>
    </tr>
    <tr>
        <td>普通名詞</td><td>形動名詞</td><td>サ変名詞</td><td>人名</td><td>姓</td><td>名</td><td>その他の人名</td>
        <td>単純地名</td><td>接尾語付き地名</td><td>形容詞</td><td>形容動詞</td>
    </tr>
    
</table>

<table>
    <tr>
        <th>副詞</th><th colspan="4">接尾語</th>
    </tr>
    <tr>
        <td>副詞</td>
        <td>人名接尾語</td><td>地名接尾語</td><td>組織名接尾語</td><td>数字列接尾語</td>
    </tr>
</table>

<table>
    <tr>
        <th colspan="7">動詞</th>
    </tr>
    <tr>
        <td colspan="3" align="center">五段動詞</td><td>一段動詞</td><td>カ変動詞</td><td>サ変動詞</td><td>ザ変動詞</td>
    </tr>
    <tr>
        <td>カ行五段<br/>サ行五段<br/>タ行五段</td><td>ナ行五段<br/>マ行五段<br/>ラ行五段</td><td>ワ行五段<br/>ガ行五段<br/>バ行五段</td><td></td><td></td><td></td><td></td>
    </tr>
</table>

<table>
    <tr>
        <th colspan="8">その他すべての品詞</th>
    </tr>
    <tr>
        <td>組織名</td><td>その他の固有名詞</td><td>連体詞</td><td>接続詞</td><td>感動詞</td><td>数字列接頭語</td><td>成句</td><td>無品詞</td>
    </tr>
</table>

参照：[Macの追加辞書に読み込むことのできる品詞](https://support.apple.com/ja-jp/guide/japanese-input-method/jpim10211/6.3/mac/26)

### インポートフォーマット(追加辞書)
* **区切り文字**: カンマ区切り (.txt)
* **文字コード**: UTF-8
* **互換**: ことえり
<table>
    <tr>
        <th>並び順</th><th>項目</th><th>例</th>
    </tr>
    <tr>
        <td>1</td><td>読み</td><td>とうきょう</td>
    </tr>
    <tr>
        <td>2</td><td>単語</td><td>東京</td>
    </tr>
    <tr>
        <td>3</td><td>品詞</td><td>地名</td>
    </tr>
</table>
品詞は大分類の9種類と細分化した38種類のどちらも使えると考えられる

### サンプル(追加辞書)
```
とうきょう,東京,地名
```

### インポートフォーマット(ユーザ辞書)
* iCloud同期対応 (macOS / iOS / iPadOS)
* 品詞未使用
* **形式**: XML (.plist)
* **文字コード**: UTF-8

### サンプル(ユーザ辞書)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
	<dict>
		<key>phrase</key>
		<string>東京</string>
		<key>shortcut</key>
		<string>とうきょう</string>
	</dict>
</array>
</plist>
```

<br/>

## Gboard

### 使用品詞
<table>
    <tr>
        <td>品詞なし</td><td>名詞</td><td>短縮よみ</td><td>サジェストのみ</td><td>固有名詞</td><td>人名</td><td>姓</td><td>名</td>
    </tr>
    <tr>
        <td>組織</td><td>地名</td><td>名詞サ変</td><td>名詞形動</td><td>数</td><td>アルファベット</td><td>記号</td><td>顔文字</td>
    </tr>
    <tr>
        <td>副詞</td><td>連体詞</td><td>接続詞</td><td>感動詞</td><td>接頭語</td><td>助数詞</td><td>接尾一般</td><td>接尾人名</td>
    </tr>
    <tr>
        <td>接尾地名</td><td>動詞ワ行五段</td><td>動詞カ行五段</td><td>動詞サ行五段</td><td>動詞タ行五段</td><td>動詞ナ行五段</td><td>動詞マ行五段</td><td>動詞ラ行五段</td>
    </tr>
    <tr>
        <td>動詞ガ行五段</td><td>動詞バ行五段</td><td>動詞ハ行四段</td><td>動詞一段</td><td>動詞カ変</td><td>動詞サ変</td><td>動詞ザ変</td><td>動詞ラ変</td>
    </tr>
    <tr>
        <td>形容詞</td><td>終助詞</td><td>句読点</td><td>独立語</td><td>抑制単語</td><td></td><td></td><td></td>
    </tr>
</table>

### インポートフォーマット
* **形式**: Zip (.zip) 内部にテキストファイル
* **区切り文字**: タブ区切り (.txt)
* **文字コード**: UTF-8
<table>
    <tr>
        <th>並び順</th><th>項目</th><th>例</th>
    </tr>
    <tr>
        <td>1</td><td>読み</td><td>とうきょう</td>
    </tr>
    <tr>
        <td>2</td><td>単語</td><td>東京</td>
    </tr>
    <tr>
        <td>3</td><td>言語</td><td>ja-JP</td>
    </tr>
    <tr>
        <td>4</td><td>品詞</td><td>地名</td>
    </tr>
</table>

### サンプル

```
# Gboard Dictionary version:2
# Gboard Dictionary format:shortcut	word	language_tag	pos_tag
とうきょう  東京    ja-JP   地名
```
