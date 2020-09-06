import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd

file_location = "F:\desktop\Assignment\Concrete_Data.xls"
data = xlrd.open_workbook(file_location)

sheet = data.sheet_by_index(0)

data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]
