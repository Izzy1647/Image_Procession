from PIL import Image
def getRGB(imgUrl):
    im = Image.open(imgUrl)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    sumR = 0
    sumG = 0
    sumB = 0
    for x in range(width):
        for y in range(height):
            sumR += pix[x, y][0]
            sumG += pix[x, y][1]
            sumB += pix[x, y][2]

    averR = sumR / (width * height)
    averG = sumG / (width * height)
    averB = sumB / (width * height)

    averRGB = (averR, averG, averB)
    print(averRGB)
    return averRGB

getRGB("/Users/zzy/PycharmProjects/ImageProcession/img/1.png")
        # print(pix[x,y])

