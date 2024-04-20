from tensorflow.keras import layers
from tensorflow.keras import regularizers
import tensorflow as tf
import numpy as np


def func(t):
 return np.sin(1 + t * np.pi * 2) / 2 + 1


def get_regression_dataset(start=0, end=3, seed=1, samples=80):
 t = np.linspace(start, end, samples)
 oryginal = func(t)
 np.random.seed(seed)
 noisy = oryginal + np.random.normal(0, 0.2, samples)
 return noisy, oryginal

#define dataset
x_train, y_train  = get_regression_dataset()
x_test, y_test = get_regression_dataset(seed=2)

#define final list of metrics:
metrics_list = list()

#build models
model = tf.keras.Sequential(
 [
 tf.keras.layers.Dense(10, input_shape=(1,), activation="relu"),
 tf.keras.layers.Dropout(0.2),
 tf.keras.layers.Dense(100, activation="relu"),
 tf.keras.layers.Dropout(0.2),
 tf.keras.layers.Dense(1)
 ]
)
model.compile(optimizer='adam',
 loss='sparse_categorical_crossentropy',
 metrics=['MSE'])

model.fit(x_train, y_train, batch_size=1, epochs=3)
val_loss, val_MSE = model.evaluate(x_test, y_test)


