

from pandas import *
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

# reading CSV file
data = read_csv("sopnil exel.csv")

# converting column data to list
Name = data['Name'].tolist()
Em_Id = data['Email Address'].tolist()


where_will_pic_save = []
for r in Em_Id:
    ss = 'F:/sopnil/editedpic/' + str(r) + '.png'
    where_will_pic_save.append(ss)

for name, new_pic in zip(Name, where_will_pic_save):
    mimage = Image.open('F:/sopnil/certificate participation.png')

    font_type = ImageFont.truetype("arialbd.ttf", 200, encoding="unit8")


    text1 = name
    w, h = font_type.getsize(text1)
    draw = ImageDraw.Draw(mimage)
    draw.text(xy=((4892-w)/2, (3488-h)/2), text=text1,  fill=(0, 0, 0), font=font_type)


    mimage.save(new_pic)