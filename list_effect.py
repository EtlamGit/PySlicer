# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from gridSprite import gridSprite


def effect(path, x, y):
    return gridSprite("assets/minecraft/textures/mob_effect/" + path + ".png", x, y, 1, 1, 0, 198, 18, 18)


effect_input = 'assets/minecraft/textures/gui/container/inventory.png'
effect_list = {
    effect("speed",             0, 0),
    effect("slowness",          1, 0),
    effect("haste",             2, 0),
    effect("mining_fatigue",    3, 0),
    effect("strength",          4, 0),
    effect("jump_boost",        2, 1),
    effect("nausea",            3, 1),
    effect("regeneration",      7, 0),
    effect("resistance",        6, 1),
    effect("fire_resistance",   7, 1),
    effect("water_breathing",   0, 2),
    effect("invisibility",      0, 1),
    effect("blindness",         5, 1),
    effect("night_vision",      4, 1),
    effect("hunger",            1, 1),
    effect("weakness",          5, 0),
    effect("poison",            6, 0),
    effect("wither",            1, 2),
    effect("health_boost",      7, 2),
    effect("absorption",        2, 2),
    effect("glowing",           4, 2),
    effect("levitation",        3, 2),
    effect("luck",              5, 2),
    effect("unluck",            6, 2),
    effect("slow_falling",      8, 0),
    effect("conduit_power",     9, 0),
    effect("dolphins_grace",   10, 0)
}
