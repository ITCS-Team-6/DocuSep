import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, BatchNormalization

# pulling the arrays models
train_data = np.load(r"numpy/train_data.npy")
train_labels = np.load(r"numpy/train_labels.npy")
test_data = np.load(r"numpy/test_data.npy")
test_labels = np.load(r"numpy/test_labels.npy")

model = Sequential()








