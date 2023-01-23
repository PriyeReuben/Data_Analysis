import math
import csv
import tkinter as tk
from tkinter import filedialog
import matplotlib.pyplot as plt



def pcc():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    filename = open(file_path, 'r')

    file = csv.reader(filename)

    next(file) #skip the first line of the file (headers)


    var1 = []
    var2 = []

    #populate the variable lists
    for line in file:
        var1.append(float(line[0]))
        var2.append(float(line[1]))
    print(var1)
    print(var2)

    v1_MD = []  # Mean Difference
    v2_MD = []

    v1_MDS = []  # Mean Difference Squared
    v2_MDS = []

    MD_product = []

    mean_var1 = math.fsum(var1) / len(var1)
    mean_var2 = math.fsum(var2) / len(var2)

    pcc = 0

    for i in var1:
        x = i - mean_var1
        v1_MD.append(x)

        x_squared = math.pow(x, 2)
        v1_MDS.append(x_squared)

    for i in var2:
        x = i - mean_var2
        v2_MD.append(x)

        x_squared = math.pow(x, 2)
        v2_MDS.append(x_squared)

    for i in range(0, len(var1)):
        MD_product.append((v1_MD[i] * v2_MD[i]))

    v1_MDS_sum = math.fsum(v1_MDS)
    v2_MDS_sum = math.fsum(v2_MDS)
    MD_product_sum = math.fsum(MD_product)

    v1_final = math.sqrt(v1_MDS_sum)
    v2_final = math.sqrt(v2_MDS_sum)

    try:
        pcc = MD_product_sum / (v1_final * v2_final)
        plt.scatter(var1, var2)
        plt.title(pcc)
        plt.show()
        return pcc
    except:
        pcc = 0
        return pcc


print(pcc())

