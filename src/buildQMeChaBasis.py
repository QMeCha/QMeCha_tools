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
    global printInputParFlag, basissetFileName
    n_at = int(0)
    one_body_type = int(1)
    two_body_type = int(2)
    cusps_order = int(5)
    atom_names = []
    inputParamsFile = "empty"
    basissetFileName = "empty"
    xyzFileName = "empty"
    wavefunction = str('rsd')
    printInputParFlag = False
    atomsDataBase = [
    ['Hydrogen','H','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Helium','He','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Lithium','Li','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Beryllium','Be','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Boron','B','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Carbon','C','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Nitrogen','N','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Oxygen','O','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Fluorine','F','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Neon','Ne','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Sodium','Na','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Magnesium','Mg','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Aluminum','Al','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Silicon','Si','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Phosphorous','P','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Sulfur','S','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Chlorine','Cl','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Argon','Ar','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Potassium','K','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Calcium','Ca','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Scandium','Sc','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Titanium','Ti','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Vanadium','V','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Chromium','Cr','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Manganese','Mn','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Iron','Fe','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Cobalt','Co','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Nickel','Ni','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Copper','Cu','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Zinc','Zn','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Gallium','Ga','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Germanium','Ge','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Arsenic','As','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Selenium','Se','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Bromine','Br','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Krypton','Kr','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Rubidium','Rb','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Strontium','Sr','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Yttrium','Y','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Zirconium','Zr','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Niobium','Nb','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Molybdenum','Mo','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Technetium','Tc','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Ruthenium','Ru','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Rhodium','Rh','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Palladium','Pd','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Silver','Ag','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Cadmium','Cd','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Indium','In','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Tin','Sn','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Antimony','Sb','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Tellurium','Te','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Iodine','I','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Xenon','Xe','cc-pVDZ','ccECP','3sG2pG1dG'],
    ['Cesium','Cs','cc-pVDZ','ccECP','3sG2pG1dG']
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

# Print input Arguments
def printInputArguments():
    print()
    print(" Required input arguments:")
    print()
    print(" XYZFile = ",xyzFileName)
    print()
    print(" Optional inputs:")
    print()
    print(" BasFile = ",basissetFileName)
    print(" wf      = ",wavefunction)
    print(" oneb    = ",one_body_type)
    print(" twob    = ",two_body_type)
    print(" CspO    = ",cusps_order)
    print(" ipar    = ",inputParamsFile)
    print()

# Print Params file for basis set
def printInputParamsFile():
    pointerInputParamsFile = open(inputParamsFile, "w" )
    for i in atomsDataBase :
        pointerInputParamsFile.write(i[1]+" "+i[2]+" "+i[3]+" "+i[4]+"\n")
    pointerInputParamsFile.close()

# Read Params file for basis set
def readInputParamsFile():
    global atomsDataBase
    pointerInputParamsFile = open(inputParamsFile, "r" )
    inputParamsFileLines = pointerInputParamsFile.readlines()
    for line in inputParamsFileLines :
        if (len(line.split()) <=3 ) :
            break
        for i in atomsDataBase :
            if ( i[1] == line.split()[0] ) :
                i[2] = line.split()[1]
                i[3] = line.split()[2]
                i[4] = line.split()[3]
                break
    pointerInputParamsFile.close()

# Read QMeCha XYZ file
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
        atom_names =[ atom for atom in atom_names if '*' in atom ]
        for line_num in range(len(atom_names)) :
            atom_names[line_num]=atom_names[line_num].replace('*', '')
        n_pseudo = len(atom_names)
        molFile.close()
    except:
        print(" Couldn't open file molecular QMeCha file")
        printHelp()
        exit()

# Read arguments
def readArguments():
    global wavefunction
    global xyzFileName
    global one_body_type
    global two_body_type
    global cusps_order
    global inputParamsFile
    global printInputParFlag
    global basissetFileName
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
        if ( sys.argv[i] == '-bas'):
            basissetFileName = str(sys.argv[i+1])
        if ( sys.argv[i] == '-prnt'):
            printInputParFlag = True
    if (basissetFileName=='empty'):
        #basissetFileName=xyzFileName.removesuffix('.xyz')+'.bas'
        basissetFileName=xyzFileName.replace('.xyz','.bas')

# Print atomic basis set
def printAtomicBasisset(atom,basistype,pseudotype,n_jorbs):
    atomicBasFile =open(qmecha_dir+'/basissets/'+pseudotype+'/'+atom+'.'+basistype+'.qmecha', 'r')
    atomicBasFileLines=atomicBasFile.readlines()
    pointerBasissetFile.write("# Basis set "+basistype+" "+pseudotype+"\n")
    if (pseudotype == 'AE') :
        pointerBasissetFile.write( atomicBasFileLines[0].split()[0]+" "+atomicBasFileLines[0].split()[1]+" "+str(n_jorbs)+"\n" ) 
    else:
        pointerBasissetFile.write( '*'+atomicBasFileLines[0].split()[0]+" "+atomicBasFileLines[0].split()[1]+" "+str(n_jorbs)+"\n" ) 
    for line in range(1,len(atomicBasFileLines)) :
        pointerBasissetFile.write(str(atomicBasFileLines[line]))
    atomicBasFile.close()


# Build and print Atomic Jastrow factor
def printAtomicJastrow(jorbs):
    pointerBasissetFile.write("# Jastrow basis set \n")
    orb_type_G = np.zeros(5,dtype=int)
    orb_type_S = np.zeros(5,dtype=int)
    orb_type_E = np.zeros(5,dtype=int)
    orb_type_M = np.zeros(5,dtype=int)
    for k1 in range(0,len(jorbs),3) :
        if (jorbs[k1+2].upper()=='G' ) :
            if (jorbs[k1+1].upper()=='S' ) :
                orb_type_G[0] = orb_type_G[0] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='P' ) :
                orb_type_G[1] = orb_type_G[1] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='D' ) :
                orb_type_G[2] = orb_type_G[2] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='F' ) :
                orb_type_G[3] = orb_type_G[3] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='G' ) :
                orb_type_G[4] = orb_type_G[4] + int(jorbs[k1])
        if (jorbs[k1+2].upper()=='S' ) :
            if (jorbs[k1+1].upper()=='S' ) :
                orb_type_S[0] = orb_type_S[0] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='P' ) :
                orb_type_S[1] = orb_type_S[1] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='D' ) :
                orb_type_S[2] = orb_type_S[2] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='F' ) :
                orb_type_S[3] = orb_type_S[3] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='G' ) :
                orb_type_S[4] = orb_type_S[4] + int(jorbs[k1])
        if (jorbs[k1+2].upper()=='E' ) :
            if (jorbs[k1+1].upper()=='S' ) :
                orb_type_E[0] = orb_type_E[0] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='P' ) :
                orb_type_E[1] = orb_type_E[1] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='D' ) :
                orb_type_E[2] = orb_type_E[2] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='F' ) :
                orb_type_E[3] = orb_type_E[3] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='G' ) :
                orb_type_E[4] = orb_type_E[4] + int(jorbs[k1])
        if (jorbs[k1+2].upper()=='M' ) :
            if (jorbs[k1+1].upper()=='S' ) :
                orb_type_M[0] = orb_type_M[0] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='P' ) :
                orb_type_M[1] = orb_type_M[1] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='D' ) :
                orb_type_M[2] = orb_type_M[2] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='F' ) :
                orb_type_M[3] = orb_type_M[3] + int(jorbs[k1])
            if (jorbs[k1+1].upper()=='G' ) :
                orb_type_M[4] = orb_type_M[4] + int(jorbs[k1])

    # generate exponentials
    exp_type_G = [[],[],[],[],[]]
    exp_type_S = [[],[],[],[],[]]
    exp_type_E = [[],[],[],[],[]]
    exp_type_M = [[],[],[],[],[]]
    z_s = []
    z_p = []
    z_d = []
    z_f = []
    z_g = []
    for k1 in range(5):
        if   (k1 == 0):
            a=0.1
        elif (k1 == 1):
            a=0.25
        elif (k1 == 2):
            a=0.50
        elif (k1 == 3):
            a=0.75
        elif (k1 == 4):
            a=1.00
        if ( orb_type_G[k1] > 0):
            for k2 in range(orb_type_G[k1]) :
                exp_type_G[k1].append(a+(1.0/np.sqrt(float(orb_type_G[k1] )))*float(orb_type_G[k1] -k2-1)**(1.7))
        if ( orb_type_S[k1] > 0):
            for k2 in range(orb_type_S[k1]) :
                exp_type_S[k1].append(a+(1.0/np.sqrt(float(orb_type_S[k1] )))*float(orb_type_S[k1] -k2-1)**(1.7))
        if ( orb_type_E[k1] > 0):
            for k2 in range(orb_type_E[k1]) :
                exp_type_E[k1].append(a+(1.0/np.sqrt(float(orb_type_E[k1] )))*float(orb_type_E[k1] -k2-1)**(1.7))
        if ( orb_type_M[k1] > 0):
            for k2 in range(orb_type_M[k1]) :
                exp_type_M[k1].append(a+(1.0/np.sqrt(float(orb_type_M[k1] )))*float(orb_type_M[k1] -k2-1)**(1.7))

    # Print contracted orbitals to file
    # Jorge suggests this could be a dictionary
    for k1 in range(0,len(jorbs),3) :
        n_orbs=int(jorbs[k1])
        if (jorbs[k1+1].upper()=='S' ) :
            l_orbs= 0
        elif (jorbs[k1+1].upper()=='P' ) :
            l_orbs= 1
        elif (jorbs[k1+1].upper()=='D' ) :
            l_orbs= 2
        elif (jorbs[k1+1].upper()=='F' ) :
            l_orbs= 3
        elif (jorbs[k1+1].upper()=='G' ) :
            l_orbs= 4
        orb_type=jorbs[k1+2].upper()
        pointerBasissetFile.write(" "+jorbs[k1+1].upper()+str(" %3d" % (n_orbs))+"\n")
        if ( orb_type == 'G'):
            printOrbital(n_orbs,orb_type,exp_type_G[:][l_orbs])
        elif (orb_type == 'S') :
            printOrbital(n_orbs,orb_type,exp_type_S[:][l_orbs])
        elif (orb_type == 'E' ) :
            printOrbital(n_orbs,orb_type,exp_type_E[:][l_orbs])
        elif (orb_type == 'M' ) :
            printOrbital(n_orbs,orb_type,exp_type_M[:][l_orbs])

# Print orbital 
def printOrbital(n_orbs,orb_type,orb_z):
    if (n_orbs >= 1):
        for k1 in range(n_orbs) :
            c=1.000-float(n_orbs-k1-1)/float(n_orbs)
            line=str(" %15.7F %10.7F" % (float(orb_z[0]),float(c)))
            pointerBasissetFile.write(line+" 1"+orb_type+"\n")
            del orb_z[0]


# Print Basis set file
def printBasisFile():
    global pointerBasissetFile
    pointerBasissetFile = open( basissetFileName, "w" )
    pointerBasissetFile.write("# Wave function \n")
    pointerBasissetFile.write(" {} \n".format(wavefunction))
    pointerBasissetFile.write("# One body \n")
    pointerBasissetFile.write("  %2i  %2i \n" % (one_body_type,cusps_order))
    pointerBasissetFile.write("# Two body \n")
    pointerBasissetFile.write("  %2i  %2i \n" % (two_body_type,cusps_order))
    basistype = ""
    pseudotype = ""
    jastroworbs = ""
    jastrowtype = ""
    n_jorbs = 0
    for i in atom_names :
        for j in range(len(atomsDataBase)) :
            if i == atomsDataBase[j][1] :
                basistype   = atomsDataBase[j][2]
                pseudotype  = atomsDataBase[j][3]
                jastroworbs = atomsDataBase[j][4]
                break
        n_jorbs=int(len(jastroworbs)/3) 
        printAtomicBasisset(i,basistype,pseudotype,n_jorbs)
        printAtomicJastrow(jastroworbs)
    pointerBasissetFile.close()

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
        inputParamsFile='param.inp'
        printInputParamsFile()
        print(" Printing default parameter file param.inp")
        print(" =======================================================================")
        exit()
    if ( xyzFileName == 'empty'):
        print(" Missing molecular QMeCha file in input")
        printHelp()
        print(" =======================================================================")
        exit()
    printInputArguments()
    readMolFile()
    if (inputParamsFile != "empty" ):
        readInputParamsFile()
    printBasisFile()

    print(" =======================================================================")
