#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import math
import time

try:
    basFileName = sys.argv[1]
    basFile = open(basFileName, "r" )
    basFileLines = basFile.readlines()
except:
    print(" Couldn't open file GAMESS basis set file")
    exit()

try:
    atm_name = str(sys.argv[2])
except:
    print(" Missing name of the atom")
    exit()

num_contr=[]
ang_contr=[]
orbs = []
for line in range(len(basFileLines)) :
    if ( len(basFileLines[line].split())<1 ) : break
    if ( basFileLines[line].split()[0] in ['s','S'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[1],basFileLines[line+i+1].split()[2]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['p','P'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[1],basFileLines[line+i+1].split()[2]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['d','D'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[1],basFileLines[line+i+1].split()[2]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['f','F'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[1],basFileLines[line+i+1].split()[2]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['g','G'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[1],basFileLines[line+i+1].split()[2]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['h','H','i','I'] ) :
        pass

num_orbs = len(ang_contr)
print(atm_name,num_orbs,0)
for i in range(num_orbs) :
    print(" %1s %3d" % (ang_contr[i],int(num_contr[i])))
    for j in range(int(num_contr[i])) :
        print(" %15.7F %10.7F 1G" % (float(orbs[i][j][0]),float(orbs[i][j][1])))
