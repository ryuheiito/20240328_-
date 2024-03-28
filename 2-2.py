import os
import openpyxl

# 'output'フォルダのパス
output_folder = 'output'

# 'in'フォルダのパス
input_folder = os.path.join(output_folder, 'in')

# 'in'フォルダが存在しない場合は作成する
if not os.path.exists(input_folder):
    os.makedirs(input_folder)

# 'output'フォルダ内のすべてのサブフォルダ内のExcelファイルを処理
for root, dirs, files in os.walk(output_folder):
    for filename in files:
        if filename.endswith('.xlsx'):
            # Excelファイルのパス
            excel_path = os.path.join(root, filename)
            
            # Excelファイルを読み込む
            wb = openpyxl.load_workbook(excel_path, data_only=True)
            
            # 対象シートを取得する
            ws = wb['1_台風データ貼り付け']
            
            # 出力先ファイルパス
            output_path = os.path.join(input_folder, filename)
            
            # Excelファイルを'in'フォルダに保存する
            wb.save(output_path)
