#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import numpy as np

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

# Load default variables
def loadDefaultVariables():
    global n_at
    global n_pseudo
    global n_psd_grd_pnts
    global xyzFileName
    global ene_psd_cut
    global psd_int_mthd
    global pseudo
    global atom_names
    atom_names = []
    n_at = int(0)
    n_pseudo = int(0)
    n_psd_grd_pnts = int(8)
    xyzFileName="empty"
    ene_psd_cut=float(0.0001)
    psd_int_mthd=int(0)
    pseudo="ccECP"

def readArguments():
    global n_psd_grd_pnts
    global xyzFileName
    global ene_psd_cut
    global psd_int_mthd
    global pseudo
    for i in range(1,len(sys.argv)) :
        if ( sys.argv[i] == '-n_int'):
            n_psd_grd_pnts = int(sys.argv[i+1])
        if ( sys.argv[i] == '-cutoff'):
            ene_psd_cut = float(sys.argv[i+1])
        if ( sys.argv[i] == '-int'):
            if ( str(sys.argv[i+1])=='LA' ) :
                psd_int_mthd = 0
            else :
                psd_int_mthd = 1
        if ( sys.argv[i] == '-xyz'):
            xyzFileName = str(sys.argv[i+1])
        if ( sys.argv[i] == '-pseudo'):
            pseudo = str(sys.argv[i+1])

# Print Help info 
def printHelp():
    print()
    print(" Required input arguments:")
    print()
    print("   -xyz    Molecular *.xyz file")
    print()
    print(" Optional inputs:")
    print()
    print("   -n_int   The number of integration points (integer) [Default 8]")
    print("   -cutoff  The energy cut off (float) [Default = 0.0001]")
    print("   -int     Pseudo integration method LA or DLA (string) [Default = 'LA']")
    print("   -pseudo  Pseudo type ccECP eCEPP BFD (string) [Default = 'ccECP']")
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
    print(" n_int   = ",n_psd_grd_pnts)
    print(" cutoff  = ",ene_psd_cut)
    if (psd_int_mthd == 0):
        print(" int     = LA")
    else:
        print(" int     = DLA")
    print(" pseudo  = ",pseudo)
    print()

# Print pseudo QMeCha file.
def printPseudoFile():
    psdOutFileName = 'pseudo.dat'
    psdOutFile = open(psdOutFileName, "w" )
    psdOutFile.write("&pseudo\n")
    psdOutFile.write("n_pseudo       ="+str(n_pseudo)+'\n')
    psdOutFile.write("n_psd_grd_pnts ="+str(n_psd_grd_pnts)+'\n')
    psdOutFile.write("ene_psd_cut    ="+str(ene_psd_cut)+'\n')
    psdOutFile.write("psd_int_mthd   ="+str(psd_int_mthd)+'\n')
    psdOutFile.write("/\n")
    for i in atom_names :
        printPseudo(i,pseudo,psdOutFile)
    psdOutFile.close()

# Print pseudo parameters.
def printPseudo(atom,pseudoname,outFile):
    file_path=qmecha_dir+'/pseudopotentials/'+pseudoname+'/'+atom+'.qmecha'
    if(os.path.isfile(file_path)) :
        psdFile =open(file_path, 'r')
        psdFileLines=psdFile.readlines()
        for line in range(len(psdFileLines)) :
            outFile.write(str(psdFileLines[line]))
        psdFile.close()
    else:
        print(" ERROR!!! Pseudo potential "+pseudoname+" for atom "+atom+" is not present")


# Read pseudo parameters.
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


if __name__ == "__main__":
    print(" =======================================================================")
    print(" ===================== Pseudo generator for QMeCha =====================")
    print(" =======================================================================")
    loadDefaultVariables()
    checkToolsDir()
    if (len(sys.argv) == 1 ) :
        printHelp()
        exit()
    else:
        readArguments()
    printInputParameters()
    readMolFile()    
    printPseudoFile()
    print(" =======================================================================")