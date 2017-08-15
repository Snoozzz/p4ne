from matplotlib import pyplot
from openpyxl import load_workbook

wb = load_workbook('data_analysis_lab.xlsx')
sheet = wb['Data']

def getvalue(x):
    return x.value

x=list(map(getvalue, sheet['A'][1:]))
y=list(map(getvalue, sheet['B'][1:]))
z=list(map(getvalue, sheet['C'][1:]))

pyplot.plot(x, y, label="Отношения")
pyplot.plot(x, z, label="Активность")
pyplot.show()