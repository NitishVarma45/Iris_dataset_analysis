#This code can be used for Finding the species of the given iris based on petal length and width.
petal_length = float(input("Enter petal length: "))
petal_width = float(input("Enter petal width: "))
if((petal_length>0 and petal_length<2)and(petal_width>0 and petal_width<0.7)):
    print("Given iris is most likely a setosa.")
elif((petal_length>2.7 and petal_length<4.42)and(petal_width>0.98 and petal_width<1.71)):
    print("Given iris is most likely a versicolor.")
elif((petal_length>4.7 and petal_length<6.95)and(petal_width>1.71 and petal_width<2.51)):
    print("Given iris is most likely a virginica.")
else:
    print("Given variables can not be considered for classification.")    