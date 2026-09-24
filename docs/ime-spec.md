# ZLex元データ仕様

### 使用品詞
<table>
    <tr>
        <th>人名</th><th>地名</th><th>一般名詞</th><th>固有名詞</th>
    </tr>
    <tr>
        <td>PERSON</td><td>LOCATION</td><td>NOUN</td><td>PROPER_NOUN</td>
    </tr>
</table>

### 互換品詞
コンバータ使用時の変換先品詞
<table>
    <tr>
        <th></th><th>人名</th><th>地名</th><th>一般名詞</th><th>固有名詞</th>
    </tr>
    <tr>
        <th>ZLex</th><td>PERSON</td><td>LOCATION</td><td>NOUN</td><td>PROPER_NOUN</td>
    </tr>
    <tr>
        <th>Microsoft IME</th><td>人名</td><td>地名その他</td><td>名詞</td><td>固有名詞</td>
    </tr>
    <tr>
        <th>ATOK</th><td>固有人他</td><td>固有地名</td><td>名詞</td><td>固有一般</td>
    </tr>
    <tr>
        <th>Google 日本語入力</th><td>人名</td><td>地名</td><td>名詞</td><td>固有名詞</td>
    </tr>
    <tr>
        <th>macOS 日本語入力</th><td>人名</td><td>地名</td><td>普通名詞</td><td>その他の固有名詞</td>
    </tr>
    <tr>
        <th>Gboard</th><td>人名</td><td>地名</td><td>名詞</td><td>固有名詞</td>
    </tr>
</table>

### フォーマット
* **区切り文字**: タブ区切り (.txt)
* **タグ区切り文字**: カンマ区切り
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
        <td>3</td><td>品詞</td><td>LOCATION</td>
    </tr>
    <tr>
        <td>4(任意)</td><td>コメント</td><td>日本の首都</td>
    </tr>
    <tr>
        <td>5(任意)</td><td>タグ</td><td>日本,首都</td>
    </tr>
</table>
空欄でもタブ区切りが入る

### サンプル

```
とうきょう	東京	LOCATION	日本の首都	日本,首都
```