#!/usr/bin/env python3

from os import listdir
from os.path import isfile, join, splitext
import os
import sys
import datetime, time
import csv

def create_gpx_header():
    return '<?xml version="1.0" encoding="utf-8" standalone="yes"?>\n<gpx version="1.1" creator="csv2gpx" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">\n'

def create_gpx_footer():
    return '</gpx>'

cwd = os.getcwd()
in_files = [f for f in listdir(cwd) if isfile(join(cwd, f))]

file_count = 0
for in_file in in_files:
    if in_file.endswith(".csv"):
        file_count += 1
        print(f"\n処理中: {in_file} ({file_count})")
        
        # CSVファイルのベースネームを取得（拡張子なし）
        basename = splitext(in_file)[0]
        
        # 各CSVファイルに対応するGPXファイルを作成
        out_filename = f"{basename}.gpx"
        
        try:
            # CSVファイルをcsvモジュールで読み込む（引用符の処理が適切に行われる）
            valid_lines = []
            with open(in_file, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                header = next(reader)  # ヘッダー行を読み込む
                print(f"ヘッダー行: {','.join(header)}")
                
                # ヘッダーから位置情報のカラムインデックスを特定
                position_index = None
                lat_index = None
                lon_index = None
                utc_index = None
                
                # 必要なカラムのインデックスを取得
                if "Position" in header:
                    position_index = header.index("Position")
                elif "Latitude" in header and "Longitude" in header:
                    lat_index = header.index("Latitude")
                    lon_index = header.index("Longitude")
                
                # UTCカラムがあるか確認
                if "UTC" in header:
                    utc_index = header.index("UTC")
                
                # 行カウンタ
                line_count = 0
                valid_count = 0
                
                # データ行を処理
                for row in reader:
                    line_count += 1
                    
                    # 空の行はスキップ
                    if not row:
                        continue
                    
                    try:
                        # タイムスタンプを取得
                        timestamp = int(row[0])
                        
                        # UTC時間文字列（存在する場合）
                        utc_time_str = None
                        if utc_index is not None and utc_index < len(row):
                            utc_time_str = row[utc_index]
                        
                        # 位置情報を取得
                        lat, lon = None, None
                        
                        if position_index is not None:
                            # "lat,lon" 形式の位置情報を分解
                            if position_index < len(row):
                                pos_str = row[position_index]
                                pos_parts = pos_str.split(',')
                                if len(pos_parts) == 2:
                                    lat, lon = pos_parts
                                else:
                                    print(f"  警告: 行 {line_count+1} の位置情報のフォーマットが無効です: {pos_str}")
                        elif lat_index is not None and lon_index is not None:
                            # 別々のカラムから緯度・経度を取得
                            if lat_index < len(row) and lon_index < len(row):
                                lat = row[lat_index]
                                lon = row[lon_index]
                        
                        # 有効な位置情報があるか確認
                        if lat and lon:
                            valid_count += 1
                            # 必要なデータを含む配列を作成 (タイムスタンプ, UTC時間文字列, 緯度, 経度)
                            valid_lines.append([timestamp, utc_time_str, lat, lon])
                            
                            # 最初の数件だけサンプルとして表示
                            if valid_count <= 3:
                                # UTCでの時間を表示
                                utc_time = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
                                print(f"  有効データ {valid_count}: UTC時間={utc_time}, 緯度={lat}, 経度={lon}")
                                if utc_time_str:
                                    print(f"    CSVのUTC列={utc_time_str}")
                        else:
                            print(f"  警告: 行 {line_count+1} の位置情報が無効または見つかりません")
                            
                    except ValueError as e:
                        print(f"  警告: 行 {line_count+1} のデータ変換エラー: {str(e)}")
                    except IndexError:
                        print(f"  警告: 行 {line_count+1} のデータ形式が不正です")
                
                print(f"CSVファイルの行数: {line_count + 1}")  # ヘッダー行を含む
                print(f"有効なデータ行数: {valid_count}")
            
            # GPXファイルに書き込む
            with open(out_filename, "w") as out_file:
                # GPXヘッダーを書き込む
                out_file.write(create_gpx_header())
                
                # データをGPXトラックとして書き込む
                if valid_lines:
                    out_file.write(f"<trk>\n  <name>{basename}</name>\n  <trkseg>\n")
                    for line in valid_lines:
                        timestamp, utc_time_str, lat, lon = line
                        
                        # UTC時間文字列がCSVにある場合はそれを使う
                        if utc_time_str and utc_time_str.endswith('Z'):
                            time_str = utc_time_str
                        else:
                            # UnixタイムスタンプからUTC時間を生成する
                            time_str = datetime.datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')
                        
                        out_file.write(f"    <trkpt lat=\"{lat}\" lon=\"{lon}\">\n      <time>{time_str}</time>\n    </trkpt>\n")
                    out_file.write("  </trkseg>\n</trk>\n")
                else:
                    print("警告: トラックポイントがありません。空のGPXファイルが作成されます。")
                
                # GPXフッターを書き込む
                out_file.write(create_gpx_footer())
            
            print(f"作成完了: {out_filename}")
            
        except Exception as e:
            import traceback
            print(f"ファイル処理中にエラーが発生: {str(e)}")
            print(traceback.format_exc())

print(f"\n全 {file_count} ファイルの処理が完了しました。")