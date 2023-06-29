import os
import openpyxl

wb = openpyxl.Workbook()
ws = wb.active


root = 'C:\\Users\\shravanjerry\\OneDrive\\Documents\\GitHub\\project_data_files\\weed detection project'

for path, subdirs, files in os.walk(root):
    for name in files:
        p = os.path.join(path, name)
        p = p[2:].strip()
        l =[p]
        ws.append(l)
        

wb.save('pathlist.xlsx')