import csv
from pandas import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import requests
import os
import wget
# reading CSV file

df = read_csv("sopnil exel.csv")
df["Photo"] = ""
df.to_csv("sopnil exel.csv", index=False)

data =read_csv("sopnil exel.csv")

# converting column data to list
Name = data['Name'].tolist()
Student_Id = data['Email Address'].tolist()

arr = os.listdir('F:/sopnil/editedpic')
lis = []
for gig in arr:
    gi = str(gig[:-4])
    lis.append(gi)

final=[]
for lij in arr:
    hi=r'F:/sopnil/editedpic/' +str(lij)
    final.append(hi)
for si,rsi in zip(lis,final):
    k=(data[data['Email Address'] == si].index.values)
    for ii in k:
        sp=int(ii)
        data.loc[sp, "Photo"]=rsi
        data.to_csv("sopnil exel.csv", index=False)

