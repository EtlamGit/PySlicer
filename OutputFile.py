# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

import os.path
from PIL import Image


class OutputFile:

    def __init__(self, path, box):
        self.path = path
        self.box = box
        self.transformers = []

    def apply(self, transform):
        self.transformers.append(transform)

    def process(self, root, image):
        width, height = image.size

        output_path = os.path.join(root,  self.path)
        x = self.box.scaleX(width)
        y = self.box.scaleY(height)
        w = self.box.scaleW(width)
        h = self.box.scaleH(height)
        sub_image = image.crop((x, y, x+w, y+h))

        # apply optional transformations
        for op in self.transformers:
            if op == 'SQUARE':
                sub_image = self.SQUARE(sub_image)

        # create output path if necessary
        if not os.path.exists(os.path.dirname(os.path.abspath(output_path))):
            os.makedirs(os.path.dirname(os.path.abspath(output_path)))

        sub_image.save(output_path)

        # todo: what the hell is this doing?
        # graphics = image.getGraphics()
        # graphics.setColor(REMOVED_MARKER)
        # graphics.fillRect(x, y, w, h)

    def SQUARE(self, image):
        width, height = image.size
        dim = max(width, height)

        dx = int((dim -  width) / 2)
        dy = int((dim - height) / 2)

        new_image = Image.new('RGBA', (dim, dim), color=0)
        new_image.paste(image, (dx, dy, dx+width, dy+height))
        return new_image
