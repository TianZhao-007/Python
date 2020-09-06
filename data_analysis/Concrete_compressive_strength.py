import matplotlib.pyplot as plt
import numpy as np
import matplotlib
import xlrd

file_location = "F:\desktop\Assignment\Concrete_Data.xls"
data = xlrd.open_workbook(file_location)
sheet = data.sheet_by_index(0)

data = [[sheet.cell_value(r,c) for c in range(sheet.ncols)] for r in range(sheet.nrows)]

c_strength = [sheet.cell_value(r,8) for r in range(1,sheet.nrows)]

plt.hist(c_strength,bins=25,normed = 0,facecolor = "blue", edgecolor = "black",alpha = 0.5)
plt.xlabel("Concrete compressive strength(MPa, megapascals) ")
plt.ylabel("Frequency")
plt.title("Frequency distribution histogram")
plt.show()

# box plot
# red_square = dict(markerfacecolor='r', marker='s')
# fig6, ax = plt.subplots()
# plt.xlabel("Concrete compressive strength(MPa, megapascals) ")
# ax.set_title('Box and whisker plot for Concrete compressive strength')
# ax.boxplot(c_strength, flierprops=red_square, vert=False, whis=0.75)
# plt.show()

print(max(c_strength),min(c_strength))