#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Script to convert *.xyz files to QMeCha molecular files.
All the properties need to be specified by the user.
The defaults describe a neutral electronic system in 
a singlet spin state.
"""
import sys
import os

# Load default variables
def loadDefaultVariables():
    global n_el
    global n_po 
    global spin_e 
    global spin_p
    global m_p
    global m_e 
    global chrg 
    global mult 
    global xyzFileName
    global systemName
    global atom_names
    global atom_x, atom_y, atom_z
    global print_spin_e, print_spin_p, print_n_po, print_n_el
    global pseudo
    n_el = int(0)
    n_po = int(0)
    spin_e = float(0.0)
    spin_p = float(0.0)
    m_p = float(1.0)
    m_e = float(1.0)
    chrg = int(0)
    mult = int(1)
    xyzFileName="empty"
    systemName="empty"
    atom_names=[]
    atom_x=[]
    atom_y=[]
    atom_z=[]
    print_spin_e=False 
    print_spin_p=False 
    print_n_el=False
    print_n_po=False
    pseudo=False

# Print molecular QMeCha file
def printMolFile():
    molFileName = systemName+'.xyz'
    check_file = os.path.isfile(molFileName)
    if check_file == False:
        molFilePointer = open(molFileName, "w" )
        molFilePointer.write("&molsys\n")
        molFilePointer.write("n_at = "+str(n_at)+'\n')
        if (print_n_el): 
            molFilePointer.write("n_el = "+str(n_el)+'\n')
        if (print_n_po): 
            molFilePointer.write("n_po = "+str(n_po)+'\n')
        if( m_e != 1.0 ): 
            molFilePointer.write("m_e = "+str(m_e)+'\n')
        if( m_p != 1.0 ): 
            molFilePointer.write("m_p = "+str(m_p)+'\n')
        if (print_spin_e): 
            molFilePointer.write("spin_e = "+str(spin_e)+'\n')
        if (print_spin_p): 
            molFilePointer.write("spin_p = "+str(spin_p)+'\n')
        if ( print_n_el==False and print_n_po==False): 
            molFilePointer.write("chrg = "+str(chrg)+'\n')
        if ( print_spin_e==False and print_spin_p==False ): 
            molFilePointer.write("mult = "+str(mult)+'\n')
        molFilePointer.write("units = 'angs'\n")
        molFilePointer.write("/\n")
        for i in range(n_at) :
            if (pseudo):
                molFilePointer.write('*%s %13.8f %13.8f %13.8f \n' % (atom_names[i],atom_x[i],atom_y[i],atom_z[i]))
            else:
                molFilePointer.write('%s %13.8f %13.8f %13.8f \n' % (atom_names[i],atom_x[i],atom_y[i],atom_z[i]))
        molFilePointer.close()
    else:
        print("WARNING!!! Outfile is already present, please remove it or rename it.") 

# Read standard XYZ file
def readXYZFile():
    global n_at
    xyzFilePointer = open(xyzFileName, "r" )
    n_at=int(xyzFilePointer.readline().split()[0])
    xyzFilePointer.readline() # Skip empty line
    for i in range(n_at) :
        line=xyzFilePointer.readline()
        atom_names.append(str(line.split()[0]))
        atom_x.append(float(line.split()[1]))
        atom_y.append(float(line.split()[2]))
        atom_z.append(float(line.split()[3]))
    xyzFilePointer.close()

# Print input parameters
def printInputParameters():
    print()
    print(" Required input arguments:")
    print()
    print(" XYZFile = ",xyzFileName)
    print(" SysFile = ",systemName)
    print(" mult    = ",mult)
    print(" chrg    = ",chrg)
    print()
    print(" Optional inputs:")
    print()
    print(" n_el    = ",n_el)
    print(" n_po    = ",n_po)
    print(" m_e     = ",m_e)
    print(" m_p     = ",m_p)
    print(" spin_e  = ",spin_e)
    print(" spin_p  = ",spin_p)
    print(" pseudo  = ",pseudo)
    print()

# Print Help info 
def printHelp():
    print()
    print(" Required input arguments:")
    print()
    print("   -xyz    Molecular *.xyz file")
    print("   -sys    Name of the Molecular system")
    print("           (be aware that the it has to be different from the *.xyz file)")
    print("   -mult   Multiplicity of the system's spin (default 1). Required if n_el or n_po not specified.")
    print("   -chrg   Total charge of the system (default 0). Reauired if spin_e or spin_p not specified.")
    print()
    print(" Optional inputs:")
    print()
    print("   -n_el   Number of positrons (default 0)")
    print("   -n_po   Number of positrons (default 0)")
    print("   -m_e    Mass of the electrons (default 1.0)")
    print("   -m_p    Mass of the positrons (default 1.0)")
    print("   -spin_e Total Spin of the electrons (default 0.0)")
    print("   -spin_p Total Spin of the positrons (default 0.0)")
    print("   -pseudo Add pseudo to all atoms")
    print()

# Read input arguments
def readArguments():
    global n_el
    global n_po 
    global spin_e 
    global spin_p
    global m_p
    global m_e 
    global chrg 
    global mult 
    global xyzFileName
    global systemName
    global print_spin_e, print_spin_p, print_n_po, print_n_el
    global pseudo
    for i in range(1,len(sys.argv)) :
        if ( sys.argv[i] == '-n_el'):
            n_el = int(sys.argv[i+1])
            print_n_el=True
        if ( sys.argv[i] == '-n_po'):
            n_po = int(sys.argv[i+1])
            print_n_po=True
        if ( sys.argv[i] == '-spin_e'):
            spin_e = float(sys.argv[i+1])
            print_spin_e=True
        if ( sys.argv[i] == '-spin_p'):
            spin_p = float(sys.argv[i+1])
            print_spin_p=True
        if ( sys.argv[i] == '-m_p'):
            m_p = float(sys.argv[i+1])
        if ( sys.argv[i] == '-m_e'):
            m_e = float(sys.argv[i+1])
        if ( sys.argv[i] == '-chrg'):
            chrg = int(sys.argv[i+1])
        if ( sys.argv[i] == '-mult'):
            mult = int(sys.argv[i+1])
        if ( sys.argv[i] == '-xyz'):
            xyzFileName = str(sys.argv[i+1])
        if ( sys.argv[i] == '-sys'):
            systemName = str(sys.argv[i+1])
        if ( sys.argv[i] == '-pseudo'):
            pseudo=True


if __name__ == "__main__":
    print(" =======================================================================")
    print(" =           XYZ file converter to Molecular file in QMeCha            =")
    print(" =======================================================================")
    loadDefaultVariables()
    if (len(sys.argv) == 1 ) :
        printHelp()
        exit()
    else:
        readArguments()
    
    printInputParameters()

    if (systemName=="empty" or xyzFileName == 'empty' ):
        print(" ERROR!!! Input or output file not specified.") 
        printHelp()
        exit()
            
    readXYZFile()
    printMolFile()

    print(" =======================================================================")
