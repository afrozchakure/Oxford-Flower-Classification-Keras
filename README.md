## Oxford Flower DataSet Classification using Keras API

### Preprocessing and preparing training & testing sets
* Preprocessing is performed on the flowers dataset so that it can be fed into the model.
* We extract the y_train, y_test and y_valid values from **setid.mat** file.
* The **imagelabels.mat** file provides the labels for our images.
* I have used 7169 images for the training set (merged train and test labels) and the rest 1020 images (validation test labels) used for testing purposes.

### Making training, test and validation data
* Each of the images has been resized to 128 * 128 pixels format.
* Each of the image is devided by 255 so as to get values between 0 and 1.
* All the images are fed into the convolutional layer in the form of an array.

### Making the model
1. Here we have first initialised the Sequential model.
2. Then we have used 2 convolutional layers having input shape 128 X 128 pixels for our model, activation function as ReLU and 32 feature detector of size 3 * 3.
3. Two Max pooling layers of size 2 * 2 units have been used.
4. Next the flattening operation is performed to convert the pooled features into a single vector.
5. This flattened vector is fed into a hidden layer with 256 neurons which applies the ReLU activation function.
6. In the end we get the output as one of the flowers from 102 categories. Since we have more than 2 categories, we are using __softmax__ activation function.

### Compiling and Fitting the model to the training set
* We compile the model using the **Adam** optimizer with learning rate = 0.001 optimizer,  loss function **categorical_crossentropy**  and metrics as **accuracy**.
* At last we fit our model to the classifier with **40 epochs**.

### Docker Files include:
* **jpg_valid** - It is a directory which has 1020 images to be used for evaluating our model.
* **classifier_4373per.h5** - Model which gives accuracy of 43.73 on testing data (X_valid).
* **Dockerfile** - File containing the build dependencies for our image. Helps to Copy files to our image and define the command to launch when we are going to run our image. 
* **imagelabels.mat** && **setid.mat** - To get the id's and labels for our images.
* **inference.py** - This file contains the python program to inference our model.
* **requirements.txt** - It includes all the packages which are required for running our project.

__Note__ : I have used Ubuntu 16.04 as the base image for our docker image.

**DockerHub repo link** : https://hub.docker.com/repository/docker/afrozchakure/flowers
**Link to DataSet** : http://www.robots.ox.ac.uk/~vgg/data/flowers/102/index.html
