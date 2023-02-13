import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

workbook1 = 'PROVA_PYTHON.xlsx'

#used to read the excel file in pandas --df = data frame
df_first_shift = pd.read_excel(workbook1)

print(df_first_shift)

# df_all = pd.concat([df_first_shift,df_second_shift,....]) #used to concatenate more than one excel file

#pick the values we want to graph

values = df_first_shift[['x','y']]
print(values)

ax = values.plot.bar(x='x',y='y',rot=0) #define a variable plot.type of graph ,x and y we have to use the location
plt.show() #show the plot