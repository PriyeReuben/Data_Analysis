import csv
import tkinter as tk
from tkinter import filedialog
import openpyxl


root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

filename = open(file_path, 'r')

print(type(file_path), file_path)
workbook = openpyxl.load_workbook(file_path)

workbook.get_sheet_by_name('2019_data_analyst_job')
worksheet = workbook.sheetnames[0]
worksheet2 = workbook[worksheet]
print(type(worksheet2), worksheet2)
worksheet



#next(file) #skip the first line of the file (headers)