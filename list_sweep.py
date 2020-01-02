# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from OutputFile import OutputFile
from Box        import Box


def sweep(i, x, y):
    temp = OutputFile("assets/minecraft/textures/particle/sweep_" + str(i) + ".png", Box(32 * x, 16 * y, 32, 16, 128, 32))
    temp.apply('SQUARE')
    return temp


sweep_input = 'assets/minecraft/textures/entity/sweep.png'
sweep_list = {
    sweep(0, 0, 0),
    sweep(1, 1, 0),
    sweep(2, 2, 0),
    sweep(3, 3, 0),
    sweep(4, 0, 1),
    sweep(5, 1, 1),
    sweep(6, 2, 1),
    sweep(7, 3, 1)
}
