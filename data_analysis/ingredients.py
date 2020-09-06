import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd
import pandas as pd
import scipy.stats as stats
import scipy.optimize as opt

file_location = "F:\desktop\Assignment\Concrete_Data.xls"
data = xlrd.open_workbook(file_location)

sheet = data.sheet_by_index(0)

# data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

data = [[sheet.cell_value(r,c) for r in range(sheet.nrows)] for c in range(sheet.ncols)]
# print(data[0][1:])
# data = [data[0][1:], data[1][1:], data[2][1:],data[3][1:],data[4][1:],data[5][1:],data[6][1:]]
# fig7, ax7 = plt.subplots()
# ax7.set_title('Seven components of ingredients')
# ax7.boxplot(data)
# plt.show()

# SCATTER PLOT FOR THE RELATIONSHIP BETWEEN CONCRETE AND AGE

# y = data[8][1:]
# x = data[7][1:]

colors = (0,0,0)

# plt.scatter(x, y, c=colors, alpha=0.5)
# plt.title('Scatter plot')
# plt.xlabel('Age(days)')
# plt.ylabel('Concrete compressive strength(MPa, megapascals)')
# plt.show()



for i in range(1,sheet.nrows):
    if data[7][i]==3:
        a = a+1
        plt.scatter(data[7][i], data[8][i], c=colors, alpha=0.5)
        

for i in range(1,sheet.nrows):
    if data[7][i]==28:
        b = b+1
        plt.scatter(data[7][i],data[8][i], c=colors, alpha=0.5)
    
# r, p=stats.pearsonr(s_1,s_2) 
plt.show()

