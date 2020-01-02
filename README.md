# PySlicer
Resource pack migration tool for Minecraft Java Edition (from 1.14 to 1.15)

This tool is a Python implementation of the [official migration tool provided by Mojang](https://github.com/Mojang/slicer).

As I do not have a JRE nor working Internet connection at the moment, I translated the important stuff from Java code into Python. Now it is working with a simple Python installation and only requires the Pillow library for image handling.


# additional features (extending the original Mojang code)
Chests are also converted.

Textures for all Chests are rotated or flipped and position inside texture file has changed for some of them. Double Chests are now stored in separated Left and Right texture files.


# Usage

`python PySlicer.py <input_dir> [output_dir]`

output_dir is optional, if ommited output will be generated in-place. Attention, Chests can only be converted once when source is overwritten in-place.
