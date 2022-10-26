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

#we use this model since we are dealing with a linear dataset
model = Sequential()
#this is our first layer, we pass the size of our images which is the 28 x 28 and then the 1 is the color
model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu', input_shape = (28, 28, 1)))
#we use maxpool to make the computing eaiser by setting a 2x2 grid over your "image"
model.add(MaxPool2D(pool_size = (2, 2)))
#we use this to normalize the data allowing us to use less epochs when training the model
model.add(BatchNormalization())

model.add(Conv2D(32, (3, 3), activation = 'relu',))
model.add(MaxPool2D((2, 2), 2))
model.add(BatchNormalization())



model.add(Flatten())
model.add(Dense())






