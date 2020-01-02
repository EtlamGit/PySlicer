# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

class Box:

    def __init__(self, x, y, w, h, total_width, total_height):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.totalW = total_width
        self.totalH = total_height

    def scaleX(self, image_width):
        return self.x * image_width / self.totalW

    def scaleY(self, image_height):
        return self.y * image_height / self.totalH

    def scaleW(self, image_width):
        return self.w * image_width / self.totalW

    def scaleH(self, image_height):
        return self.h * image_height / self.totalH


def b256(x, y, w, h):
    return Box(x, y, w, h, 256, 256)


def b128(x, y, w, h):
    return Box(x, y, w, h, 128, 128)
