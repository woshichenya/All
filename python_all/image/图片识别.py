from PIL import Image
import pytesseract
import traceback

def get_shoping_img_jiage():
    try:
        # png_names = png_names
        # box = box
        # image = Image.open(png_names)
        # newImage = image.crop(box)
        # newImage.save('a.png')
        c=open("b.png")
        im = Image.open("b.png")
        print(pytesseract.image_to_string(im))
        # jiage = pytesseract.image_to_string(im,lang='chi_sim')
        jiage = pytesseract.image_to_string(im)

        return jiage
    except Exception as e:
        ee = traceback.format_exc()
        print(ee)



get_shoping_img_jiage()