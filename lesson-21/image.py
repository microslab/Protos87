from PIL import Image, ImageDraw, ImageFont
import requests
import sys

# link = 'https://images.wallpaperscraft.ru/image/single/10_slova_nadpis_171433_2400x3600.jpg'
# rest = '2400x3600'
# link2 = 'https://images.wallpaperscraft.ru/image/single/10_slova_nadpis_171433_1080x1920.jpg'

def get_files_img(link, rest, link2):
    url = link
    res = rest.split('x')
    w1 = int(res[0])
    size1 = int((w1 / 1280) * 50)
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        pass
        # sys.exit(1)
    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        # sys.exit(1)
    img.save('temp/templase.jpg', 'jpeg')
    # img.close()


    try:
        watermark = Image.open("temp/templase.jpg")
    except:
        print("Unable to load image")
        # sys.exit(1)

    idraw = ImageDraw.Draw(watermark)
    text = "Protos ™"
    font = ImageFont.truetype("arial.ttf", size=size1)
    idraw.text((30, 30), text, font=font, stroke_width=1, stroke_fill='black')

    watermark.save('temp/templase.jpg')
    img.close()
    # watermark.close()
    get_files_imgmobi(link2)
    mokap_img()
    return 'good'


def get_files_imgmobi(link):
    url = link
    # h1 = 1920
    # size = int((h1 / 1280) * 20)
    try:
        resp = requests.get(url, stream=True).raw
    except requests.exceptions.RequestException as e:
        # sys.exit(1)
        pass
    try:
        img = Image.open(resp)
    except IOError:
        print("Unable to open image")
        # sys.exit(1)
    img.save('temp/templasemobi.jpg', 'jpeg')
    img.close()

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

def mokap_img():
    img1 = Image.open('temp/all_mokap.jpg')
    img2 = Image.open('temp/templase.jpg')
    img3 = Image.open('temp/templasemobi.jpg')
    # fixed_width = 568
    # width_percent = (fixed_width / float(img2.size[0]))
    # height_size = int((float(img2.size[0]) * float(width_percent)))
    # new_img = img2.resize((fixed_width, height_size))
    new_img = img2.resize((1005, 568))
    new_img1 = img3.resize((363, 675))


    img1.paste(new_img, (477, 202))
    img1.paste(new_img1, (31, 538))
    img1.save('temp/templasemokapall.jpg', 'jpeg')

    img1.close()
    img2.close()
    # img1 = Image.open('temp/templasemokapall.jpg')
    # img1.show()
    # img1.close()

    try:
        watermark = Image.open("temp/templasemokapall.jpg")
    except:
        print("Unable to load image")
        # sys.exit(1)
    h1 = 1920
    size = int((h1 / 1280) * 20)
    idraw = ImageDraw.Draw(watermark)
    text = "Protos ™"
    font = ImageFont.truetype("arial.ttf", size=size)
    idraw.text((10, 10), text, font=font, stroke_width=1, stroke_fill='black')

    watermark.save('temp/templasemokapall.jpg')
    watermark.close()


# get_files_img(link, rest, link2)