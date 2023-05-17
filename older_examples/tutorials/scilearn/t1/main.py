from math import gamma
from string import digits
from pandas import array
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
from sklearn import svm #Vector Classification
import matplotlib.pyplot as plt

# import pandas as pd

print(digits.data)

print("----------------------------------")

print(digits.target)

# estimator (Object ->) for classification, fit(X, y) and predict(T)

clf = svm.SVC(gamma=0.001, C=100.) #manually set gamma

classf = clf.fit(digits.data[:-1], digits.target[:-1])

print(classf)

predict_last_digit = clf.predict(digits.data[-1:]) # predict last digit

print(predict_last_digit) 

# print(array([8]))

# plt.gray()
# plt.matshow(predict_last_digit)
# plt.show


# >>> from sklearn.datasets import load_digits
# >>> digits = load_digits()
# >>> print(digits.data.shape)
# (1797, 64)
# >>> import matplotlib.pyplot as plt
# >>> plt.gray()
# >>> plt.matshow(digits.images[0])
# <...>
# >>> plt.show()