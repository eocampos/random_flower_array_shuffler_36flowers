# -*- coding: utf-8 -*-
"""
Created on Mon Jul 7th 2014 18:07:03

@author: EOCampos (Eric Octavio Campos)
"""

# Written for Python 2.7
import random

ArrayFlowers01 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers02 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers03 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers04 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers05 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers06 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers07 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers08 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers09 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]
ArrayFlowers10 = ["zero_1", "zero_2", "zero_3", "zero_4", "zero_5", "zero_6", "neg1_1", "neg1_2", "neg1_3", "neg1_4", "neg1_5", "neg1_6", "neg2_1", "neg2_2", "neg2_3", "neg2_4", "neg2_5", "neg2_6", "neg3_1", "neg3_2", "neg3_3", "neg3_4", "neg3_5", "neg3_6", "neg4_1", "neg4_2", "neg4_3", "neg4_4", "neg4_5", "neg4_6", "-inf_1", "-inf_2", "-inf_3", "-inf_4", "-inf_5", "-inf_6"]

random.shuffle(ArrayFlowers01)
random.shuffle(ArrayFlowers02)
random.shuffle(ArrayFlowers03)
random.shuffle(ArrayFlowers04)
random.shuffle(ArrayFlowers05)
random.shuffle(ArrayFlowers06)
random.shuffle(ArrayFlowers07)
random.shuffle(ArrayFlowers08)
random.shuffle(ArrayFlowers09)
random.shuffle(ArrayFlowers10)

print
print "A1"
for shape in ArrayFlowers01:
    if ArrayFlowers01.index(shape) + 1 < 10:
        print "", ArrayFlowers01.index(shape) + 1, shape
    else:
        print ArrayFlowers01.index(shape) + 1, shape

print
print "A2"
for shape in ArrayFlowers02:
    if ArrayFlowers02.index(shape) + 1 < 10:
        print "", ArrayFlowers02.index(shape) + 1, shape
    else:
        print ArrayFlowers02.index(shape) + 1, shape
        
print
print "A3"
for shape in ArrayFlowers03:
    if ArrayFlowers03.index(shape) + 1 < 10:
        print "", ArrayFlowers03.index(shape) + 1, shape
    else:
        print ArrayFlowers03.index(shape) + 1, shape
        
print
print "A4"
for shape in ArrayFlowers04:
    if ArrayFlowers04.index(shape) + 1 < 10:
        print "", ArrayFlowers04.index(shape) + 1, shape
    else:
        print ArrayFlowers04.index(shape) + 1, shape
        
print
print "A5"
for shape in ArrayFlowers05:
    if ArrayFlowers05.index(shape) + 1 < 10:
        print "", ArrayFlowers05.index(shape) + 1, shape
    else:
        print ArrayFlowers05.index(shape) + 1, shape
        
print
print "A6"
for shape in ArrayFlowers06:
    if ArrayFlowers06.index(shape) + 1 < 10:
        print "", ArrayFlowers06.index(shape) + 1, shape
    else:
        print ArrayFlowers06.index(shape) + 1, shape
        
print
print "A7"
for shape in ArrayFlowers07:
    if ArrayFlowers07.index(shape) + 1 < 10:
        print "", ArrayFlowers07.index(shape) + 1, shape
    else:
        print ArrayFlowers07.index(shape) + 1, shape
        
print
print "A8"
for shape in ArrayFlowers08:
    if ArrayFlowers08.index(shape) + 1 < 10:
        print "", ArrayFlowers08.index(shape) + 1, shape
    else:
        print ArrayFlowers08.index(shape) + 1, shape
        
print
print "A9"
for shape in ArrayFlowers09:
    if ArrayFlowers09.index(shape) + 1 < 10:
        print "", ArrayFlowers09.index(shape) + 1, shape
    else:
        print ArrayFlowers09.index(shape) + 1, shape
        
print
print "A10"
for shape in ArrayFlowers10:
    if ArrayFlowers10.index(shape) + 1 < 10:
        print "", ArrayFlowers10.index(shape) + 1, shape
    else:
        print ArrayFlowers10.index(shape) + 1, shape
# end of script