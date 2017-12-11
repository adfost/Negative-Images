Each folder named by a number contains the files that should be in MNIST_data (or whatever folder your program will use to look for data) for a dataset with that percentage of negative images in the training set (the test set is all negative images).

If you wish to create your own percentage, you can run “create_images.py” and modify the k value to get the correct percentage (more in “create_images.py”). Then, check in the directory “test” for the folder “training2” and “testing2”. Change the names of these folders to “training-images” and “test-images”, and run PNG2MNIST.py (available in both this directory and “test”).

The directory “old” contains the raw data from the original MNIST download.

MNIST2PNG.py is the code from https://github.com/myleott/mnist_png and PNG2MNIST.py is the code from https://github.com/gskielian/JPG-PNG-to-MNIST-NN-Format (Neither of these was written by me).

“linear.py” and “cnn.py” are the both from the Tensorflow site. https://www.tensorflow.org/tutorials/layers and https://www.tensorflow.org/get_started/mnist/beginners (Neither was written by me).

The raw MNIST images can be downloaded from the MNIST site. http://yann.lecun.com/exdb/mnist/ (Not made by me).