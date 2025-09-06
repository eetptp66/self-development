import pandas as pd
import tensorflow as tf
from tensorflow import keras
from keras.layers import Dense

file = r'Study\tensorflow1-master\csv\lemonade.csv'
data = pd.read_csv(file)

print(data)

독립 = data[['온도']]
종속 = data[['판매량']]


print(독립.shape, 종속.shape)

print(data.columns)

X = tf.keras.layers.Input(shape = [1])
Y = tf.keras.layers.Dense(1)(X)

model = tf.keras.models.Model(X, Y)
model.compile(loss='mse')

model.fit(독립, 종속, epochs = 100, verbose = 0)

print("-------------------------------")
model.predict(독립)

print(종속)






