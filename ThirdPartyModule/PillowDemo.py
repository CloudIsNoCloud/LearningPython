'操作图像'

# 图像缩放
# from PIL import Image

# 打开一个图片
# im = Image.open('V:/1.jpg')
# 获得图像尺寸
# w, h = im.size
# print('Original image size: %s x %s' % (w, h))
# 缩放百分五十
# im.thumbnail((w//2, h//2))
# print('Resize image to: %s x %s' % (w//2, h//2))
# 把缩放后的图像用jpeg格式保存
# im.save('V:/2.jpg', 'jpeg')

# 模糊效果
# from PIL import ImageFilter
# 使用模糊
# im2 = im.filter(ImageFilter.BLUR)
# im2.save('V:/3.jpg', 'jpeg')

# 生成字母验证码图片
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


def rndChar():
    '''随机字母'''
    return chr(random.randint(65, 90))


def randerColor():
    '''随机颜色1'''
    return (random.randint(64, 255), random.randint(64, 255),
            random.randint(64, 255))


def randerColorTwo():
    '''随机颜色2'''
    return (random.randint(32, 127), random.randint(32, 127),
            random.randint(32, 127))


# 分辨率
width = 60 * 4
height = 60

image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象，字体要自己存到路径里面
font = ImageFont.truetype('V:/Arial.ttf', 36)
# 创建Draw对象
draw = ImageDraw.Draw(image)

# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=randerColor())

# 输出字母
for t in range(4):
    draw.text((60 * t + 10, 10), rndChar(), fill=randerColorTwo(), font=font)

# 模糊
image = image.filter(ImageFilter.BLUR)
image.save('V:/1.jpg', 'jpeg')
