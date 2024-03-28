import os
import xlwings as xw
import openpyxl

# 入力フォルダのパス
input_folder = 'output'

# 入力フォルダ内のすべてのExcelファイルに対して処理を実行
for subdir, _, files in os.walk(input_folder):
    for file_name in files:
        if file_name.endswith('.xlsx'):
            input_file_path = os.path.join(subdir, file_name)
            
            # Excelアプリケーションを起動してワークブックを開く
            app = xw.App(visible=False)
            wb = app.books.open(input_file_path)
            
            # ワークブックを保存して閉じる（変更なし）
            wb.save()
            wb.close()
            app.quit()

