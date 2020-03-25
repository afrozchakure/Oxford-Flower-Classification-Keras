## CNN Summary 

### Convolutional Layer : 
 It is a layer of deep neural network in which a **convolutional filter passes along the input matrix**.

### Convolutional Neural Network (CNN)
* A neural network in which atleast one layer is a **convolutional layer**.
* Depending on features, we categorize the images (classify) using CNN.
* __Yann Lecun__ ---> Grandfather of Convolutionl neural network.

### Steps involved in a Convolutional Neural Network :
1. Convolution Operation.
  b. ReLU Layer.
2. Pooling.
3. Flattening.
4. Full Connection.

![](extras/cnn_blackbox.png)

### 1. **Convolution Operation** :
 * In this process, we reduce the size of image by passing the input image through a **Feature detector/Filter/Kernel** so as to convert it into a **Feature Map/ Convolved feature/ Activation Map**
 * It helps remove the unnecessary details from the image.
 * We can create many feature maps (detects certain features from the image) to obtain our first convolution layer.
 * Involves element-wise multiplication of convolutional filter with the slice of an input matrix and finally the summation of all values in the resulting matrix.

![](extras/convolution_operation.png)

### **Stride**: 
  The number of pixels we are moving the filter over the input matrix is called a **stride**.

   ### b. **ReLU Activation Function** :
* ReLU is the most commonly used activation function in the world. 
* When applying convolution, there is a risk we might create something linear and there we need to break linearity. 
* Rectified Linear unit can be described by the function **f(x) = max(x, 0)**.
* We are applying the rectifier to increase the non-linearity in our image/CNN. Rectifier **keeps only non-negative values of an image**.


### 2. **Pooling** :
 * It helps to reduce the spatial size of the convolved feature which in-turn helps to **to decrease the computational power required to process the data**.
 * Here we are able to **preserve the dominant features**, thus helping in the process of effectively training the model.
 * Converts the **Feature Map** into a **Pooled Feature Map**.

   It is Divided into 2 types:
     1. **Max Pooling** - Returns the max value from the portion of image covered by the kernel.
     2. **Average Pooling** - Returns the average of all values from the portion of image covered by the kernel.

### 3. **Flattening** : 
   Involves converting a **Pooled feature Map** into a **Column vector**

### 4. **Full Connection** : 
 * The flattened output is fed to a feed-forward neural network with backpropagation applied to every iteration.
 * Over a series of epocs, the model is able to identiy dominating features and low-level features in image and classify them using the **Softmax Classification** technique (It brings the output values between 0 and 1).

![](extras/cnn2.png)