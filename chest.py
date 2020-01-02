# copyright 2020 EtlamGit

import os
import os.path
from PIL import Image


class Chest:
    def __init__(self, image_dimension_64):
        self.scale = image_dimension_64 / 64.0

    def scale_it(self, ox, oy, dx, dy):
        return (int(ox * self.scale), int(oy * self.scale), int(ox * self.scale + dx * self.scale), int(oy * self.scale + dy * self.scale))


# helper to get texture bounding box in OLD format
class ChestOld(Chest):
    # locker
    def l_top(self):    return self.scale_it(1, 0, 2, 1)
    def l_bottom(self): return self.scale_it(3, 0, 2, 1)
    def l_left(self):   return self.scale_it(0, 1, 1, 4)
    def l_front(self):  return self.scale_it(1, 1, 2, 4)
    def l_right(self):  return self.scale_it(3, 1, 1, 4)
    def l_back(self):   return self.scale_it(4, 1, 2, 4)
    # top lid
    def t_top(self):    return self.scale_it(14,  0, 14, 14)
    def t_inside(self): return self.scale_it(28,  0, 14, 14)
    def t_left(self):   return self.scale_it( 0, 14, 14,  5)
    def t_front(self):  return self.scale_it(14, 14, 14,  5)
    def t_right(self):  return self.scale_it(28, 14, 14,  5)
    def t_back(self):   return self.scale_it(42, 14, 14,  5)
    # bottom container
    def b_inside(self): return self.scale_it(14, 19, 14, 14)
    def b_bottom(self): return self.scale_it(28, 19, 14, 14)
    def b_left(self):   return self.scale_it( 0, 33, 14, 10)
    def b_front(self):  return self.scale_it(14, 33, 14, 10)
    def b_right(self):  return self.scale_it(28, 33, 14, 10)
    def b_back(self):   return self.scale_it(42, 33, 14, 10)


class DoubleChestOld(Chest):
    # locker
    def l_top1(self):    return self.scale_it(1, 0, 1, 1)
    def l_top2(self):    return self.scale_it(2, 0, 1, 1)
    def l_bottom1(self): return self.scale_it(3, 0, 1, 1)
    def l_bottom2(self): return self.scale_it(4, 0, 1, 1)
    def l_left(self):    return self.scale_it(0, 1, 1, 4)
    def l_front1(self):  return self.scale_it(1, 1, 1, 4)
    def l_front2(self):  return self.scale_it(2, 1, 1, 4)
    def l_right(self):   return self.scale_it(3, 1, 1, 4)
    def l_back1(self):   return self.scale_it(4, 1, 1, 4)
    def l_back2(self):   return self.scale_it(5, 1, 1, 4)
    # top lid
    def t_top1(self):    return self.scale_it(14,  0, 15, 14)
    def t_top2(self):    return self.scale_it(29,  0, 15, 14)
    def t_inside1(self): return self.scale_it(44,  0, 15, 14)
    def t_inside2(self): return self.scale_it(59,  0, 15, 14)
    def t_left(self):    return self.scale_it( 0, 14, 14,  5)
    def t_front1(self):  return self.scale_it(14, 14, 15,  5)
    def t_front2(self):  return self.scale_it(29, 14, 15,  5)
    def t_right(self):   return self.scale_it(44, 14, 14,  5)
    def t_back1(self):   return self.scale_it(58, 14, 15,  5)
    def t_back2(self):   return self.scale_it(73, 14, 15,  5)
    # bottom container
    def b_inside1(self): return self.scale_it(14, 19, 15, 14)
    def b_inside2(self): return self.scale_it(29, 19, 15, 14)
    def b_bottom1(self): return self.scale_it(44, 19, 15, 14)
    def b_bottom2(self): return self.scale_it(59, 19, 15, 14)
    def b_left(self):    return self.scale_it( 0, 33, 14, 10)
    def b_front1(self):  return self.scale_it(14, 33, 15, 10)
    def b_front2(self):  return self.scale_it(29, 33, 15, 10)
    def b_right(self):   return self.scale_it(44, 33, 14, 10)
    def b_back1(self):   return self.scale_it(58, 33, 15, 10)
    def b_back2(self):   return self.scale_it(73, 33, 15, 10)


# helper to get texture bounding box in NEW format
class ChestNew(Chest):
    # locker
    def l_bottom(self): return self.scale_it(1, 0, 2, 1)
    def l_top(self):    return self.scale_it(3, 0, 2, 1)
    def l_left(self):   return self.scale_it(0, 1, 1, 4)
    def l_back(self):   return self.scale_it(1, 1, 2, 4)
    def l_right(self):  return self.scale_it(3, 1, 1, 4)
    def l_front(self):  return self.scale_it(4, 1, 2, 4)
    # top lid
    def t_inside(self): return self.scale_it(14,  0, 14, 14)
    def t_top(self):    return self.scale_it(28,  0, 14, 14)
    def t_left(self):   return self.scale_it( 0, 14, 14,  5)
    def t_right(self):  return self.scale_it(14, 14, 14,  5)
    def t_back(self):   return self.scale_it(28, 14, 14,  5)
    def t_front(self):  return self.scale_it(42, 14, 14,  5)
    # bottom container
    def b_bottom(self): return self.scale_it(14, 19, 14, 14)
    def b_inside(self): return self.scale_it(28, 19, 14, 14)
    def b_left(self):   return self.scale_it( 0, 33, 14, 10)
    def b_right(self):  return self.scale_it(14, 33, 14, 10)
    def b_back(self):   return self.scale_it(28, 33, 14, 10)
    def b_front(self):  return self.scale_it(42, 33, 14, 10)


class DoubleChestNew(Chest):
    # locker
    def l_bottom(self):  return self.scale_it(1, 0, 1, 1)
    def l_top(self):     return self.scale_it(2, 0, 1, 1)
    def l_left(self):    return self.scale_it(0, 1, 1, 4)
    def l_back(self):    return self.scale_it(1, 1, 1, 4)
    def l_right(self):   return self.scale_it(2, 1, 1, 4)
    def l_front(self):   return self.scale_it(3, 1, 1, 4)
    # top lid
    def t_inside1(self): return self.scale_it(14,  0, 15, 14)
    def t_inside2(self): return self.scale_it(14,  0, 15, 14)
    def t_top1(self):    return self.scale_it(29,  0, 15, 14)
    def t_top2(self):    return self.scale_it(29,  0, 15, 14)
    def t_left(self):    return self.scale_it( 0, 14, 14,  5)
    def t_front1(self):  return self.scale_it(43, 14, 15,  5)
    def t_front2(self):  return self.scale_it(43, 14, 15,  5)
    def t_right(self):   return self.scale_it(29, 14, 14,  5)
    def t_back1(self):   return self.scale_it(14, 14, 15,  5)
    def t_back2(self):   return self.scale_it(14, 14, 15,  5)
    # bottom container
    def b_bottom1(self): return self.scale_it(14, 19, 15, 14)
    def b_bottom2(self): return self.scale_it(14, 19, 15, 14)
    def b_inside1(self): return self.scale_it(29, 19, 15, 14)
    def b_inside2(self): return self.scale_it(29, 19, 15, 14)
    def b_left(self):    return self.scale_it( 0, 33, 14, 10)
    def b_front1(self):  return self.scale_it(43, 33, 15, 10)
    def b_front2(self):  return self.scale_it(43, 33, 15, 10)
    def b_right(self):   return self.scale_it(29, 33, 14, 10)
    def b_back1(self):   return self.scale_it(14, 33, 15, 10)
    def b_back2(self):   return self.scale_it(14, 33, 15, 10)


def transform_chest(input_root, output_root, input_file):
    base_folder = 'assets/minecraft/textures/entity/chest/'
    if os.path.exists(input_root + base_folder + input_file):
        img = Image.open(input_root + base_folder + input_file)
        # create new chest
        new_chest = Image.new('RGBA', img.size, color=0)
        # get bounding box helpers
        oc = ChestOld(min(img.size))
        nc = ChestNew(min(img.size))
        # locker part
        new_chest.paste(img.crop(oc.l_top())   .transpose(Image.FLIP_TOP_BOTTOM), nc.l_top())
        new_chest.paste(img.crop(oc.l_bottom()),                                  nc.l_bottom())
        new_chest.paste(img.crop(oc.l_left())  .transpose(Image.ROTATE_180),      nc.l_left())
        new_chest.paste(img.crop(oc.l_front()) .transpose(Image.ROTATE_180),      nc.l_front())
        new_chest.paste(img.crop(oc.l_right()) .transpose(Image.ROTATE_180),      nc.l_right())
        new_chest.paste(img.crop(oc.l_back())  .transpose(Image.ROTATE_180),      nc.l_back())
        # top part
        new_chest.paste(img.crop(oc.t_top())   .transpose(Image.FLIP_TOP_BOTTOM), nc.t_top())
        new_chest.paste(img.crop(oc.t_inside()).transpose(Image.FLIP_TOP_BOTTOM), nc.t_inside())
        new_chest.paste(img.crop(oc.t_left())  .transpose(Image.ROTATE_180),      nc.t_left())
        new_chest.paste(img.crop(oc.t_front()) .transpose(Image.ROTATE_180),      nc.t_front())
        new_chest.paste(img.crop(oc.t_right()) .transpose(Image.ROTATE_180),      nc.t_right())
        new_chest.paste(img.crop(oc.t_back())  .transpose(Image.ROTATE_180),      nc.t_back())
        # bottom part
        new_chest.paste(img.crop(oc.b_inside()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_inside())
        new_chest.paste(img.crop(oc.b_bottom()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_bottom())
        new_chest.paste(img.crop(oc.b_left())  .transpose(Image.ROTATE_180),      nc.b_left())
        new_chest.paste(img.crop(oc.b_front()) .transpose(Image.ROTATE_180),      nc.b_front())
        new_chest.paste(img.crop(oc.b_right()) .transpose(Image.ROTATE_180),      nc.b_right())
        new_chest.paste(img.crop(oc.b_back())  .transpose(Image.ROTATE_180),      nc.b_back())

        # create output path if necessary
        if not os.path.exists(os.path.abspath(output_root + base_folder)):
            os.makedirs(os.path.abspath(output_root + base_folder))

        new_chest.save(output_root + base_folder + input_file)


def transform_doublechest(input_root, output_root, input_file):
    base_folder = 'assets/minecraft/textures/entity/chest/'
    if os.path.exists(input_root + base_folder + input_file):
        img = Image.open(input_root + base_folder + input_file)
        width = min(img.size)
        # create new chest
        new_chest_L = Image.new('RGBA', (width, width), color=0)
        new_chest_R = Image.new('RGBA', (width, width), color=0)
        # get bounding box helpers
        oc = DoubleChestOld(width)
        nc = DoubleChestNew(width)
        # locker part
        new_chest_R.paste(img.crop(oc.l_top1())   .transpose(Image.FLIP_TOP_BOTTOM), nc.l_top())
        new_chest_R.paste(img.crop(oc.l_bottom1()),                                  nc.l_bottom())
        new_chest_R.paste(img.crop(oc.l_left())   .transpose(Image.ROTATE_180),      nc.l_left())
        new_chest_R.paste(img.crop(oc.l_back1())  .transpose(Image.FLIP_TOP_BOTTOM), nc.l_back())
        new_chest_R.paste(img.crop(oc.l_front1()) .transpose(Image.ROTATE_180),      nc.l_front())
        new_chest_L.paste(img.crop(oc.l_top2())   .transpose(Image.FLIP_TOP_BOTTOM), nc.l_top())
        new_chest_L.paste(img.crop(oc.l_bottom2()),                                  nc.l_bottom())
        new_chest_L.paste(img.crop(oc.l_back2())  .transpose(Image.FLIP_TOP_BOTTOM), nc.l_back())
        new_chest_L.paste(img.crop(oc.l_right())  .transpose(Image.ROTATE_180),      nc.l_right())
        new_chest_L.paste(img.crop(oc.l_front2()) .transpose(Image.ROTATE_180),      nc.l_front())
        # top part
        new_chest_R.paste(img.crop(oc.t_top1())   .transpose(Image.FLIP_TOP_BOTTOM), nc.t_top1())
        new_chest_L.paste(img.crop(oc.t_top2())   .transpose(Image.FLIP_TOP_BOTTOM), nc.t_top2())
        new_chest_R.paste(img.crop(oc.t_inside1()).transpose(Image.FLIP_TOP_BOTTOM), nc.t_inside1())
        new_chest_L.paste(img.crop(oc.t_inside2()).transpose(Image.FLIP_TOP_BOTTOM), nc.t_inside2())
        new_chest_R.paste(img.crop(oc.t_left()) .transpose(Image.ROTATE_180), nc.t_left())
        new_chest_R.paste(img.crop(oc.t_front1()).transpose(Image.ROTATE_180), nc.t_front1())
        new_chest_L.paste(img.crop(oc.t_front2()).transpose(Image.ROTATE_180), nc.t_front2())
        new_chest_L.paste(img.crop(oc.t_right()).transpose(Image.ROTATE_180), nc.t_right())
        new_chest_L.paste(img.crop(oc.t_back1()) .transpose(Image.ROTATE_180), nc.t_back1())
        new_chest_R.paste(img.crop(oc.t_back2()) .transpose(Image.ROTATE_180), nc.t_back2())
        # bottom part
        new_chest_R.paste(img.crop(oc.b_inside1()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_inside1())
        new_chest_L.paste(img.crop(oc.b_inside2()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_inside2())
        new_chest_R.paste(img.crop(oc.b_bottom1()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_bottom1())
        new_chest_L.paste(img.crop(oc.b_bottom2()).transpose(Image.FLIP_TOP_BOTTOM), nc.b_bottom2())
        new_chest_R.paste(img.crop(oc.b_left()) .transpose(Image.ROTATE_180), nc.b_left())
        new_chest_R.paste(img.crop(oc.b_front1()).transpose(Image.ROTATE_180), nc.b_front1())
        new_chest_L.paste(img.crop(oc.b_front2()).transpose(Image.ROTATE_180), nc.b_front2())
        new_chest_L.paste(img.crop(oc.b_right()).transpose(Image.ROTATE_180), nc.b_right())
        new_chest_L.paste(img.crop(oc.b_back1()) .transpose(Image.ROTATE_180), nc.b_back1())
        new_chest_R.paste(img.crop(oc.b_back2()) .transpose(Image.ROTATE_180), nc.b_back2())

        # create output path if necessary
        if not os.path.exists(os.path.abspath(output_root + base_folder)):
            os.makedirs(os.path.abspath(output_root + base_folder))

        new_chest_L.save(output_root + base_folder + input_file.replace('double', 'left'))
        new_chest_R.save(output_root + base_folder + input_file.replace('double', 'right'))
