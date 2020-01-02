# copyright 2020 EtlamGit

import os
import os.path
import argparse
from PIL import Image

from list_painting   import *
from list_effect     import *
from list_particle   import *
from list_explosion  import *
from list_sweep      import *

from chest           import transform_chest, transform_doublechest


def process(input_root, output_root, input_file, output_list):
    if os.path.exists(input_root + input_file):
        image = Image.open(input_root + input_file)

        if not os.path.exists(output_root):
            os.makedirs(output_root)

        for output_file in output_list:
            output_file.process(output_root, image)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_root_path")
    parser.add_argument("output_root_path", nargs='?')
    args = parser.parse_args()
    if not args.output_root_path:
        args.output_root_path = args.input_root_path

    # ensure trailing slash
    if (args.input_root_path[-1] != '/'):
        args.input_root_path += '/'
    if (args.output_root_path[-1] != '/'):
        args.output_root_path += '/'

    # slit large images
    process(args.input_root_path, args.output_root_path, painting_input,  painting_list)
    process(args.input_root_path, args.output_root_path, effect_input,    effect_list)
    process(args.input_root_path, args.output_root_path, particle_input,  particle_list)
    process(args.input_root_path, args.output_root_path, explosion_input, explosion_list)
    process(args.input_root_path, args.output_root_path, sweep_input,     sweep_list)

    # transform chests
    transform_chest(args.input_root_path, args.output_root_path, 'christmas.png')
    transform_chest(args.input_root_path, args.output_root_path, 'ender.png')
    transform_chest(args.input_root_path, args.output_root_path, 'normal.png')
    transform_chest(args.input_root_path, args.output_root_path, 'trapped.png')

    transform_doublechest(args.input_root_path, args.output_root_path, 'christmas_double.png')
    transform_doublechest(args.input_root_path, args.output_root_path, 'ender_double.png')
    transform_doublechest(args.input_root_path, args.output_root_path, 'normal_double.png')
    transform_doublechest(args.input_root_path, args.output_root_path, 'trapped_double.png')
