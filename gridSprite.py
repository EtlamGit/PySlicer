# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from OutputFile import OutputFile
from Box        import b256


def gridSprite(path, x, y, w, h, x_offset, y_offset, x_scale, y_scale):
    return OutputFile(path, b256(x_scale * x + x_offset, y_scale * y + y_offset, w * x_scale, h * y_scale))

