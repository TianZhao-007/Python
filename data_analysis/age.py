import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd

file_location = "F:\desktop\Assignment\Concrete_Data.xls"
data = xlrd.open_workbook(file_location)

sheet = data.sheet_by_index(0)

# print(sheet.cell_value(0,0))

# print(sheet.nrows)

# print(sheet.ncols)

# for col in range(sheet.ncols):
#     print(sheet.cell_value(0,col))

# for col in range(sheet.ncols):
#     print(sheet.cell_value(2,col))

# data stores all information in the excel
data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

# print the attribute 'Days' out
# for row in range(1,sheet.nrows):
#     print(data[row][7])

# days = [sheet.cell_value(r,7) for r in range(1,sheet.nrows)]

# print(max(days),min(days))

# hist for age

# plt.hist(days,bins=25,normed = 0,facecolor = "blue", edgecolor = "black",alpha = 0.5)
# plt.xlabel("Age(days)")
# plt.ylabel("Frequency")
# plt.title("Frequency distribution histogram for Age(days)")
# plt.show()

# box plot
# red_square = dict(markerfacecolor='r', marker='s')
# fig6, ax = plt.subplots()
# plt.xlabel("Age(days)")
# ax.set_title('Box and whisker plot for Age')
# ax.boxplot(days, flierprops=red_square, vert=False, whis=0.75)
# plt.show()
