import tensorflow as tf 
import numpy as np 
import matplotlib.pyplot as plt

print(tf.__version__)

data = tf.keras.datasets.fashion_mnist

(train_images, train_labesl), (test_images, test_labels) = data.load_data()

print(train_images.shape)