from PIL import Image, ImageDraw, ImageFont
import requests
import sys

def get_files_img(link, rest, type1, link2):
    url = link
    res = rest.split('x')
    w1 = int(res[0])
    size1 = int((w1 / 1280) * 50)
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        sys.exit(1)
    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        sys.exit(1)
    img.save('temp/templase.jpg', 'jpeg')

    try:
        watermark = Image.open("temp/templase.jpg")
    except:
        print("Unable to load image")
        sys.exit(1)

    idraw = ImageDraw.Draw(watermark)
    text = "Protos ™"
    font = ImageFont.truetype("arial.ttf", size=size1)
    idraw.text((30, 30), text, font=font, stroke_width=1, stroke_fill='black')

    watermark.save('temp/templase.jpg')
    get_files_imgmobi(link2)


def get_files_imgmobi(link):
    url = link
    # h1 = 1920
    # size = int((h1 / 1280) * 20)
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        sys.exit(1)
    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        sys.exit(1)
    img.save('temp/templasemobi.jpg', 'jpeg')

    # try:
    #     watermark = Image.open("temp/templasemobi.jpg")
    # except:
    #     print("Unable to load image")
    #     sys.exit(1)
    #
    # idraw = ImageDraw.Draw(watermark)
    # text = "Protos ™"
    # font = ImageFont.truetype("arial.ttf", size=size)
    # idraw.text((10, 10), text, font=font, stroke_width=1, stroke_fill='black')
    #
    # watermark.save('temp/templasemobi.jpg')