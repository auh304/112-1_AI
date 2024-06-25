import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.metrics import classification_report, confusion_matrix


# 模型路徑，根據您保存模型的位置進行修改
model_path = 'path_to_your_saved_model.h5'

# 加載訓練好的模型
model = tf.keras.models.load_model(r"D:\model\model.h5")

# 您的新數據
data = {
    'FLex_Sensor1': [-106, -106, -106, -106, -106],
    'FLex_Sensor2': [-57, -58, -57, -57, -57],
    'FLex_Sensor3': [-96, -96, -96, -96, -96],
    'FLex_Sensor4': [23, 25, 20, 24, 24],
    'FLex_Sensor5': [66, 13, -54, 166, 17],
    'Orient_Y': [2.81, 2.81, 2.81, 2.81, 2.81],
    'Orient_Z': [10.5, 10.56, 10.69, 10.81, 11.06],
    'Gyro_Y': [0.01, 0, 0.01, 0.01, 0.05],
    'Gyro_Z': [0.01, 0.01, 0.01, -0.02, -0.03],
    'Accel_Y': [-1.62, -1.72, -1.68, -1.64, -1.88],
    'Accel_Z': [9.65, 9.63, 9.66, 9.75, 9.54],
    'action': [1, 1, 1, 1, 1]
}

# 轉換為DataFrame
new_data = pd.DataFrame(data)

# 標準化特徵
scaler = StandardScaler()
scaled_features = scaler.fit_transform(new_data)  # 假設您已經用訓練集的數據fit過scaler

# 使用模型進行預測
predictions = model.predict(scaled_features)

# 如果模型的輸出是獨熱編碼，我們需要將其轉換為原始標籤
predicted_labels = np.argmax(predictions, axis=1)

# 打印預測結果
print(predicted_labels)
