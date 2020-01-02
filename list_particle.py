# copyright 2019 Mojang (Microsoft Corporation), Python translation by EtlamGit

from OutputFile import OutputFile
from gridSprite import gridSprite
from Box        import b256


def particle(path, x, y, w=1, h=1, x_offset=0, y_offset=0):
    return gridSprite("assets/minecraft/textures/particle/" + path + ".png", x, y, w, h, x_offset, y_offset, 8, 8)


particle_input = 'assets/minecraft/textures/particle/particles.png'
particle_list = {
    particle("generic_0", 0, 0),
    particle("generic_1", 1, 0),
    particle("generic_2", 2, 0),
    particle("generic_3", 3, 0),
    particle("generic_4", 4, 0),
    particle("generic_5", 5, 0),
    particle("generic_6", 6, 0),
    particle("generic_7", 7, 0),

    particle("splash_0", 3, 1),
    particle("splash_1", 4, 1),
    particle("splash_2", 5, 1),
    particle("splash_3", 6, 1),

    particle("sga_a", 1, 14),
    particle("sga_b", 2, 14),
    particle("sga_c", 3, 14),
    particle("sga_d", 4, 14),
    particle("sga_e", 5, 14),
    particle("sga_f", 6, 14),
    particle("sga_g", 7, 14),
    particle("sga_h", 8, 14),
    particle("sga_i", 9, 14),
    particle("sga_j", 10, 14),
    particle("sga_k", 11, 14),
    particle("sga_l", 12, 14),
    particle("sga_m", 13, 14),
    particle("sga_n", 14, 14),
    particle("sga_o", 15, 14),
    particle("sga_p", 0, 15),
    particle("sga_q", 1, 15),
    particle("sga_r", 2, 15),
    particle("sga_s", 3, 15),
    particle("sga_t", 4, 15),
    particle("sga_u", 5, 15),
    particle("sga_v", 6, 15),
    particle("sga_w", 7, 15),
    particle("sga_x", 8, 15),
    particle("sga_y", 9, 15),
    particle("sga_z", 10, 15),

    particle("effect_0", 0, 8),
    particle("effect_1", 1, 8),
    particle("effect_2", 2, 8),
    particle("effect_3", 3, 8),
    particle("effect_4", 4, 8),
    particle("effect_5", 5, 8),
    particle("effect_6", 6, 8),
    particle("effect_7", 7, 8),

    particle("glitter_0", 0, 11),
    particle("glitter_1", 1, 11),
    particle("glitter_2", 2, 11),
    particle("glitter_3", 3, 11),
    particle("glitter_4", 4, 11),
    particle("glitter_5", 5, 11),
    particle("glitter_6", 6, 11),
    particle("glitter_7", 7, 11),

    particle("spark_0", 0, 10),
    particle("spark_1", 1, 10),
    particle("spark_2", 2, 10),
    particle("spark_3", 3, 10),
    particle("spark_4", 4, 10),
    particle("spark_5", 5, 10),
    particle("spark_6", 6, 10),
    particle("spark_7", 7, 10),

    particle("spell_0", 0, 9),
    particle("spell_1", 1, 9),
    particle("spell_2", 2, 9),
    particle("spell_3", 3, 9),
    particle("spell_4", 4, 9),
    particle("spell_5", 5, 9),
    particle("spell_6", 6, 9),
    particle("spell_7", 7, 9),

    particle("bubble_pop_0", 0 * 2, 16, 2, 2, 0, 3),    # attention order of arguments changed!
    particle("bubble_pop_1", 1 * 2, 16, 2, 2, 0, 3),    # attention order of arguments changed!
    particle("bubble_pop_2", 2 * 2, 16, 2, 2, 0, 3),    # attention order of arguments changed!
    particle("bubble_pop_3", 3 * 2, 16, 2, 2, 0, 3),    # attention order of arguments changed!
    particle("bubble_pop_4", 4 * 2, 16, 2, 2, 0, 3),    # attention order of arguments changed!

    particle("flash", 4, 2, 4, 4),
    particle("nautilus", 0, 13),
    particle("note", 0, 4),
    particle("angry", 1, 5),
    particle("bubble", 0, 2),
    particle("damage", 3, 4),
    particle("flame", 0, 3),
    particle("lava", 1, 3),
    particle("heart", 0, 5),
    particle("glint", 2, 5),
    particle("enchanted_hit", 2, 4),
    particle("critical_hit", 1, 4),
    particle("drip_hang", 0, 7),
    particle("drip_fall", 1, 7),
    particle("drip_land", 2, 7),

    OutputFile("assets/minecraft/textures/entity/fishing_hook.png", b256(8 * 1, 8 * 2, 8, 8))
}
