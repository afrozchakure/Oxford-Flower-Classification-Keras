#!/usr/bin/env python3

import os
import cv2
import numpy as np
from keras.models import load_model
from keras.utils import to_categorical
from scipy.io import loadmat

# Loading the model
model = load_model('classifier_4373per.h5')

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# Loading the labels
labelmat = loadmat('imagelabels.mat')
label = labelmat['labels']
label = label[0]

# Changing the label index
for i in range(len(label)):
    label[i] = label[i] - 1

# Loading setid
idmat = loadmat('setid.mat')
idmat.keys()
valid_num = idmat['valid']
valid_num = valid_num[0]
print("\nNumber of images in the validation set: {}".format(len(valid_num)))

# Making X_valid
valid = []
valid_label = []
for i in range(len(valid_num)):
    try:
        dir = 'jpg_valid/image' + '_' + str(valid_num[i]).zfill(5) + '.jpg'
        image = cv2.imread(dir)
        new_image = cv2.resize(image, (128, 128))
        new_image = new_image.astype('float32')
        new_image /= 255.0
        valid.append(new_image)
    except Exception as e:
        print(str(e))
X_valid = np.asarray(valid, dtype=np.float32)
print("Shape of X_valid : {}".format(X_valid.shape))

# Making y_both_train (y_train + y_test), y_valid
for i in range(len(valid_num)):
    valid_label.append(label[valid_num[i]-1])
valid_label = np.asarray(valid_label, dtype=np.float32)

# Changing y_valid to categorical form
y_valid = to_categorical(valid_label)  # valid_label
print("Shape of y_valid : {}".format(y_valid.shape))

# Displays model's architecture
print("\nSummary of Model's architecture:\n")
model.summary()

# Evaluating our model
print("\n\nEvaluating the Model:")
loss, acc = model.evaluate(X_valid, y_valid)

print("\nTrained model's Accuracy on Validation Set:")
print("accuracy: {}\nloss:  {}".format(acc*100, loss))
