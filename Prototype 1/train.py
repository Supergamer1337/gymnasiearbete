import tensorflow as tf # Import Tensorflow - https://www.tensorflow.org/guide/keras/train_and_evaluate
import numpy as np # Import Numpu - https://www.tensorflow.org/guide/keras/train_and_evaluate
from tensorflow import keras # Import Keras - https://www.tensorflow.org/guide/keras/train_and_evaluate
from tensorflow.keras import layers # Import Keras Layers - https://www.tensorflow.org/guide/keras/train_and_evaluate
from PIL import Image

# Get size and pixeldata
inputImage = Image.open('input.jpg')
width = inputImage.width
height = inputImage.height
inputData = list(inputImage.getdata())

# Create Model
model = tf.keras.Sequential()
model.add(layers.Dense(width*height, activation='linear', input_shape=(width*height,))) # Input Layer
model.add(layers.Dense(64)) # Hidden Layer 1
model.add(layers.Dense(128)) # Hidden Layer 2
model.add(layers.Dense(128)) # Hidden Layer 3
model.add(layers.Dense(3, activation='softmax')) # Output Layer
model.compile( # Compile The Model
        optimizer=tf.keras.optimizers.Adam(.0001),
        loss='categorical_crossentropy', # https://stackoverflow.com/a/62286888
        metrics=['accuracy'])

# Train


# Save Model