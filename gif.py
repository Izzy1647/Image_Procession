import imageio
from PIL import Image
import os

def gifToPngs(gifUrl):   # gif转化为多张png

    gifFileName = gifUrl
    # 使用Image模块的open()方法打开gif动态图像时，默认是第一帧
    im = Image.open(gifFileName)
    pngDir = gifFileName[:-4]
    # 创建存放每帧图片的文件夹
    os.mkdir(pngDir)
    try:
        while True:
            # 保存当前帧图片
            current = im.tell()
            im.save(pngDir + '/' + str(current) + '.png')
            # 获取下一帧图片
            im.seek(current + 1)
    except EOFError:
        pass

# /Users/zzy/PycharmProjects/ImageProcession/img/sticker1
def pngsToGif(folderUrl):  # 文件夹中保存多张图片拼接
    # images = imgList
    imgList = []  # 从文件夹中读取图片
    for root, dirs, files in os.walk("/Users/zzy/PycharmProjects/ImageProcession/img/sticker1/"):
        for file in files:
            print(os.path.join(root, file))
            # print(type(os.path.join(root, file)))
            imgList.append(os.path.join(root, file))

    filename = '/Users/zzy/PycharmProjects/ImageProcession/img/result.gif'

    m = []
    for image in imgList:
        m.append(imageio.imread(image))
    imageio.mimsave(filename, m, 'GIF', duration=0.2)
#
# for root, dirs, files in os.walk("/Users/zzy/PycharmProjects/ImageProcession/img/sticker1/"):
#     for file in files:
#         print(os.path.join(root, file))
#         print(type(os.path.join(root, file)))

# list1 = []

# pngsToGif()

pngsToGif("/Users/zzy/PycharmProjects/ImageProcession/img/sticker1")