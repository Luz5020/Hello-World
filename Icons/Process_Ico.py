#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects
#  GNU General Public License v3.0
#  https://www.gnu.org/licenses/gpl-3.0.en.html
from PIL import Image, ImageFilter

amount = int(input("Amount of icons: "))
for i in range(amount):
    im = Image.open("Ico_"+str(i)+".png")
    img = im.convert("RGB")
    imgp = img.filter(ImageFilter.DETAIL)
    imgpp = imgp.filter(ImageFilter.SMOOTH_MORE)
    imgpp.save("Process_Ico_"+str(i)+".png")
