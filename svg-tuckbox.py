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
from optparse import OptionParser

# The default CorelDraw page width and height
WIDTH = 1000
HEIGHT = 1000

# How CorelDraw defines a Hairline width
HAIRLINE = 0.01

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

def circle(cx, cy, r, strokewidth = HAIRLINE, stroke='red', fill='none'):
    # Creates a circle
    # @type cx: string or int
    # @param cx: starting x-coordinate
    # @type cy: string or int
    # @param cy: starting y-coordinate
    # @type r: string or int
    # @param r: radius
    # @type strokewidth: string or int
    # @param strokewidth: width of the pen used to draw
    # @type stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    # @param stroke: color with which to draw the outer limits
    # @type fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    # @param fill: color with which to fill the element (default: no filling)
    # @return: a circle object
    style_dict = {'fill':fill, 'stroke-width':strokewidth, 'stroke':stroke}
    myStyle = pysvg.builders.StyleBuilder(style_dict)
    c = pysvg.shape.circle(cx, cy, r)
    c.set_style(myStyle.getStyle())

    return c

def arc(x1, y1, x2, y2, r, strokewidth = HAIRLINE, stroke = 'red', fill = 'none', sweep = 0):
    # Creates a circle
    # @type cx: string or int
    # @param cx: starting x-coordinate
    # @type cy: string or int
    # @param cy: starting y-coordinate
    # @type r: string or int
    # @param r: radius
    # @type strokewidth: string or int
    # @param strokewidth: width of the pen used to draw
    # @type stroke: string (either css constants like "black" or numerical values like "#FFFFFF")
    # @param stroke: color with which to draw the outer limits
    # @type fill: string (either css constants like "black" or numerical values like "#FFFFFF")
    # @param fill: color with which to fill the element (default: no filling)
    # @return: a circle object
    style_dict = {'fill':fill, 'stroke-width':strokewidth, 'stroke':stroke}
    myStyle = pysvg.builders.StyleBuilder(style_dict)
    p = pysvg.shape.path("M %s,%s" % (x1, y1))
    p.appendArcToPath((x2 - x1) / 2, r, x2, y2, sweep_flag = sweep, relative = False)
    p.set_style(myStyle.getStyle())

    return p

parser = OptionParser(usage="usage: %prog [options]")
parser.add_option("-H", dest="h", help="card height", type="float", default = 92.0)
parser.add_option("-W", dest="w", help="card width", type="float", default = 60.0)
parser.add_option("-T", dest="t", help="card thickness", type="float", default = 4.0)

(o, a) = parser.parse_args()

svg = pysvg.structure.svg(width='%smm' % WIDTH, height='%smm' % HEIGHT)
svg.set_viewBox('0 0 %s %s' % (WIDTH, HEIGHT))

# Left edge of flaps 1 and 4
svg.addElement(line(0, 0, 0, o.t * 0.9 + o.h))

# Bottom edge of flap 1
svg.addElement(line(0, 0, o.t, 0))

# Right edge of flap 1
svg.addElement(line(o.t, 0, o.t, o.t))

# Top edge of flap 4
svg.addElement(line(0, o.t + o.h, o.t, o.t + o.h))

# Bottom edge of flap 3
svg.addElement(line(o.t, o.t * 0.1, o.t + o.w, o.t * 0.1))

# Left edge of flap 2
svg.addElement(line(o.t + o.w, 0, o.t + o.w, o.t))

# Bottom edge of flap 2 and bottom flap of box front
svg.addElement(line(o.t + o.w, 0, o.t + o.w + o.t + o.w, 0))

# Right edge of flap 2
svg.addElement(line(o.t + o.w + o.t, 0,
    o.t + o.w + o.t, o.t))

# Right edge of bottom flap of box front
svg.addElement(line(o.t + o.w + o.t + o.w, 0,
    o.t + o.w + o.t + o.w, o.t))

# Bottom edge of right flap of box front
svg.addElement(line(o.t + o.w + o.t + o.w, o.t,
    o.t + o.w + o.t + o.w + o.t, o.t))

# Right edge of right flap of box front
svg.addElement(line(o.t + o.w + o.t + o.w + o.t, o.t,
    o.t + o.w + o.t + o.w + o.t, o.t + o.h + o.t * 0.5))

# Right flap of box front
svg.addElement(line(o.t + o.w + o.t + o.w + o.t, o.t + o.h + o.t * 0.5,
    o.t + o.w + o.t + o.w + 0.5 * o.t, o.t + o.h + o.t * 0.5))
svg.addElement(line(o.t + o.w + o.t + o.w + 0.5 * o.t, o.t + o.h + o.t * 0.5,
    o.t + o.w + o.t + o.w, o.t + o.h + o.t * 0.25))
svg.addElement(line(o.t + o.w + o.t + o.w, o.t + o.h + o.t * 0.25,
    o.t + o.w + o.t + o.w, o.t + o.h))

# Top of box front, with 15mm semi-circle inset
R = 7.5   # Radius
svg.addElement(line(o.t + o.w + o.t + o.w, o.t + o.h,
    o.t + o.w + o.t + o.w * 0.5 + R, o.t + o.h))
svg.addElement(line(o.t + o.w + o.t + o.w * 0.5 - R, o.t + o.h,
    o.t + o.w + o.t, o.t + o.h))
svg.addElement(arc(o.t + o.w + o.t + o.w * 0.5 - R, o.t + o.h,
    o.t + o.w + o.t + o.w * 0.5 + R, o.t + o.h, R, sweep = 1))

# Left flap of box front
svg.addElement(line(o.t + o.w + o.t, o.t + o.h,
    o.t + o.w + o.t, o.t + o.h + o.t * 0.25))
svg.addElement(line(o.t + o.w + o.t, o.t + o.h + o.t * 0.25,
    o.t + o.w + o.t * 0.5, o.t + o.h + o.t * 0.5))
svg.addElement(line(o.t + o.w + o.t * 0.5, o.t + o.h + o.t * 0.5,
    o.t + o.w, o.t + o.h + o.t * 0.5))

# Top flap
svg.addElement(line(o.t + o.w, o.t + o.h,
    o.t + o.w, o.t + o.h + o.t * 1.5))
svg.addElement(line(o.t, o.t + o.h, o.t, o.t + o.h + o.t * 1.5))
svg.addElement(arc(o.t, o.t + o.h + o.t * 1.5, o.t + o.w,
        o.t + o.h + o.t * 1.5, o.w * 0.25))

svg.save('/Users/timur/Documents/LaserCutter/line.svg')
