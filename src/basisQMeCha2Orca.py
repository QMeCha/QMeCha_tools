#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import math
import time

atomsDataBase = [
['H','Hydrogen'],
['He','Helium'],
['Li','Lithium'],
['Be','Beryllium'],
['B','Boron'],
['C','Carbon'],
['N','Nitrogen'],
['O','Oxygen'],
['F','Fluorine'],
['Ne','Neon'],
['Na','Sodium'],
['Mg','Magnesium'],
['Al','Aluminum'],
['Si','Silicon'],
['P','Phosphorus'],
['S','Sulfur'],
['Cl','Chlorine'],
['Ar','Argon'],
['K','Potassium'],
['Ca','Calcium'],
['Sc','Scandium'],
['Ti','Titanium'],
['V','Vanadium'],
['Cr','Chromium'],
['Mn','Manganese'],
['Fe','Iron'],
['Co','Cobalt'],
['Ni','Nickel'],
['Cu','Copper'],
['Zn','Zinc'],
['Ga','Gallium'],
['Ge','Germanium'],
['As','Arsenic'],
['Se','Selenium'],
['Br','Bromine'],
['Kr','Krypton'],
['Rb','Rubidium'],
['Sr','Strontium'],
['Y','Yttrium'],
['Zr','Zirconium'],
['Nb','Niobium'],
['Mo','Molybdenum'],
['Tc','Technetium'],
['Ru','Ruthenium'],
['Rh','Rhodium'],
['Pd','Palladium'],
['Ag','Silver'],
['Cd','Cadmium'],
['In','Indium'],
['Sn','Tin'],
['Sb','Antimony'],
['Te','Tellurium'],
['I','Iodine'],
['Xe','Xenon'],
['Cs','Cesium'],
['Ba','Barium'],
['La','Lanthanum'],
['Ce','Cerium'],
['Pr','Praseodymium'],
['Nd','Neodymium'],
['Pm','Promethium'],
['Sm','Samarium'],
['Eu','Europium'],
['Gd','Gadolinium'],
['Tb','Terbium'],
['Dy','Dysprosium'],
['Ho','Holmium'],
['Er','Erbium'],
['Tm','Thulium'],
['Yb','Ytterbium'],
['Lu','Lutetium'],
['Hf','Hafnium'],
['Ta','Tantalum'],
['W','Tungsten'],
['Re','Rhenium'],
['Os','Osmium'],
['Ir','Iridium'],
['Pt','Platinum'],
['Au','Gold'],
['Hg','Mercury'],
['Tl','Thallium'],
['Pb','Lead'],
['Bi','Bismuth'],
['Po','Polonium'],
['At','Astatine'],
['Rn','Radon'],
['Fr','Francium'],
['Ra','Radium'],
['Ac','Actinium'],
['Th','Thorium'],
['Pa','Protactinium'],
['U','Uranium'],
['Np','Neptunium'],
['Pu','Plutonium'],
['Am','Americium'],
['Cm','Curium'],
['Bk','Berkelium'],
['Cf','Californium'],
['Es','Einsteinium'],
['Fm','Fermium'],
['Md','Mendelevium'],
['No','Nobelium'],
['Lr','Lawrencium'],
['Rf','Rutherfordium'],
['Db','Dubnium'],
['Sg','Seaborgium'],
['Bh','Bohrium'],
['Hs','Hassium'],
['Mt','Meitnerium'],
['Ds','Darmstadtium'],
['Rg','Roentgenium'],
['Cn','Copernicium'],
['Nh','Nihonium'],
['Fl','Flerovium'],
['Mc','Moscovium'],
['Lv','Livermorium'],
['Ts','Tennessine'],
['Og','Oganesson']]

try:
    basFileName = sys.argv[1]
    basFile = open(basFileName, "r" )
    basFileLines = basFile.readlines()
except:
    print(" Couldn't open file QMeCha basis set file")
    exit()

num_contr=[]
ang_contr=[]
orbs = []


for basFileLines[0].split()[0] in atomsDataBase[:][0] :
    for i in range(len(atomsDataBase)) :
        if ( atomsDataBase[i][0] == basFileLines[0].split()[0]) :
            atm_name=atomsDataBase[i][1].upper()

for line in range(1,len(basFileLines)) :
    if ( len(basFileLines[line].split())<1 ) : break
                
    if ( basFileLines[line].split()[0] in ['s','S'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[0],basFileLines[line+i+1].split()[1]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['p','P'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[0],basFileLines[line+i+1].split()[1]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['d','D'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[0],basFileLines[line+i+1].split()[1]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['f','F'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[0],basFileLines[line+i+1].split()[1]])
        orbs.append(orb)
    if ( basFileLines[line].split()[0] in ['g','G'] ) :
        ang_contr.append(str(basFileLines[line].split()[0]).upper())
        num_contr.append(int(basFileLines[line].split()[1]))
        orb = []
        for i in range(int(basFileLines[line].split()[1])) :
            orb.append([basFileLines[line+i+1].split()[0],basFileLines[line+i+1].split()[1]])
        orbs.append(orb)

num_orbs = len(ang_contr)
print(atm_name)
for i in range(num_orbs) :
    print(" %1s %3d" % (ang_contr[i],int(num_contr[i])))
    for j in range(int(num_contr[i])) :
        print(" %3d %15.7F %10.7F" % (j+1,float(orbs[i][j][0]),float(orbs[i][j][1])))
