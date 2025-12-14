import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

iris = pd.read_csv("IRIS.csv")
sns.set_style("whitegrid")

features = [
    "sepal_length",
    "sepal_width",
    "petal_length",
    "petal_width"
]

for feature in features:
    plt.figure(figsize=(6, 4))
    
    sns.histplot(
        data=iris,
        x=feature,
        hue="species",
        bins=20,
        kde=True
    )
    
    plt.title(f"Distribution of {feature.replace('_', ' ').title()} by Species")
    plt.xlabel(feature.replace('_', ' ').title())
    plt.ylabel("Count")
    plt.show()
