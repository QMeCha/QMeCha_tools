#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np
import math
import time

global n_at 
global atom_names 
global atomsDataBase

atomsDataBase = [
['Hydrogen','H','cc-pVDZ','ccECP','3s2p1d','G'],
['Helium','He','cc-pVDZ','ccECP','3s2p1d','G'],
['Lithium','Li','cc-pVDZ','ccECP','3s2p1d','G'],
['Beryllium','Be','cc-pVDZ','ccECP','3s2p1d','G'],
['Boron','B','cc-pVDZ','ccECP','3s2p1d','G'],
['Carbon','C','cc-pVDZ','ccECP','3s2p1d','G'],
['Nitrogen','N','cc-pVDZ','ccECP','3s2p1d','G'],
['Oxygen','O','cc-pVDZ','ccECP','3s2p1d','G'],
['Fluorine','F','cc-pVDZ','ccECP','3s2p1d','G'],
['Neon','Ne','cc-pVDZ','ccECP','3s2p1d','G'],
['Sodium','Na','cc-pVDZ','ccECP','3s2p1d','G'],
['Magnesium','Mg','cc-pVDZ','ccECP','3s2p1d','G'],
['Aluminum','Al','cc-pVDZ','ccECP','3s2p1d','G'],
['Silicon','Si','cc-pVDZ','ccECP','3s2p1d','G'],
['Phosphorous','P','cc-pVDZ','ccECP','3s2p1d','G'],
['Sulfur','S','cc-pVDZ','ccECP','3s2p1d','G'],
['Chlorine','Cl','cc-pVDZ','ccECP','3s2p1d','G'],
['Argon','Ar','cc-pVDZ','ccECP','3s2p1d','G'],
['Potassium','K','cc-pVDZ','ccECP','3s2p1d','G'],
['Calcium','Ca','cc-pVDZ','ccECP','3s2p1d','G'],
['Scandium','Sc','cc-pVDZ','ccECP','3s2p1d','G'],
['Titanium','Ti','cc-pVDZ','ccECP','3s2p1d','G'],
['Vanadium','V','cc-pVDZ','ccECP','3s2p1d','G'],
['Chromium','Cr','cc-pVDZ','ccECP','3s2p1d','G'],
['Manganese','Mn','cc-pVDZ','ccECP','3s2p1d','G'],
['Iron','Fe','cc-pVDZ','ccECP','3s2p1d','G'],
['Cobalt','Co','cc-pVDZ','ccECP','3s2p1d','G'],
['Nickel','Ni','cc-pVDZ','ccECP','3s2p1d','G'],
['Copper','Cu','cc-pVDZ','ccECP','3s2p1d','G'],
['Zinc','Zn','cc-pVDZ','ccECP','3s2p1d','G'],
['Gallium','Ga','cc-pVDZ','ccECP','3s2p1d','G'],
['Germanium','Ge','cc-pVDZ','ccECP','3s2p1d','G'],
['Arsenic','As','cc-pVDZ','ccECP','3s2p1d','G'],
['Selenium','Se','cc-pVDZ','ccECP','3s2p1d','G'],
['Bromine','Br','cc-pVDZ','ccECP','3s2p1d','G'],
['Krypton','Kr','cc-pVDZ','ccECP','3s2p1d','G'],
['Rubidium','Rb','cc-pVDZ','ccECP','3s2p1d','G'],
['Strontium','Sr','cc-pVDZ','ccECP','3s2p1d','G'],
['Yttrium','Y','cc-pVDZ','ccECP','3s2p1d','G'],
['Zirconium','Zr','cc-pVDZ','ccECP','3s2p1d','G'],
['Niobium','Nb','cc-pVDZ','ccECP','3s2p1d','G'],
['Molybdenum','Mo','cc-pVDZ','ccECP','3s2p1d','G'],
['Technetium','Tc','cc-pVDZ','ccECP','3s2p1d','G'],
['Ruthenium','Ru','cc-pVDZ','ccECP','3s2p1d','G'],
['Rhodium','Rh','cc-pVDZ','ccECP','3s2p1d','G'],
['Palladium','Pd','cc-pVDZ','ccECP','3s2p1d','G'],
['Silver','Ag','cc-pVDZ','ccECP','3s2p1d','G'],
['Cadmium','Cd','cc-pVDZ','ccECP','3s2p1d','G'],
['Indium','In','cc-pVDZ','ccECP','3s2p1d','G'],
['Tin','Sn','cc-pVDZ','ccECP','3s2p1d','G'],
['Antimony','Sb','cc-pVDZ','ccECP','3s2p1d','G'],
['Tellurium','Te','cc-pVDZ','ccECP','3s2p1d','G'],
['Iodine','I','cc-pVDZ','ccECP','3s2p1d','G'],
['Xenon','Xe','cc-pVDZ','ccECP','3s2p1d','G'],
['Cesium','Cs','cc-pVDZ','ccECP','3s2p1d','G']
]


def readQMeCHaMolFile(molFileName : str,atom_names : list,n_at : int ):
    molFile = open(molFileName, "r" )
    molFileLines = molFile.readlines()
    for line_num in range(len(molFileLines)) :
        if ("n_at" in molFileLines[line_num]) :
            try:
                n_at = int(molFileLines[line_num].split()[2])
            except:
                n_at = 0
        if ("/" in molFileLines[line_num]) :
            read_from = line_num + 1
            break
    for line_num in range(read_from,read_from+n_at) :
        atom_names.append(molFileLines[line_num].split()[0])
    atom_names = list( dict.fromkeys(atom_names) )

    for line_num in range(len(atom_names)) :
        atom_names[line_num]=atom_names[line_num].replace('*', '')
    molFile.close()
    return atom_names, n_at

def printccECPBasisset(atom,basistype,eletype,outFile,n_jorbs):
    bssFile =open(qmecha_dir+'/basissets/pseudo/'+atom+'.ccECP_'+basistype+'.qmecha', 'r')
    bssFileLines=bssFile.readlines()
    outFile.write("# Basis set "+basistype+" "+eletype+"\n")
    if (eletype == 'AE') :
        outFile.write( bssFileLines[0].split()[0]+" "+bssFileLines[0].split()[1]+" "+str(n_jorbs)+"\n" ) 
    else:
        outFile.write( '*'+bssFileLines[0].split()[0]+" "+bssFileLines[0].split()[1]+" "+str(n_jorbs)+"\n" ) 

    for line in range(1,len(bssFileLines)) :
        outFile.write(str(bssFileLines[line]))
    bssFile.close()

def countJastrowOrbitals(jorbs):
    return int(len(jorbs)/2)

def readBasisInfo(basFileName,atomsDataBase):
    basFile = open(basFileName, "r" )
    basFileLines = basFile.readlines()
    for line in basFileLines :
        if (len(line.split()) <=4 ) :
            break
        for i in atomsDataBase :
            if ( i[1] == line.split()[0] ) :
                i[2] = line.split()[1]
                i[3] = line.split()[2]
                i[4] = line.split()[3]
                i[5] = line.split()[4]
                break
    basFile.close()
    return atomsDataBase

def printBasisInfo(basFileName):
    basFile = open(basFileName, "w" )
    for i in atomsDataBase :
        basFile.write(i[1]+" "+i[2]+" "+i[3]+" "+i[4]+" "+i[5]+"\n")
    basFile.close()

def printJastrow(chrg,jorbs,jtype,outFile):
    outFile.write("# Jastrow basis set \n")
    # Count primitive orbital types
    n_s = 0
    n_p = 0
    n_d = 0
    n_f = 0
    n_g = 0
    for k1 in range(0,len(jorbs),2) :
        if (jorbs[k1+1].upper()=='S' ) :
            n_s = n_s + int(jorbs[k1])
        if (jorbs[k1+1].upper()=='P' ) :
            n_p = n_p + int(jorbs[k1])
        if (jorbs[k1+1].upper()=='D' ) :
            n_d = n_d + int(jorbs[k1])
        if (jorbs[k1+1].upper()=='F' ) :
            n_f = n_f + int(jorbs[k1])
        if (jorbs[k1+1].upper()=='G' ) :
            n_g = n_g + int(jorbs[k1])

    # generate exponentials
    z_s = []
    z_p = []
    z_d = []
    z_f = []
    z_g = []
    if ( n_s > 0) :
        for k1 in range(n_s) :
            z_s.append(0.1+(1.0/np.sqrt(float(n_s)))*float(n_s-k1-1)**(1.7))
    if ( n_p > 0) :
        for k1 in range(n_p) :
            z_p.append(0.25+(1.0/np.sqrt(float(n_p)))*float(n_p-k1-1)**(1.7))
    if ( n_d > 0) :
        for k1 in range(n_d) :
            z_d.append(0.5+(1.0/np.sqrt(float(n_d)))*float(n_d-k1-1)**(1.7))
    if ( n_f > 0) :
        for k1 in range(n_f) :
            z_f.append(0.75+(1.0/np.sqrt(float(n_f)))*float(n_f-k1-1)**(1.7))
    if ( n_g > 0) :
        for k1 in range(n_g) :
            z_g.append(1.0+(1.0/np.sqrt(float(n_g)))*float(n_g-k1-1)**(1.7))

    # Print file
    for k1 in range(0,len(jorbs),2) :
        n_orbs=int(jorbs[k1])
        l_orbs=jorbs[k1+1].upper()
        outFile.write(" "+l_orbs+str(" %3d" % (n_orbs))+"\n")
        if (l_orbs=='S' ) :
            for k2 in range(n_orbs) :
                c=1.000-float(n_orbs-k2-1)/float(n_orbs)
                line=str(" %15.7F %10.7F" % (float(z_s[0]),float(c)))
                outFile.write(line+" 1"+jtype+"\n")
                del z_s[0]
        if (l_orbs=='P' ) :
            for k2 in range(n_orbs) :
                c=1.000-float(n_orbs-k2-1)/float(n_orbs)
                line=str(" %15.7F %10.7F" % (float(z_p[0]),float(c)))
                outFile.write(line+" 1"+jtype+"\n")
                del z_p[0]
        if (l_orbs=='D' ) :
            for k2 in range(n_orbs) :
                c=1.000-float(n_orbs-k2-1)/float(n_orbs)
                line=str(" %15.7F %10.7F" % (float(z_d[0]),float(c)))
                outFile.write(line+" 1"+jtype+"\n")
                del z_d[0]
        if (l_orbs=='F' ) :
            for k2 in range(n_orbs) :
                c=1.000-float(n_orbs-k2-1)/float(n_orbs)
                line=str(" %15.7F %10.7F" % (float(z_f[0]),float(c)))
                outFile.write(line+" 1"+jtype+"\n")
                del z_f[0]
        if (l_orbs=='G' ) :
            for k2 in range(n_orbs) :
                c=1.000-float(n_orbs-k2-1)/float(n_orbs)
                line=str(" %15.7F %10.7F" % (float(z_g[0]),float(c)))
                outFile.write(line+" 1"+jtype+"\n")
                del z_g[0]

def printBasisFile(atom_names,atomsDataBase,bssOutFileName):
    bssOutFile = open( bssOutFileName, "w" )
    bssOutFile.write("# Wave function \n")
    bssOutFile.write(" "+str(wavefunction)+"\n")
    bssOutFile.write("# One body \n")
    bssOutFile.write("  1   5  \n")
    bssOutFile.write("# Two body \n")
    bssOutFile.write("  2   5  \n")
    basistype = ""
    eletype = ""
    jastroworbs = ""
    jastrowtype = ""
    n_jorbs = 0
    for i in atom_names :
        for j in range(len(atomsDataBase)) :
            if i == atomsDataBase[j][1] :
                basistype   = atomsDataBase[j][2]
                eletype     = atomsDataBase[j][3]
                jastroworbs = atomsDataBase[j][4]
                jastrowtype = atomsDataBase[j][5]
                break

        n_jorbs=countJastrowOrbitals(jastroworbs)
        printccECPBasisset(i,basistype,eletype,bssOutFile,n_jorbs)
        printJastrow(j+1,jastroworbs,jastrowtype,bssOutFile)
    bssOutFile.close()

print(" =======================================================================")
print(" ==================== Basis set generator for QMeCha ===================")
print(" =======================================================================")

n_at = 0
atom_names = []
molFileName = ''
basFileName = ''
wavefunction = ''
printbasisinfo = False
def printHeader():
    print(" Required inputs:")
    print(" -m molecular_QMeCha_file ")
    print(" Optional inputs:")
    print(" -w Wave_function [rsd,usd,rsg,usg,...] ")
    print(" -i Basis set input [otherwise defaults] ")
    print(" -p  (To print basis set defaults in default.inp) ")

try:
    qmecha_dir=os.environ['QMECHA_DIR']
except:
    print(" $QMECHA_DIR environment variable not set")
    print(" run:")
    print("  setenv QMECHA_DIR=../QMeCha_dev")
    print(" or")
    print("  export QMECHA_DIR=../QMeCha_dev")
    exit()

try:
    if (len(sys.argv) == 1 ) :
        printHeader()
        exit()
    for i in range(1,len(sys.argv)) :
        if ( sys.argv[i] == '-m'):
            molFileName = sys.argv[i+1]
        if ( sys.argv[i] == '-i'):
            inpFileName = sys.argv[i+1]
        if ( sys.argv[i] == '-w'):
            wavefunction = sys.argv[i+1]
        if ( sys.argv[i] == '-p'):
            printbasisinfo = True
except:
    #printHeader()
    exit()

if (printbasisinfo == True) :
    printBasisInfo("default.inp")
    exit()


if (molFileName == '') :
    print(" Missing molecular QMeCha file in input")
    exit()
else:
    basFileName = molFileName.removesuffix('.xyz')+'.bas'

try:
    atom_names, n_at = readQMeCHaMolFile(molFileName,atom_names,n_at)
except:
    print(" Couldn't open file molecular QMeCha file")
    printHeader()
    exit()
   
try:
    atomsDataBase = readBasisInfo(inpFileName,atomsDataBase)
except:
    print(" Couldn't read basis set info. Will use default settings for atoms")

if (wavefunction == '') :
    print(" Wave function type not defined setting to Default [rsg]")
    wavefunction = 'rsg'

try:
    printBasisFile(atom_names,atomsDataBase,basFileName)
except:
    print(" Error: Couldn't create basis set file")
    exit()
