import epaper
import os

picdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "pic"
)
libdir = os.path.join(
    os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "lib"
)
from PIL import Image, ImageDraw, ImageFont


class EPDText:
    def __init__(self, epd_size="epd2in7"):
        self.epd_size = epd_size
        self.epd = epaper.epaper(self.epd_size).EPD()

    def display_text(self, text="hello world"):
        self.epd.init()
        self.epd.Clear()
        font24 = ImageFont.truetype(
            os.path.join(
                picdir, os.path.dirname(__file__) + "/font/pixel_arial_11.ttf"
            ),
            24,
        )
        Himage = Image.new(
            "1", (self.epd.height, self.epd.width), 255
        )  # 255: clear the frame
        draw = ImageDraw.Draw(Himage)
        draw.text((10, 0), text, font=font24, fill=0)
        self.epd.display(self.epd.getbuffer(Himage))
        self.epd.sleep()
