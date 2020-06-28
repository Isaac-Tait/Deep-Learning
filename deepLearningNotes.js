/*Deep Learning Notes
Artificial Neural Networks (ANN) are built with neurons (or nodes). If a ANN has more than one hidden layer it is called a deep ANN.

//* Deep Learning Diagram

To write the above diagram in Keras you would use the following: */

Layers = [
	Dense(units=4, input_shape=(3,), activation=‘relu’),
	Dense (units=2, activation=‘softmax’)
]

/*Dense is a type of layer, there are many different types (e.g. Dense (or fully connected), Convolutional, Pooling, Recurrent, Normalization).

Each connection between nodes has an associated weight. 

Forward pass - Data moving through the model from input to output. A single pass of the entire dataset to the network is called an Epoch.

In an ANN, an activation function is a function that maps a node's inputs to its corresponding output. There are many types but two examples are ReLU and Sigmoid (graphs below).

//* ReLU & Sigmoid Diagrams

Activation functions can be either linear or non-linear.

We train a network by optimizing the weights of the connections between nodes to reduce loss as much as possible. 

The most widely known optimizer is called stochastic gradient descent, or more simply, SGD.
https://keras.io/api/optimizers/

SGD
RMSprop
Adam
Adadelta
Adagrad
Adamax
Nadam
Ftrl

One common loss function is mean squared error (MSE).

The learning rate tells us how large of a step we should take in the direction of the minimum.
A learning rate is a small number usually ranging between 0.01 and 0.0001*/

model.fit(
x=scaled_train_samples,
y=train_labels,
batch_size=10,
epochs=20,
shuffle=True,
verbose=2
)

/*scaled_train_samples is a numpy array consisting of the training samples.

train_labels is a numpy array consisting of the corresponding labels for the training samples.

batch_size=10 specifies how many training samples should be sent to the model at once.

epochs=20 means that the complete training set (all of the samples) will be passed to the model a total of 20 times.

shuffle=True indicates that the data should first be shuffled before being passed to the model.

verbose=2 indicates how much logging we will see as the model trains.

The loss function is what the optimizer is attempting to minimize by iteratively updating the weights in the ANN.

https://keras.io/api/losses/
The currently available loss functions for Keras are as follows:

mean_squared_error
mean_absolute_error
mean_absolute_percentage_error
mean_squared_logarithmic_error
squared_hinge
hinge
categorical_hinge
logcosh
categorical_crossentropy
sparse_categorical_crossentropy
binary_crossentropy
kullback_leibler_divergence
poisson
cosine_proximity

Learning rates is a hyper parameter. 

Data for our model is broken down into three distinct sets:
//? Training Set (updates the weights, includes labels)
//? Validation Set (does not update the weights, includes labels)
//? Test Set (does not update the weights, does not include labels).

Labels are necessary to so that the loss and accuracy can be determined from each epoch.*/