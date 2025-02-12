#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import math
import time



name_jastFile2b  = sys.argv[1]
name_jastFileIn  = sys.argv[2]
name_jastFileOut = sys.argv[3]


def readJastFact(namejastFile: str, oneBodyCusp = None, twoBodyCusp = None, oneBodyDyn = None, twoBodyDyn = None):
    jastFileIn = open(namejastFile, "r" )
    jastFileInLines = jastFileIn.readlines()
    jastFileIn.close()
    # One body Cusp
    if type(oneBodyCusp) == list:
        for line_num in range(len(jastFileInLines)) :
            if ("# One body Cusp parameters" in jastFileInLines[line_num]) :
                break
        oneBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        oneBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        cmp_num   = int(jastFileInLines[line_num].split()[2])
        if (cmp_num > 0):
            for i in range(3*cmp_num):
                line_num = line_num + 1
                oneBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        oneBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        cmp_num   = int(jastFileInLines[line_num].split()[2])
        if (cmp_num > 0):
            for i in range(3*cmp_num):
                line_num = line_num + 1
                oneBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))

    # Two body Cusp
    if type(twoBodyCusp) == list:
        for line_num in range(len(jastFileInLines)) :
            if ("# Two body Cusp parameters" in jastFileInLines[line_num]) :
                break
        twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        cmp_num   = int(jastFileInLines[line_num].split()[2])
        if (cmp_num > 0):
            for i in range(3*cmp_num):
                line_num = line_num + 1
                twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        cmp_num   = int(jastFileInLines[line_num].split()[2])
        if (cmp_num > 0):
            for i in range(3*cmp_num):
                line_num = line_num + 1
                twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))
        cmp_num   = int(jastFileInLines[line_num].split()[2])
        if (cmp_num > 0):
            for i in range(3*cmp_num):
                line_num = line_num + 1
                twoBodyCusp.append(jastFileInLines[line_num].replace("\n", ""))

    # One body Dynamical
    if type(oneBodyDyn) == list:
        for line_num in range(len(jastFileInLines)) :
            if ("# Coefficients of the 1Body linear Jastrow" in jastFileInLines[line_num]) :
                break
        oneBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        cmp_num   = int(jastFileInLines[line_num].split()[0])
        oneBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))
        if (cmp_num > 0):
            for i in range(cmp_num):
                line_num = line_num + 1
                oneBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))

    # Two body Dynamical
    if type(twoBodyDyn) == list:
        for line_num in range(len(jastFileInLines)) :
            if ("# Coefficients of the 2Body linear Jastrow" in jastFileInLines[line_num]) :
                break
        twoBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))
        line_num = line_num + 1
        cmp_num   = int(jastFileInLines[line_num].split()[0])
        twoBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))
        if (cmp_num > 0):
            for i in range(cmp_num):
                line_num = line_num + 1
                twoBodyDyn.append(jastFileInLines[line_num].replace("\n", ""))

def writeJastFact(namejastFile: str, oneBodyCusp: list, twoBodyCusp: list, oneBodyDyn: list, twoBodyDyn: list):
    jastFilewr = open(namejastFile, "w" )
    # One body Cusp
    for line_num in range(len(oneBodyCusp)) :
        jastFilewr.write(str(oneBodyCusp[line_num])+'\n')

    # Two body Cusp
    for line_num in range(len(twoBodyCusp)) :
        jastFilewr.write(str(twoBodyCusp[line_num])+'\n')

    # One body Dyn
    for line_num in range(len(oneBodyDyn)) :
        jastFilewr.write(str(oneBodyDyn[line_num])+'\n')

    # Two body Dyn
    for line_num in range(len(twoBodyDyn)) :
        jastFilewr.write(str(twoBodyDyn[line_num])+'\n')

    jastFilewr.close()

oneBodyCuspIn = []
twoBodyCuspIn = []
oneBodyDynIn = []
twoBodyDynIn = []

readJastFact(name_jastFile2b,twoBodyCusp=twoBodyCuspIn)

readJastFact(name_jastFileIn,oneBodyCusp=oneBodyCuspIn, oneBodyDyn=oneBodyDynIn, twoBodyDyn=twoBodyDynIn)

writeJastFact(name_jastFileOut,oneBodyCuspIn, twoBodyCuspIn, oneBodyDynIn, twoBodyDynIn)
