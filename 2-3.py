import os
import pandas as pd

# 'output/in'フォルダのパス
folder_path = 'output/in'

# 出力する列の範囲（13列目から17列目に相当）
output_columns = [12, 13, 14, 15, 16]  # 0-indexedで考えると、13列目から17列目に相当

# 'output/in'フォルダ内のすべてのExcelファイルを処理
for filename in os.listdir(folder_path):
    if filename.endswith('.xlsx'):
        # Excelファイルのパス
        excel_path = os.path.join(folder_path, filename)
        
        # Excelファイルを読み込む
        df = pd.read_excel(excel_path, header=None)  # ヘッダーを無視して読み込む
        
        # 17列目が0の行のみ抽出
        filtered_df = df[df.iloc[:, 16] == 0]  # 17列目（0-indexed）がQ列に相当
        
        # 出力先CSVファイルパス
        output_csv_path = os.path.join(folder_path, os.path.splitext(filename)[0] + 'modifi.csv')
        
        # M-Q列をCSVに出力
        filtered_df.iloc[:, output_columns].round(4).to_csv(output_csv_path, index=False, header=False)  # 少数点以下4桁で出力
        
        # csvファイルを読み込む
        df_csv = pd.read_csv(output_csv_path, header=None)
        
        # 5列目を削除
        df_csv.drop(columns=[4], inplace=True)  # 0-indexedで考えると、5列目に相当
        
        # 出力先CSVファイルパス
        modified_csv_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.csv')
        
        # モディファイ後のCSVを出力
        df_csv.to_csv(modified_csv_path, index=False, header=False)
        
        # 元のCSVファイルを削除
        os.remove(output_csv_path)
        
        # 元のExcelファイルを削除
        os.remove(excel_path)

print("処理が完了しました。")
