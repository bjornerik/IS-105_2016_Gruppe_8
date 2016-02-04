# -*- coding: utf-8 -*-
import sys
from sys import argv
from sys import path

def func1(name1, name2):
    return "hei," + name1 + " og " +name2
   
name1, name2 = argv[1], argv[2]
print func1(name1,name2)
