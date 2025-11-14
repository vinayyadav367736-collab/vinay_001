#pandas is a python library designed for data mainpulation and anylasis
import pandas as pro

data = [12,23,34,45,56]
s = pro.Series(data)
print(s)


import pandas as pd 

data = {
    'Name': ['Ritik','Aman','Priya','Neha'],
    'Age':[21, 23, 20 ,22],
    'Marks':[85, 90, 78, 88]
}

dt = pd.DataFrame(data)
print(dt)

'''
practice question
["Math":90,"Science":85,"English":78]

1> print the series
2> Acces the marks for science

'''

data3 = {
    "Math":90,
    "Science":85,
    "English":78,
}

d = pd.Series(data3)
print(d)