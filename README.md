# Improved csv2gpx

A simple and flexible script to convert Flightradar24 CSV files to GPX tracks for animated data visualization. This improved version eliminates the need for manual date/time configuration and properly handles UTC timestamps.

## Features

- **No Configuration Required**: Automatically processes all CSV files in the directory without needing to manually set dates or time ranges
- **Proper UTC Handling**: Ensures correct time formatting according to GPX specification
- **Flexible Position Format**: Handles both combined position data ("lat,lon") and separate latitude/longitude columns
- **Detailed Logging**: Provides informative output about the conversion process
- **Individual GPX Files**: Creates a separate GPX file for each CSV input

## Usage

1. Download your flight data CSV files from Flightradar24 (from the `YYYYMMDD_positions.zip` files)
2. Place the CSV files in the same directory as the script
3. Run the script:
   ```
   python csv2gpx.py
   ```
4. The script will generate a `.gpx` file for each `.csv` file in the directory

## CSV Format Compatibility

This script is designed to work with Flightradar24 CSV files that have the following header format:
```
Timestamp,UTC,Callsign,Position,Altitude,Speed,Direction
```

The script looks for:
- A timestamp in the first column
- Position data either in a "Position" column as "lat,lon" or in separate "Latitude" and "Longitude" columns
- Optional "UTC" column containing ISO-formatted UTC time strings

## Visualization Options

You can visualize the generated GPX files using various tools:

- The Time Manager plugin in QGIS
- [trackanimation](https://github.com/JoanMartin/trackanimation)
- [RunParticles](https://github.com/dal/RunParticles)
- [GPX animator](https://github.com/zdila/gpx-animator)

## Improvements over the original

This version improves upon the original script by:

1. Eliminating the need to manually configure date and time parameters
2. Properly handling UTC timestamps according to GPX specification
3. Creating individual GPX files for each input CSV
4. Adding better error handling and debugging information
5. Using the CSV module to properly handle quoted fields
6. Supporting multiple position format variants

## License

This script is based on the original [csv2gpx](https://github.com/Davn01/csv2gpx) by Davn01.

This project is licensed under the MIT License - see below for details:

```
MIT License

Original work Copyright (c) 2020 Simon Haas
Modified work Copyright (c) 2025 Shinichi Ohki

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

# 日本語説明

## 改良版 csv2gpx

Flightradar24のCSVファイルをアニメーション可視化のためのGPXトラックに変換するシンプルで柔軟なスクリプトです。この改良版では、手動での日付/時間設定が不要になり、UTCタイムスタンプを適切に処理します。

## 特徴

- **設定不要**: ディレクトリ内のすべてのCSVファイルを日付や時間範囲を手動設定せずに自動的に処理
- **適切なUTC処理**: GPX仕様に従った正確な時間フォーマットを保証
- **柔軟な位置情報フォーマット**: 組み合わせた位置データ（"緯度,経度"）と別々の緯度/経度列の両方に対応
- **詳細なログ出力**: 変換プロセスに関する有益な情報を提供
- **個別のGPXファイル**: 各CSV入力ファイルに対して別々のGPXファイルを作成

## 使い方

1. Flightradar24からフライトデータのCSVファイルをダウンロード（`YYYYMMDD_positions.zip`ファイルから）
2. CSVファイルをスクリプトと同じディレクトリに配置
3. スクリプトを実行:
   ```
   python csv2gpx.py
   ```
4. ディレクトリ内の各`.csv`ファイルに対応する`.gpx`ファイルが生成されます

## CSV形式の互換性

このスクリプトは、以下のようなヘッダー形式を持つFlightradar24のCSVファイル用に設計されています:
```
Timestamp,UTC,Callsign,Position,Altitude,Speed,Direction
```

スクリプトは以下を探します:
- 最初の列のタイムスタンプ
- "Position"列の"緯度,経度"形式、または別々の"Latitude"と"Longitude"列の位置データ
- ISO形式のUTC時間文字列を含む任意の"UTC"列

## 可視化オプション

生成されたGPXファイルは様々なツールで可視化できます:

- QGISのTime Managerプラグイン
- [trackanimation](https://github.com/JoanMartin/trackanimation)
- [RunParticles](https://github.com/dal/RunParticles)
- [GPX animator](https://github.com/zdila/gpx-animator)

## オリジナルからの改良点

このバージョンはオリジナルのスクリプトから以下の点を改良しています:

1. 日付と時間パラメータを手動で設定する必要をなくしました
2. GPX仕様に従ってUTCタイムスタンプを適切に処理します
3. 入力CSVごとに個別のGPXファイルを作成します
4. より優れたエラー処理とデバッグ情報を追加
5. 引用符で囲まれたフィールドを適切に処理するためにCSVモジュールを使用
6. 複数の位置情報フォーマットのバリエーションをサポート

## ライセンス

このスクリプトはDavn01による元の[csv2gpx](https://github.com/Davn01/csv2gpx)をベースにしています。

このプロジェクトはMITライセンスの下で公開されています - 詳細は以下をご覧ください:

```
MITライセンス

Original work Copyright (c) 2020 Simon Haas
Modified work Copyright (c) 2025 Shinichi Ohki

以下に定める条件に従い、本ソフトウェアおよび関連文書のファイル（以下「ソフトウェア」）の複製を取得するすべての人に対し、
ソフトウェアを無制限に扱うことを無償で許可します。これには、ソフトウェアの複製を使用、複写、変更、結合、掲載、頒布、
サブライセンス、および/または販売する権利、およびソフトウェアを提供する相手に同じことを許可する権利も無制限に含まれます。

上記の著作権表示および本許諾表示を、ソフトウェアのすべての複製または重要な部分に記載するものとします。

ソフトウェアは「現状のまま」で、明示であるか暗黙であるかを問わず、何らの保証もなく提供されます。
ここでいう保証とは、商品性、特定の目的への適合性、および権利非侵害についての保証も含みますが、
それに限定されるものではありません。作者または著作権者は、契約行為、不法行為、またはそれ以外であろうと、
ソフトウェアに起因または関連し、あるいはソフトウェアの使用またはその他の扱いによって生じる一切の請求、
損害、その他の義務について何らの責任も負わないものとします。
```
