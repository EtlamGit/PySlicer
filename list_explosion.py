# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from OutputFile import OutputFile
from Box        import *


def explosion(path, x, y):
    return OutputFile("assets/minecraft/textures/particle/" + path + ".png", b128(32 * x, 32 * y, 32, 32))


explosion_input = 'assets/minecraft/textures/entity/explosion.png'
explosion_list = {
    explosion("explosion_0", 0, 0),
    explosion("explosion_1", 1, 0),
    explosion("explosion_2", 2, 0),
    explosion("explosion_3", 3, 0),

    explosion("explosion_4", 0, 1),
    explosion("explosion_5", 1, 1),
    explosion("explosion_6", 2, 1),
    explosion("explosion_7", 3, 1),

    explosion("explosion_8", 0, 2),
    explosion("explosion_9", 1, 2),
    explosion("explosion_10", 2, 2),
    explosion("explosion_11", 3, 2),

    explosion("explosion_12", 0, 3),
    explosion("explosion_13", 1, 3),
    explosion("explosion_14", 2, 3),
    explosion("explosion_15", 3, 3)
}
