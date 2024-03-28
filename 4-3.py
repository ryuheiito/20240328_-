import pandas as pd
import os

# 出力するフォルダー
output_folder = "output/srt"
os.makedirs(output_folder, exist_ok=True)

# output/srt内のすべてのxlsxファイルを処理
for file_name in os.listdir("output/srt"):
    if file_name.endswith(".xlsx"):
        file_path = os.path.join("output/srt", file_name)
        
        # Excelファイルを読み込む
        df = pd.read_excel(file_path, sheet_name='4_inputfile', header=None)
        
        # 出力する行数（7列目1行目の数値）
        rows_to_output = int(df.iloc[0, 6])
        
        # 不要なコメントを削除する
        df.iloc[1:, 6] = df.iloc[1:, 6].apply(lambda x: x.replace("'", ""))
        
        # CSVファイルに出力
        output_filename = os.path.splitext(file_name)[0] + ".csv"
        output_path = os.path.join(output_folder, output_filename)
        df.iloc[1:rows_to_output+1, 6:12].to_csv(output_path, header=False, index=False, float_format='%.5f,%.5f,%.5f,%.2f,%.2f', quoting=1)
