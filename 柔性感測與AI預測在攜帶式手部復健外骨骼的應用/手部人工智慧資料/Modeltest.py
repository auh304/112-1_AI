import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import load_model
from sklearn.preprocessing import StandardScaler

# 模型路徑，根據您保存模型的位置進行修改
model_path = r"D:\model\model.h5"

# 加載訓練好的模型
model = load_model(model_path)

# 讀取CSV文件中的數據
csv_path = '測試2.csv'  # 修改為您的CSV文件路徑
data = pd.read_csv(csv_path)

# 選擇需要的特徵列
feature_columns = ['FLex_Sensor1', 'FLex_Sensor2', 'FLex_Sensor3', 
                   'FLex_Sensor4', 'FLex_Sensor5', 'Orient_Y', 'Orient_Z', 
                   'Gyro_Y', 'Gyro_Z', 'Accel_Y', 'Accel_Z', 'action']
new_data = data[feature_columns]

# 標準化特徵
scaler = StandardScaler()
scaled_features = scaler.fit_transform(new_data)  # 假設您已經用訓練集的數據fit過scaler

# 使用模型進行預測
predictions = model.predict(scaled_features)

# 如果模型的輸出是獨熱編碼，我們需要將其轉換為原始標籤
predicted_labels = np.argmax(predictions, axis=1)

# 打印預測結果
print(predicted_labels)
