import serial
import csv
from datetime import datetime

# 串行連接設置
SERIAL_PORT = 'COM7'  # 將串行連接端口設置為COM7
BAUD_RATE = 115200

# CSV檔案名稱
CSV_FILENAME = '重度動作3.csv'

# 打開串行連接
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)

# 將資料分解為字典
def parse_data(data):
    data_dict = {}
    pairs = data.split(';')
    for pair in pairs:
        if ':' in pair:
            key, value = pair.split(':', 1)
            # 對於包含逗號的值，進一步分割
            if ',' in value:
                sub_values = value.split(',')
                for sub_value in sub_values:
                    # 確保每個子值都包含冒號
                    if ':' in sub_value:
                        sub_key, sub_val = sub_value.split(':')
                        data_dict[sub_key.strip()] = sub_val.strip()
            else:
                data_dict[key.strip()] = value.strip()
    return data_dict


# 將資料寫入CSV檔案
def write_to_csv(data_dict, timestamp, filename=CSV_FILENAME):
    # 檢查是否需要寫入標題
    try:
        with open(filename, 'x', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=list(data_dict.keys()) + ['timestamp'])
            writer.writeheader()
    except FileExistsError:
        pass

    # 寫入數據
    with open(filename, 'a', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=list(data_dict.keys()) + ['timestamp'])
        data_dict['timestamp'] = timestamp
        writer.writerow(data_dict)

# 無限循環，讀取串行數據
while True:
    if ser.in_waiting > 0:
        line = ser.readline().decode('utf-8').strip()
        if line.startswith("allData："):
            data = line.split("allData：")[1]
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            parsed_data = parse_data(data)
            write_to_csv(parsed_data, timestamp)
            print(f"Data saved: {data} at {timestamp}")
