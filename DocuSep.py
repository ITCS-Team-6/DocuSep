#need to import these packages
#also need tensorflow on for backend sklearn and keras need tensorflow to work but don't need to import it 
import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from keras.utils import to_categorical
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split

#link for dataset: https://www.kaggle.com/datasets/sachinpatel21/az-handwritten-alphabets-in-csv-format
#Digital: https://www.kaggle.com/datasets/adamkaniasty/digital-letters
#pathing will determine where your files are located
data = r"Datasets/Handwritten/A_Z Handwritten Data.csv"
data_2 = r"Datasets/Machine/digital_letters.csv"

#variables to load the dataset csvs
dataset = pd.read_csv(data).astype("float32")
dataset.rename(columns={'0': "label"}, inplace=True)
#creating variables that correspond to the data within the CSV file
dataset = pd.read_csv(data).astype("float32")
dataset_2 = pd.read_csv(data_2)

#renaming the first column in the csv file and naming it label
dataset.rename(columns={'0': "label"}, inplace=True)
dataset_2.rename(columns={'0': "label"}, inplace=True)

#variables being passed the data and removing the label column from the letter variable
letter_x = dataset.drop("label", axis = 1)
letter_x_2 = dataset_2.drop("label", axis=1)
#creating the varuable that is assigned to the label
letter_y = dataset["label"]
letter_y_2 = dataset_2["label"]

#variable associated to the letters within the csv file
letter_x = letter_x.values
letter_x_2 = letter_x_2.values

print(letter_x.shape, letter_y.shape)
print(letter_x_2.shape, letter_y_2.shape)

#creating an empty array
data = []

#reshaping the array to fit the 28 x 28 format of the images
for smash in letter_x:
    image = np.reshape(smash, (28,28,1))
    data.append(image)

#creating a variable that has the data that is then created to numpy array
letter_data = np.array(data, dtype=np.float32)
letter_target = letter_y

print(letter_data.shape, letter_target.shape)

# shuffle_data = shuffle(letter_data)
# rows,cols = 10 ,10

# plt.figure(figsize=(20,20))
#
# for i in range (rows * cols):
#     plt.subplot(cols, rows, i+1)
#     plt.imshow(shuffle_data[i].reshape(28,28), interpolation="nearest", cmap="gray")
#
# plt.show()

#assigning these varaibles to the letters itself and the labels
data = letter_data
target = letter_target

# print(data.shape, target.shape)

#creating varaibles for training and testing
train_data, test_data, train_labels, test_labels = train_test_split(data, target , test_size=0.2)

# print(train_data.shape, train_labels.shape)
# print(test_data.shape, test_labels.shape)

#normalizing the data to make the pixel range 0-1
train_data = train_data / 255.0
test_data = test_data / 255.0

#setting the label variables to categorical formats
train_labels = to_categorical(train_labels, num_classes= 26, dtype= 'int')
test_labels = to_categorical(test_labels, num_classes= 26, dtype= 'int')

#turning the data into 4d array
train_data = train_data.reshape(train_data.shape[0], train_data.shape[1], train_data.shape[2], 1)
test_data = test_data.reshape(test_data.shape[0], test_data.shape[1], test_data.shape[2], 1)

print(train_data.shape, train_labels.shape)
print(test_data.shape, test_labels.shape)

#saving the numpy arrays  data to use for training...uncomment for these to save to your machine 
# np.save(r"numpy/train_data", train_data)
# np.save(r"numpy/train_labels", train_labels)
# np.save(r"numpy/test_data", test_data)
# np.save(r"numpy/test_labels", test_labels)
