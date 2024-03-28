import pandas as pd
import os

# 出力するフォルダー
output_folder = "output/srt"
os.makedirs(output_folder, exist_ok=True)

# output/srt内のすべてのcsvファイルを処理
for file_name in os.listdir(output_folder):
    if file_name.endswith(".csv"):
        file_path = os.path.join(output_folder, file_name)
        
        # CSVファイルを読み込む
        df = pd.read_csv(file_path, header=None, sep=',')
        
        # txtファイルに出力
        output_filename = os.path.splitext(file_name)[0] + ".srt"
        output_path = os.path.join(output_folder, output_filename)
        
        # 各列のフォーマットを指定してtxtファイルに書き出す
        with open(output_path, 'w') as txt_file:
            for index, row in df.iterrows():
                line = '\t'.join(['%d' % row[0]] + ['%.3f' % num for num in row[1:4]] + ['%.1f' % num for num in row[4:]]) + '\n'
                txt_file.write(line)
