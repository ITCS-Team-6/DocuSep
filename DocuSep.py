#need to import these packages
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import tensorflow as tf
import tensorflow_datasets as tfds
from extra_keras_datasets import emnist
from keras.utils import np_utils
from keras.datasets import mnist
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

#link for dataset: https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format
#pathing will determine where your files are located
data = r"Datasets/Handwritten/A_Z Handwritten Data.csv"


dataset = pd.read_csv(data).astype("float32")
dataset.rename(columns={'0': "label"}, inplace=True)

letter_x = dataset.drop("label", axis = 1)
letter_y = dataset["label"]

letter_x = letter_x.values

print(letter_x.shape, letter_y.shape)

data = []

for flatten in letter_x:
    image = np.reshape(flatten, (28,28,1))
    data.append(image)

letter_data = np.array(data, dtype=np.float32)
letter_target = letter_y

print(letter_data.shape, letter_target.shape)

shuffle_data = shuffle(letter_data)
rows,cols = 10 ,10

plt.figure(figsize=(20,20))

for i in range (rows * cols):
    plt.subplot(cols, rows, i+1)
    plt.imshow(shuffle_data[i].reshape(28,28), interpolation="nearest", cmap="gray")

plt.show()
