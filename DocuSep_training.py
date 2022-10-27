import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPool2D, Flatten, Dense, BatchNormalization

# pulling the arrays models
train_data_H = np.load(r"numpy/train_data_H.npy")
train_labels_H = np.load(r"numpy/train_labels_H.npy")
test_data_H = np.load(r"numpy/test_data_H.npy")
test_labels_H = np.load(r"numpy/test_labels_H.npy")

#we use this model since we are dealing with a linear dataset
model = Sequential()

#this is our first layer, we pass the size of our images which is the 28 x 28 and then the 1 is the color,
#add padding to ensure that image shape doesn't change
model.add(Conv2D(filters = 32, kernel_size = (3, 3), activation = 'relu', padding = 'same', input_shape = (28, 28, 1)))
#we use maxpool to make the computing eaiser by setting a 2x2 grid over your "image"
model.add(MaxPool2D(pool_size = (2, 2)))
#we use this to normalize the data allowing us to use less epochs when training the model
model.add(BatchNormalization())

model.add(Conv2D(32, (3, 3), activation = 'relu', padding = 'same'))
model.add(MaxPool2D((2, 2), 2))
model.add(BatchNormalization())

#increase the filter size to account for the increase of complexity
model.add(Conv2D(64,(3, 3), activation = 'relu', padding = 'same'))
model.add(MaxPool2D((2, 2),2))
model.add(BatchNormalization())

model.add(Conv2D(64,(3, 3), activation = 'relu', padding = 'same'))
model.add(MaxPool2D((2, 2),2))
model.add(BatchNormalization())

#used to turn the data into a single array
model.add(Flatten())

#we use dense to preform predictions
model.add(Dense(64, activation = "relu"))
model.add(Dense(128, activation = "relu"))

#we 26 nuerons for this dense layer as that is the amount of lables we have,
#we use softmax to normalize output
model.add(Dense(26, activation = "softmax"))

#compiler information wee categorical because our result are 1 or 0 aka yes or no
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#result for training
train_result = model.fit(train_data_H, train_labels_H, epochs=1, validation_data=(test_data_H, test_labels_H))

#results for for puting test data against the trianed model
result = model.evaluate(test_data_H,test_labels_H)
print(result[0])
print(result[1])


