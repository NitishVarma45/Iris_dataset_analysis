import numpy as np
import pandas as pd

iris = pd.read_csv("IRIS.csv")
print("Median:")
iris_setosa = iris[iris["species"]=="Iris-setosa"]
print(np.median(iris_setosa["petal_length"]))
iris_virginica = iris[iris["species"]=="Iris-virginica"]
print(np.median(iris_virginica["petal_length"]))
iris_versicolor = iris[iris["species"]=="Iris-versicolor"]
print(np.median(iris_versicolor["petal_length"]))

print("Percentile:")
print(np.percentile(iris_setosa["petal_length"],90))
print(np.percentile(iris_virginica["petal_length"],90))
print(np.percentile(iris_versicolor["petal_length"],90))

print("Quantile:")
print(np.percentile(iris_setosa["petal_length"],np.arange(0,100,25)))
print(np.percentile(iris_virginica["petal_length"],np.arange(0,100,25)))
print(np.percentile(iris_versicolor["petal_length"],np.arange(0,100,25)))