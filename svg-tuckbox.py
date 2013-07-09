#!/usr/bin/env python

# This program creates a tuckbox for a deck of playing cards.  The tuckbox file is
# an SVG file that is compatible with CorelDraw X5.  The file can then be imported
# into CorelDraw X5 and used as-is with a laser cutter.

# Note that CorelDraw's SVG import feature assumes a page size of 8.5 x 11.

# This program requires pysvg (http://codeboje.de/pysvg/)

# Copyright 2013, Timur Tabi
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
# This software is provided by the copyright holders and contributors "as is"
# and any express or implied warranties, including, but not limited to, the
# implied warranties of merchantability and fitness for a particular purpose
# are disclaimed. In no event shall the copyright holder or contributors be
# liable for any direct, indirect, incidental, special, exemplary, or
# consequential damages (including, but not limited to, procurement of
# substitute goods or services; loss of use, data, or profits; or business
# interruption) however caused and on any theory of liability, whether in
# contract, strict liability, or tort (including negligence or otherwise)
# arising in any way out of the use of this software, even if advised of
# the possibility of such damage.

import sys
import os
import pysvg.builders
import pysvg.structure
import pysvg.style
import pysvg.shape

# The default CorelDraw page width and height
WIDTH = 8.5
HEIGHT = 11

# How CorelDraw defines a Hairline width
HAIRLINE = 0.003

def line(x1, y1, x2, y2, strokewidth = HAIRLINE, stroke = 'red'):
    # Creates a line
    # @type x1: string or int
    # @param x1: starting x-coordinate
    # @type y1: string or int
    # @param y1: starting y-coordinate
    # @type x2: string or int
    # @param x2: ending x-coordinate
    # @type y2: string or int
    # @param y2: ending y-coordinate
    # @type strokewidth: string or int
    # @param strokewidth: width of the pen used to draw
    # @type stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    # @param stroke: color with which to draw the outer limits
    # @return: a line object
    style_dict = {'stroke-width':strokewidth, 'stroke':stroke}
    myStyle = pysvg.builders.StyleBuilder(style_dict)
    l = pysvg.shape.line(x1, y1, x2, y2)
    l.set_style(myStyle.getStyle())
    return l

def draw_line(coords):
    global svg

    l = line(coords[0], coords[1], coords[2], coords[3])
    svg.addElement(l)

svg = pysvg.structure.svg(width='%sin' % WIDTH, height='%sin' % HEIGHT)
svg.set_viewBox('0 0 %s %s' % (WIDTH, HEIGHT))

svg.addElement(line(1, 1, 1, 2))
svg.addElement(line(1, 2, 2, 2))
svg.addElement(line(2, 2, 2, 1))
svg.addElement(line(2, 1, 1, 1))
svg.save('/Users/timur/Documents/LaserCutter/line.svg')