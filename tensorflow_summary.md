## Tensorflow Summary

### Tensorflow :
* It is a **free and open-source platform for high-performance numerical computation**, specifically for ML and Deep Learning.
* Has a **flexible architecture** and can be deployed across a variety of platforms (CPUs, GPUs and TPUs) as well as mobile and edge devices.
* Makes it **easy to build and deploy Machine Learning solutions**.

### Applications of Tensorflow :
 Tensorflow is used in applications such as Search Engines,Text Translation, Image Captioning, Recommendations, etc

### Installation of Tensorflow :
1. Installing tensorflow in python3
```
$ pip3 install tensorflow
```
2. Installing tensorflow in python2
```
$ pip install tensorflow
```
2. Install Tensorflow 2.0
```
$ pip install tensorflow==2.0.0-alpha0
```
3. Install Tensorflow in Anaconda Environment
```
$ conda install tensorflow
```

### Tensor 
  A tensor is a **typed multi-dimenstional array**. It can be 0-dimensional, 1-dimensional, 2-dimensional and 3-dimensional or n-dimensional.

### Types of Tensors :
1. Zero-dimensional - Scalar (magnitude only)
2. One-dimensional - Vector (magnitude and direction)
3. Two-dimensional - Matrix (table of numbers)
4. Three-dimensional - Matrix (cube of numbers)
5. N-dimensional - Matrix
   The rank of a tf.Tensor object is its number of dimensions. It is also called **order** or **degree**.

### Shape of a tensor :
* It is the **number of elements in each dimension**.
* To get the shape of a tensor we use :
```
>> tensor.shape
```

### Constant :
* It is a data structure in Tensorflow which when assigned, **its values can't be changed at the execution time**.
* Its initialization is with a value, not with an operation.
```
a = tf.constant([[1, 2], [3, 4]])
```

### Variable :
* They **store the state of graph in Tensorflow** and **are mutable (i.e. can be changed during execution)**.
* They need to be initialized while declaring it.
```
new_variable = tf.Variable([.5], dtype=tf.float32)
new_variable = tf.get_variable("my_variable", [1, 2, 3])
```
* Here its value can be changed using tf.assign().

### Placeholder :
* It is a variable which **doesn't hold a value initially and value to it can be assigned later**.
* The Data type of placeholder must be specified during the creation of placeholder.

### Important Part of Tensorflow:
1. #### Graph:
* It is the backbone of any Tensorflow program. 
* A Graph is **composed of a series of notes connected to each other by edges**. 
* Each node represents unit of computation and the edges represent the data consumed or produced by computation.
```python
tf.get_default_graph()
# Creating a new graph
graph = tf.graph()
# Printing all operations in a graph
print(graph.get_operations())
```

##### Advantages of Graphs :
* Parallelism
* Distributed execution
* Compilation
* Portability

2. #### Session:
* It **allocates resources**.
* Stores the actual values of intermediate results.
```
with tf.Session() as sess:  # Creating a session
# Perform operations here
```
**Mathematical operations of Tensorflow**
```python
>> tf.add(x,y)  # Add two tensors of same type, x+y
>> tf.sub(x, y) # Subtract two tensors of same type, x-y
>> tf.mul(x, y)  # Multiply two tensors element-wise
>> tf.pow(x, y) # Element-wise power of x to y
>> tf.exp(x)  # Equivalent to pow(e, x)
>> tf.sqrt(x)  # Equivlent to pow(x, 0.5)
>> tf.div(x, y)  # Element wise division of x and y
>> tf.truediv(x, y)  # Same as tf.div, but casts the arguments as float
>> tf.floordiv(x, y)  # Same as truediv, excepts rouds final answer to an integer
>> tf.mod(x, y)  # Element wise remainder from division
```

### Graph Visualizer
 It is a component of TensorBoard that **renders the structure of your graph visually in browser**.
```python
# Saving a graph for visualization
with tf.Session() as sess:
writer = tf.summary.FileWriter("/tmp/log/...", sess.graph)
```

### Eager Execution 
* Using eager execution **you can run your code without a session**. 
* It evaluates operations immediately, without building graphs.
```python
tf.enable_eager_execution()  # To enable eager execution in old versions of Tensorflow
```