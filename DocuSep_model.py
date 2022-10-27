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
data_H = r"Datasets/Handwritten/A_Z Handwritten Data.csv"
data_D = r"Datasets/Machine/digital_letters.csv"

#variables to load the dataset csvs
dataset_H = pd.read_csv(data_H).astype("float32")
dataset_H.rename(columns={'0': "label"}, inplace=True)
#creating variables that correspond to the data within the CSV file
dataset_D = pd.read_csv(data_D).astype("float32")

#renaming the first column in the csv file and naming it label
dataset_H.rename(columns={'0': "label"}, inplace=True)
dataset_D.rename(columns={'0': "label"}, inplace=True)

#variables being passed the data and removing the label column from the letter variable
letter_H = dataset_H.drop("label", axis = 1)
letter_D = dataset_D.drop("label", axis=1)

#creating the varuable that is assigned to the label
label_H = dataset_H["label"]
label_D = dataset_D["label"]

#variable associated to the letters within the csv file
letter_H = letter_H.values
letter_D = letter_D.values

print(letter_H.shape, label_H.shape)
print(letter_D.shape, label_D.shape)

#creating an empty array
data_H = []

#reshaping the array to fit the 28 x 28 format of the images
for smash in letter_H:
    image = np.reshape(smash, (28,28,1))
    data_H.append(image)

#creating a variable that has the data that is then created to numpy array
letter_data_H = np.array(data_H, dtype=np.float32)
letter_label_H = label_H

print(letter_data_H.shape, letter_label_H.shape)

# shuffle_data = shuffle(letter_data_H)
# rows,cols = 10 ,10

# plt.figure(figsize=(20,20))
#
# for i in range (rows * cols):
#     plt.subplot(cols, rows, i+1)
#     plt.imshow(shuffle_data[i].reshape(28,28), interpolation="nearest", cmap="gray")
#
# plt.show()

#assigning these varaibles to the letters itself and the labels
data_H = letter_data_H
label_obj_H = letter_label_H
    
# print(data_H.shape, label_obj_H.shape)

#creating varaibles for training and testing
train_data_H, test_data_H, train_labels_H, test_labels_H = train_test_split(data_H, label_obj_H , test_size=0.2)

# print(train_data_H.shape, train_labels_H.shape)
# print(test_data_H.shape, test_labels_H.shape)

#normalizing the data to make the pixel range 0-1
train_data_H = train_data_H / 255.0
test_data_H = test_data_H / 255.0

#setting the label variables to categorical formats
train_labels_H = to_categorical(train_labels_H, num_classes= 26, dtype= 'int')
test_labels_H = to_categorical(test_labels_H, num_classes= 26, dtype= 'int')

#turning the data into 4d array
train_data_H = train_data_H.reshape(train_data_H.shape[0], train_data_H.shape[1], train_data_H.shape[2], 1)
test_data_H = test_data_H.reshape(test_data_H.shape[0], test_data_H.shape[1], test_data.shape[2], 1)

print(train_data_H.shape, train_labels_H.shape)
print(test_data_H.shape, test_labels_H.shape)

#saving the numpy arrays  data to use for training...uncomment for these to save to your machine 
# np.save(r"numpy/train_data_H", train_data_H)
# np.save(r"numpy/train_labels_H", train_labels_H   )
# np.save(r"numpy/test_data_H", test_data_H)
# np.save(r"numpy/test_labels_H", test_labels_H)
