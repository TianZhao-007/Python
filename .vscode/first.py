import matplotlib.pyplot as mpl 
import numpy as np
import matplotlib
import xlrd

file_location = "F:\desktop\Assignment\Concrete_Data.xls"
data = xlrd.open_workbook(file_location)

sheet = data.sheet_by_index(0)

print(sheet)