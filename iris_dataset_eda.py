import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

iris = pd.read_csv("IRIS.csv")

print(iris.shape) #Dimensions of the dataset.
print(iris.columns) #What column_names are present.
print(iris["species"].value_counts()) #Count of each species.

#Let's plot a scatter plot
iris.plot(kind='scatter',x='sepal_length',y='sepal_width')
plt.grid()
plt.show()

#As the plot above is a bit unclear, Lets make a better plot.
sns.set_style("whitegrid")
sns.FacetGrid(iris,hue="species",height = 4) \
.map(plt.scatter,'sepal_length','sepal_width') \
.add_legend()
plt.show()

#pair-plot : Better visualization.
sns.set_style("whitegrid")
sns.pairplot(iris, hue="species", size=3)
plt.show()
plt.show()
