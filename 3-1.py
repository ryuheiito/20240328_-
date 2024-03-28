import os
import csv

def convert_out_to_csv(input_folder, output_folder):
    # フォルダが存在しない場合は作成する
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 'output/out'フォルダから.outファイルを取得
    out_files = [f for f in os.listdir(input_folder) if f.endswith('.out')]

    for file_name in out_files:
        input_path = os.path.join(input_folder, file_name)
        output_path = os.path.join(output_folder, os.path.splitext(file_name)[0] + '.csv')

        with open(input_path, 'r', encoding='utf-8') as in_file:
            # outファイルを読み込んで、内容をcsvに書き込む
            with open(output_path, 'w', newline='', encoding='utf-8') as out_file:
                writer = csv.writer(out_file)
                for idx, line in enumerate(in_file):
                    # 行の空白を削除してcsvに書き込む
                    if idx < 5:
                        writer.writerow([field.strip() for field in line.split(',')])
                    else:
                        writer.writerow([field.strip() for field in line.split()])

        print(f"{file_name} を {output_path} に変換しました。")

# 入力と出力のフォルダ
input_folder = 'output/out'
output_folder = 'output/out'

# 変換を実行
convert_out_to_csv(input_folder, output_folder)
