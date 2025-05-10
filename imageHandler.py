from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from io import BytesIO
import base64
from dataHandler import DataHandler

class ImageHandler:
    monthDayCount = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    IMGWIDTH = 1200
    IMGHEIGHT = 1400
    LUIMGWIDTH = 200
    LUIMGHEIGHT = 200
    TITLESIZE = 100
    NUMSIZE = 80

    
    def __init__(self, image_path: str):
        self.image_path = image_path
        self.image = None
        self.userName = ""
        self.month = None
        self.record = None
        self.userId = None

    @staticmethod
    def resizeOkImage(okImage):
        width = ImageHandler.LUIMGWIDTH
        height = ImageHandler.LUIMGHEIGHT
        okImage = okImage.resize((width, height))
        newImage = Image.new('RGBA', (int(width*1.5), int(height*1.5)), (255, 255, 255, 0))
        newImage.paste(okImage, (int(width/2), int(width*0.6)))
        newImage = newImage.resize((width, height))
        return newImage
    
    @staticmethod
    def getLuOkImage():
        okImage = Image.open("img/yes.png")
        luImage = Image.open("img/lu.png")
        luImage = luImage.resize((ImageHandler.LUIMGWIDTH, ImageHandler.LUIMGHEIGHT))
        okImage = ImageHandler.resizeOkImage(okImage)
        okLuImage = Image.alpha_composite(luImage, okImage)
        return okLuImage
    
    @staticmethod
    def getLuImage():
        luImage = Image.open("img/lu.png")
        luImage = luImage.resize((ImageHandler.LUIMGWIDTH, ImageHandler.LUIMGHEIGHT))
        return luImage
    

    def getImage(self):
        self.image = Image.new('RGBA', (self.IMGWIDTH, self.IMGHEIGHT), (255, 255, 255, 0))
        draw = ImageDraw.Draw(self.image)
        formalFont = ImageFont.truetype("font/STXINGKA.TTF", self.TITLESIZE)
        titleText = str(self.month)+"月份 " + self.userName + " 打卡记录"
        draw.text((self.TITLESIZE/2, self.TITLESIZE/2), titleText, font=formalFont, fill=(0, 0, 0, 255))
        okLuImage = ImageHandler.getLuOkImage()
        
        luImage = ImageHandler.getLuImage()
        for i in range(self.monthDayCount[self.month]):
            day = i+1
            count = DataHandler.getCount(self.userId, self.month, day)
            if count == 0:
                self.image.paste(luImage, ((day%6)*self.LUIMGWIDTH, (day//6)*self.LUIMGHEIGHT + self.TITLESIZE*2), luImage)
            else :
                self.image.paste(okLuImage, ((day%6)*self.LUIMGWIDTH, (day//6)*self.LUIMGHEIGHT + self.TITLESIZE*2), okLuImage)       
                if count[0] != 1 :
                    formalFont = ImageFont.truetype("font/STHUPO.TTF", int(self.NUMSIZE*0.8))
                    draw.text(((day%6)*self.LUIMGWIDTH+self.TITLESIZE+self.NUMSIZE//2, (day//6)*self.LUIMGHEIGHT + self.TITLESIZE*2+self.TITLESIZE+self.NUMSIZE//2), str(count[0]), font=formalFont, fill=(255, 0, 0, 255))
            formalFont = ImageFont.truetype("font/STCAIYUN.TTF", self.NUMSIZE)
            draw.text(((day%6)*self.LUIMGWIDTH, (day//6)*self.LUIMGHEIGHT + self.TITLESIZE*2), str(day), font=formalFont, fill=(0, 0, 0, 255))

        background = Image.new('RGBA', (self.IMGWIDTH, self.IMGHEIGHT), (249,245,215, 255))
        self.image = Image.alpha_composite(background, self.image)
        buffer = BytesIO()
        self.image.save(buffer, format="PNG")
        imageData = buffer.getvalue()
        base64_image = base64.b64encode(imageData).decode('utf-8')
        data_url = f"data:image/png;base64,{base64_image}"
        return data_url
