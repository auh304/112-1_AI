import os
import pandas as pd

# 資料夾路徑和目標資料夾名稱
folder_path = 'C:\lohaowei\Data\alldata'
output_folder = 'C:\lohaowei\Data\cleandata'

# 建立目標資料夾
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 讀取資料夾中的xls檔案
for filename in os.listdir(folder_path):
    if filename.endswith('.xls'):
        file_path = os.path.join(folder_path, filename)
        output_file = os.path.splitext(filename)[0] + '.xlsx'
        output_path = os.path.join(output_folder, output_file)
        print(file_path)

        # 讀取xls檔案
        df = pd.read_excel(file_path, header=None)
        print(df)

        # 檢查第0欄是否包含LA或LC，並保存符合條件的行
        # filtered_df = df[df.iloc[:, 0].isin(['LA', 'LC', 'LB', 'LD', 'LF', 'LI', 'LE'])]

        selected_row_col0 = df.iloc[[9, 10, 11, 12, 13, 14, 27],0]
        selected_row_col5 = df.iloc[[9, 10, 11, 12, 13, 14, 27],5]
        selected_row_col6 = df.iloc[[9, 10, 11, 12, 13, 14, 27],6]
        selected_row_col7 = df.iloc[[9, 10, 11, 12, 13, 14, 27],7]

        merged_data = pd.concat([selected_row_col0,selected_row_col5,selected_row_col6,selected_row_col7], axis=1)
        print(merged_data)

        # 儲存為xlsx檔案
        merged_data.to_excel(output_path, index=False, header=None)