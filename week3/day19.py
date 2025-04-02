# from PIL import Image
#
# img = Image.open('photo.jpg')
#
# print('格式：', img.format)
# print('尺寸：', img.size)
# print('模式：', img.mode)
#
# img.show()
#
# box = (100, 100, 400, 400)
# cropped_img = img.crop(box)
# cropped_img.show()
#
# new_size = (img.width//2, img.height//2)
# resized_img = img.resize(new_size)
# resized_img.show()
#
# img.thumbnail((200, 200))
# img.show()
#
# rotated_img = img.rotate(45)
# rotated_img.show()
#
# flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
# flipped_img.show()
#
# from PIL import ImageDraw, ImageFont
#
# draw = ImageDraw.Draw(img)
# font = ImageFont.truetype('arial.ttf', 36)
#
# draw.text((10, 10), 'Sample Watermark', fill=(255, 0, 0), font=font)
# img.show()
# img.save('watermarked.jpg')
#
# from PIL import ImageFilter
#
# blur_img = img.filter(ImageFilter.BLUR)
# blur_img.show()
#
# contour_img = img.filter(ImageFilter.CONTOUR)
# contour_img.show()
#
#
#
# from PIL import Image
#
#
# def adjust_brightness_manual(img, factor):
#     """ 手动调整亮度 """
#     img = img.convert("RGB")  # 确保是 RGB 模式
#     pixels = img.load()  # 获取像素数据
#
#     for i in range(img.width):
#         for j in range(img.height):
#             r, g, b = pixels[i, j]  # 获取像素
#             pixels[i, j] = (
#                 min(int(r * factor), 255),
#                 min(int(g * factor), 255),
#                 min(int(b * factor), 255)
#             )  # 计算新像素值
#
#     return img
#
#
# img = Image.open("photo.jpg")
# bright_img = adjust_brightness_manual(img, 1.2)
# bright_img.show()
from PIL import Image, ImageDraw, ImageFont
import datetime


def process_id_photo(input_path, output_path):
    # 打开原始照片
    img = Image.open(input_path)

    # 裁剪居中区域
    width, height = img.size
    crop_size = min(width, height)
    left = (width - crop_size) // 2
    top = (height - crop_size) // 2
    cropped = img.crop((left, top, left + crop_size, top + crop_size))

    # 调整尺寸
    id_photo = cropped.resize((413, 626))

    # 替换蓝色背景为红色
    for x in range(id_photo.width):
        for y in range(id_photo.height):
            r, g, b = id_photo.getpixel((x, y))

            # 识别蓝色背景（B 最大，且 B > 150）
            if b > r and b > g and b > 150:
                id_photo.putpixel((x, y), (255, 0, 0))  # 替换为红色

    # 添加日期水印
    draw = ImageDraw.Draw(id_photo) 
    font = ImageFont.truetype("arial.ttf", 20)
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    draw.text((10, 600), date_str, fill=(255, 255, 255), font=font)

    # 保存
    id_photo.save(output_path)
    print("证件照生成成功！")


# 使用示例
process_id_photo("photo.jpg", "id_photo_red.jpg")
