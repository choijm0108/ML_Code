import os
from PIL import Image
from goolge.colab import files

uploaded = files.upload()

import pandas as pd

for fn in uploaded.keys() :
    print('user uploaded file "{name}"" with length {length} bytes'.format(
        name=fn, length = len(uploaded[fn])))

import numpy as np
import matplotlib.pyplot as plt

import tensorflow as tf
from tensorflow import keras


print(tf.__version__)
print(keras.__version__)
print("Hello World!")

