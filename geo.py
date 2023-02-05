from PIL import Image, ImageDraw

def create_earth():
    size = (200, 200)
    earth = Image.new("RGBA", size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(earth)
    draw.ellipse((0, 0, size[0], size[1]), fill=(0, 0, 255), outline=(0, 0, 0))
    draw.ellipse((30, 50, 70, 130), fill=(255, 255, 255, 0), outline=(0, 0, 0))
    draw.ellipse((60, 80, 120, 140), fill=(255, 255, 255, 0), outline=(0, 0, 0))
    earth.show()

create_earth()

# def create_earth():
#     size = (200, 200)
#     earth = Image.new("RGBA", size, (255, 255, 255, 0))
#     draw = ImageDraw.Draw(earth)
#     draw.ellipse((0, 0, size[0], size[1]), fill=(0, 128, 0), outline=(0, 128, 0))
#     draw.ellipse((30, 50, 70, 130), fill=(255, 255, 255, 0), outline=(0, 0, 0))
#     draw.ellipse((60, 80, 120, 140), fill=(255, 255, 255, 0), outline=(0, 0, 0))
#     draw.ellipse((90, 100, 170, 160), fill=(255, 255, 255, 0), outline=(0, 0, 0))
#     earth.show()
#
# create_earth()
