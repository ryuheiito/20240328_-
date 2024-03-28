import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
import csv
import shutil

# inputフォルダ内のCSVファイルを読み込む
input_folder = 'input'
output_folder = 'output'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

input_file = os.path.join(input_folder, 'input.csv')

if not os.path.exists(input_file):
    print(f"{input_file}が見つかりません。")
    exit()

# CSVファイルから整数値を読み取り、URLを生成してデータを抽出
df = pd.read_csv(input_file, header=None, names=['整数'], encoding='shift-jis')

for index, row in df.iterrows():
    integer_value = row['整数']
    url = f'http://agora.ex.nii.ac.jp/digital-typhoon/summary/wnp/l/{integer_value}.html.ja'
    response = requests.get(url)
    
    # 1. outputにinteger_value名のフォルダを作成
    specific_output_folder = os.path.join(output_folder, str(integer_value))
    if not os.path.exists(specific_output_folder):
        os.makedirs(specific_output_folder)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser', from_encoding='shift-jis')
        tables = soup.find_all('table')
        
        if len(tables) >= 7:
            table = tables[6]  # 7番目の表を選択
            output_file = os.path.join(specific_output_folder, f'{integer_value}.csv')
            table_df = pd.read_html(str(table), encoding='shift-jis')[0]
            
            # ヘッダー行を緯度と経度に設定
            table_df.columns.values[4] = '緯度'
            table_df.columns.values[5] = '経度'
            
            # CSVファイルをUTF-8エンコーディングで保存
            table_df.to_csv(output_file, index=False, encoding='shift-jis')
                
            print(f'{integer_value}の7番目の表を抽出し、{output_file}に保存しました。')
        else:
            print(f'{integer_value}の7番目の表が見つかりませんでした。')
    else:
        print(f'{integer_value}のURLにアクセスできませんでした。')

    # 2. "covert_inputfile_v3.xlsx"をコピーして1で作成したフォルダに複製
    source_excel = os.path.join(input_folder, 'covert_inputfile_v3.xlsx')
    target_excel = os.path.join(specific_output_folder, f'{integer_value}.xlsx')
    if os.path.exists(source_excel):
        shutil.copy(source_excel, target_excel)

print('処理が完了しました。')
