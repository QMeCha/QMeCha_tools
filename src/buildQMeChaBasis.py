#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np

# Set tools dir
def setToolsDir():
    global qmecha_dir
    qmecha_dir=str(os.path.dirname(os.path.abspath(__file__)))+"/../"
    os.putenv("QMECHA_TOOLS", qmecha_dir)

# Check tools directory Print input parameters
def checkToolsDir():
    global qmecha_dir
    try:
        qmecha_dir=os.environ['QMECHA_TOOLS']
    except:
        print(" $QMECHA_TOOLS environment variable not set")
        print(" run:")
        print("  setenv QMECHA_TOOLS=../QMeCha_tools")
        print(" or")
        print("  export QMECHA_TOOLS=../QMeCha_tools")
        exit()

# load Default variables
def loadDefaultVariables():
    global n_at 
    global atom_names 
    global atomsDataBase,xyzFileName
    global one_body_type, two_body_type, cusps_order
    global inputParamsFile, wavefunction
    global printInputParFlag
    n_at = int(0)
    one_body_type = int(1)
    two_body_type = int(2)
    cusps_order = int(5)
    n_at = int(0)
    atom_names = []
    inputParamsFile = 'empty'
    xyzFileName = "empty"
    wavefunction = str('rsd')
    printInputParFlag = False
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

# Print Help info 
def printHelp():
    print()
    print(" Required input arguments:")
    print()
    print("   -xyz    Molecular *.xyz file")
    print()
    print(" Optional inputs:")
    print()
    print("   -wf      Wave_function [rsd,usd,rsg,usg,...]")
    print("   -oneb    One-Body type [1,2,3] [Default 1]")
    print("   -twob    Two-Body type [1,2,3] [Default 2]")
    print("   -CspO    Number of gassians in cusp [Default 5]")
    print("   -ipar    Basis set parameters [otherwise defaults] ")
    print("   -prnt    (To print basis set defaults in default.inp)")
    print()

# Print input parameters
def printInputParameters():
    print()
    print(" Required input arguments:")
    print()
    print(" XYZFile = ",xyzFileName)
    print()
    print(" Optional inputs:")
    print()
    print(" wf      = ",wavefunction)
    print(" oneb    = ",one_body_type)
    print(" twob    = ",two_body_type)
    print(" CspO    = ",cusps_order)
    print(" ipar    = ",inputParamsFile)
    print()

def readArguments():
    global wavefunction
    global xyzFileName
    global one_body_type
    global two_body_type
    global inputParamsFile
    global cusps_order
    global printInputParFlag
    for i in range(1,len(sys.argv)) :
        if ( sys.argv[i] == '-oneb'):
            one_body_type = int(sys.argv[i+1])
        if ( sys.argv[i] == '-twob'):
            two_body_type = int(sys.argv[i+1])
        if ( sys.argv[i] == '-CspO'):
            cusps_order=int(sys.argv[i+1])
        if ( sys.argv[i] == '-xyz'):
            xyzFileName = str(sys.argv[i+1])
        if ( sys.argv[i] == '-wf'):
            wavefunction = str(sys.argv[i+1])
        if ( sys.argv[i] == '-ipar'):
            inputParamsFile = str(sys.argv[i+1])
        if ( sys.argv[i] == '-prnt'):
            printInputParFlag = True

# Read QMeChq XYZ file
def readMolFile():
    global atom_names, n_at, n_pseudo
    try:
        molFile = open(xyzFileName, "r" )
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
        #Remove non pseudo atoms.
        atom_names =[ atom for atom in atom_names if '*' in atom ]

        for line_num in range(len(atom_names)) :
            atom_names[line_num]=atom_names[line_num].replace('*', '')

        n_pseudo = len(atom_names)
        molFile.close()
    except:
        print(" Couldn't open file molecular QMeCha file")
        printHelp()
        exit()

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

# Print basis set parameters 
def printBasisSetParametersInfo(FileName):
    basFile = open(FileName, "w" )
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
    bssOutFile.write(" {} \n".format(wavefunction))
    bssOutFile.write("# One body \n")
    bssOutFile.write("  {}  {} \n".format(one_body_type,cusps_order))
    bssOutFile.write("# Two body \n")
    bssOutFile.write("  {}  {} \n".format(two_body_type,cusps_order))
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

if __name__ == "__main__":
    print(" =======================================================================")
    print(" ==================== Basis set generator for QMeCha ===================")
    print(" =======================================================================")
    loadDefaultVariables()
    setToolsDir()
    if (len(sys.argv) == 1 ) :
        printHelp()
        exit()
    else:
        readArguments()
    if (printInputParFlag): 
        printBasisSetParametersInfo("param.inp")
        print(" Printing default parameter file param.inp")
        print(" =======================================================================")
        exit()
    if ( xyzFileName == 'empty') :
        print(" Missing molecular QMeCha file in input")
        printHelp()
    printInputParameters()

    print(" =======================================================================")
