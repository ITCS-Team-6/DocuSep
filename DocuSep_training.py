import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, BatchNormalization

# pulling the arrays models
train_data = np.load(r"numpy/train_data.npy")
train_labels = np.load(r"numpy/train_labels.npy")
test_data = np.load(r"numpy/test_data.npy")
test_labels = np.load(r"numpy/test_labels.npy")

#these are parameters that go into these parenthesis except sequential, testing to figure out what numbers and such work
#also these are layers added to train the data the dataset hasnt been applied
#may need more of each testing
model = Sequential()

model.add(Conv2D()
model.add(BatchNormalization())
model.add(MaxPool2D()

model.add(Flatten())
model.add(Dense())






