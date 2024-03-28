import os
import pandas as pd

# 'output/in'フォルダのパス
folder_path = 'output/in'

# 'output/in'フォルダ内のすべてのCSVファイルを処理
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # CSVファイルのパス
        csv_path = os.path.join(folder_path, filename)
        
        # CSVファイルを読み込む
        df = pd.read_csv(csv_path, header=None)
        
        # 'nan'という文字列を含む要素を削除
        df = df.replace('nan', pd.NA).dropna()
        
        # カンマをタブに置換し、小数点以下4桁まで出力
        df = df.applymap(lambda x: '{:.4f}'.format(x))
        
        # 出力先TXTファイルパス
        txt_path = os.path.join(folder_path, os.path.splitext(filename)[0] + '.in')
        
        # TXTファイルに出力（タブ区切り）
        df.to_csv(txt_path, sep='\t', index=False, header=False)
        
        # 元のCSVファイルを削除
        os.remove(csv_path)

print("処理が完了しました。")
