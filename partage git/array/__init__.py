from array import array
import openpyxl

# for a in dir(array):
#    print(a)
a=array('H',[100,200,450,150,2000])
print (sum(a))
print (a[0:4])
wb=openpyxl.load_workbook("c:/users/esic/documents/classeur1.xlsx")
