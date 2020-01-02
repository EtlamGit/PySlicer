# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from gridSprite import gridSprite


def painting(path, x, y, w, h):
    return gridSprite('assets/minecraft/textures/painting/' + path + ".png", x, y, w, h, 0, 0, 16, 16)


painting_input = 'assets/minecraft/textures/painting/paintings_kristoffer_zetterstrand.png'
painting_list = {
    painting("back",            15,  0, 1, 1),
    painting("kebab",            0,  0, 1, 1),
    painting("aztec",            1,  0, 1, 1),
    painting("alban",            2,  0, 1, 1),
    painting("aztec2",           3,  0, 1, 1),
    painting("bomb",             4,  0, 1, 1),
    painting("plant",            5,  0, 1, 1),
    painting("wasteland",        6,  0, 1, 1),
    painting("pool",             0,  2, 2, 1),
    painting("courbet",          2,  2, 2, 1),
    painting("sea",              4,  2, 2, 1),
    painting("sunset",           6,  2, 2, 1),
    painting("creebet",          8,  2, 2, 1),
    painting("wanderer",         0,  4, 1, 2),
    painting("graham",           1,  4, 1, 2),
    painting("match",            0,  8, 2, 2),
    painting("bust",             2,  8, 2, 2),
    painting("stage",            4,  8, 2, 2),
    painting("void",             6,  8, 2, 2),
    painting("skull_and_roses",  8,  8, 2, 2),
    painting("wither",          10,  8, 2, 2),
    painting("fighters",         0,  6, 4, 2),
    painting("pointer",          0, 12, 4, 4),
    painting("pigscene",         4, 12, 4, 4),
    painting("burning_skull",    8, 12, 4, 4),
    painting("skeleton",        12,  4, 4, 3),
    painting("donkey_kong",     12,  7, 4, 3)
}
