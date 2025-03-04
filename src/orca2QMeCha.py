#!/usr/bin/python
import sys
import math
import numpy

# Read and allocate orca file lines
def readOrcaFile( fileName ):
    fileToRead = open(fileName, "r")
    fileLines = fileToRead.readlines()
    fileToRead.close()
    return fileLines

# Read orca file header 
def readOrcaHead ( orcaFileLines ):
    for i in range(0, len(orcaFileLines) ) :
        line = orcaFileLines[i]

        if "# of contracted shells                  ..." in line :
            n_cart_orb = int( line.split()[5] )
        if "Hartree-Fock type      HFTyp           ...." in line :
            scftyp = line.split()[4]
        if "Total Charge           Charge          ...." in line : 
            tot_chr = int( line.split()[4] )
        if "Multiplicity           Mult            ...." in line : 
            mult = int( line.split()[3] )
        if "Number of Electrons    NEL             ...." in line : 
            n_el = int( line.split()[5] )
        if "Basis Dimension        Dim             ...." in line : 
            n_sphe_orb = int( line.split()[4] )
        # Orca 5.0.4
        if "Number of basis functions                   ..." in line :
            n_cart_orb = int( line.split()[5] )

    # Compute number of occupied orbitals
    n_occ_beta = int((n_el-mult+1)/2)
    n_occ_alpha = n_occ_beta+mult-1

    print("NUMBER OF CARTESIAN ORBITALS            :", n_cart_orb)
    print("NUMBER OF SPHERICAL HARMONICAL ORBITALS :", n_sphe_orb)
    print("NUMBER OF OCCUPIED ALPHA ORBITALS       :", n_occ_alpha) 
    print("NUMBER OF OCCUPIED BETA ORBITALS        :", n_occ_beta)
    print("SCFTYP                                  :", scftyp)

    return n_sphe_orb, n_occ_alpha, n_occ_beta, scftyp

# Read molecular orbitals into the matrix
def readOrcaMolOrb ( scfType, orcaFileLines, numAlphaOrbs, numBetaOrbs, numBas):
    scanLine = 'MOLECULAR ORBITALS'
    numBlocks = int(numAlphaOrbs/6)
    numResidu = numAlphaOrbs - numBlocks*6
    label_vector = []
    tmpCoefMatAlpha = numpy.zeros ((numAlphaOrbs,numBas),dtype=float)
    for i in range(0, len(orcaFileLines) ) :
        line = orcaFileLines[i]
        if scanLine in line :
            xi = i + 6
            xf = xi + numBas 
            oi = 0
            if numBlocks>=1:
                for n_blocks in range(0,numBlocks):
                    coef_num=0
                    for x in range(xi,xf):
                        line = orcaFileLines[x]
                        if (n_blocks==0) :
                            label_vector.append(str(line.split()[1]))
                        for y in range(0,6):
                            tmpCoefMatAlpha[y+oi][coef_num] =float( line.split()[y+2] )
                        coef_num+=1

                    oi+=6    
                    xi = xf+4
                    xf = xi + numBas

            if numResidu>=1:
                coef_num=0
                for x in range(xi,xf):
                    line = orcaFileLines[x]
                    if (numBlocks==0) :
                        label_vector.append(str(line.split()[1]))
                    for y in range(0,numResidu):
                        tmpCoefMatAlpha[y+oi][coef_num] =float( line.split()[y+2] )
                    coef_num+=1
            break

    if scfType == 'UHF':
        scanLine = '0         1         2         3         4         5'
        numBlocks = int(numBetaOrbs/6)
        numResidu = numBetaOrbs - numBlocks*6
        tmpCoefMatBeta = numpy.zeros ((numBetaOrbs,numBas),dtype=float)
        start_line = xf
        for i in range(start_line, len(orcaFileLines) ) :
            line = orcaFileLines[i]
            if scanLine in line :
                xi = i + 4
                xf = xi + numBas 
                oi = 0
                if numBlocks>=1:
                    for n_blocks in range(0,numBlocks):
                        coef_num=0
                        for x in range(xi,xf):
                            line = orcaFileLines[x]
                            for y in range(0,6):
                                tmpCoefMatBeta[y+oi][coef_num] =float( line.split()[y+2] )
                            coef_num+=1

                        oi+=6    
                        xi = xf+4
                        xf = xi + numBas

                if numResidu>=1:
                    coef_num=0
                    for x in range(xi,xf):
                        line = orcaFileLines[x]
                        for y in range(0,numResidu):
                            tmpCoefMatBeta[y+oi][coef_num] =float( line.split()[y+2] )
                        coef_num+=1
                break

    if scfType == 'UHF':
        return label_vector, tmpCoefMatAlpha, tmpCoefMatBeta
    else:
        return label_vector, tmpCoefMatAlpha

# Reorder Orca orbitals according to QMeCha
def reordOrcaOrbs ( orbList, numOrb, numBas, tmpCoefMat ):

    coefMat = numpy.zeros ((numOrb,numBas),dtype=float)

    coef_num = 0
    while ( coef_num < numBas ):

        if   ('pz' in orbList[coef_num]):
            for orb_num in range(0,numOrb):
                coefMat[orb_num][coef_num+1]= tmpCoefMat[orb_num][coef_num]    # pz -> 2
                coefMat[orb_num][coef_num+2]= tmpCoefMat[orb_num][coef_num+1]  # px -> 3
                coefMat[orb_num][coef_num]  = tmpCoefMat[orb_num][coef_num+2]  # py -> 1
            coef_num+=3
        elif ('dz2'in orbList[coef_num]):
            for orb_num in range(0,numOrb):
                coefMat[orb_num][coef_num+2]=tmpCoefMat[orb_num][coef_num]     # dz2 -> 3
                coefMat[orb_num][coef_num+3]=tmpCoefMat[orb_num][coef_num+1]   # dxz -> 4 
                coefMat[orb_num][coef_num+1]=tmpCoefMat[orb_num][coef_num+2]   # dyz -> 2
                coefMat[orb_num][coef_num+4]=tmpCoefMat[orb_num][coef_num+3]   # dx2y2 -> 5
                coefMat[orb_num][coef_num]  =tmpCoefMat[orb_num][coef_num+4]   # dxy -> 1 
            coef_num+=5
        elif ('f0'in orbList[coef_num]):
            for orb_num in range(0,numOrb):
                coefMat[orb_num][coef_num+3]=tmpCoefMat[orb_num][coef_num]     # f0  -> 4
                coefMat[orb_num][coef_num+4]=tmpCoefMat[orb_num][coef_num+1]   # f+1 -> 5 
                coefMat[orb_num][coef_num+2]=tmpCoefMat[orb_num][coef_num+2]   # f-1 -> 3
                coefMat[orb_num][coef_num+5]=tmpCoefMat[orb_num][coef_num+3]   # f+2 -> 6
                coefMat[orb_num][coef_num+1]=tmpCoefMat[orb_num][coef_num+4]   # f-2 -> 2 
                coefMat[orb_num][coef_num+6]=-tmpCoefMat[orb_num][coef_num+5]   # f+3 -> 7
                coefMat[orb_num][coef_num]  =-tmpCoefMat[orb_num][coef_num+6]   # f-3 -> 1 
            coef_num+=7
        elif ('g0'in orbList[coef_num]):
            for orb_num in range(0,numOrb):
                coefMat[orb_num][coef_num+4]=tmpCoefMat[orb_num][coef_num]     # g0  -> 5
                coefMat[orb_num][coef_num+5]=tmpCoefMat[orb_num][coef_num+1]   # g+1 -> 6 
                coefMat[orb_num][coef_num+3]=tmpCoefMat[orb_num][coef_num+2]   # g-1 -> 4
                coefMat[orb_num][coef_num+6]=tmpCoefMat[orb_num][coef_num+3]   # g+2 -> 7
                coefMat[orb_num][coef_num+2]=tmpCoefMat[orb_num][coef_num+4]   # g-2 -> 3 
                coefMat[orb_num][coef_num+7]=-tmpCoefMat[orb_num][coef_num+5]   # g+3 -> 8
                coefMat[orb_num][coef_num+1]=-tmpCoefMat[orb_num][coef_num+6]   # g-3 -> 2 
                coefMat[orb_num][coef_num+8]=-tmpCoefMat[orb_num][coef_num+7]   # g+4 -> 9
                coefMat[orb_num][coef_num]  =-tmpCoefMat[orb_num][coef_num+8]   # g-4 -> 1 
            coef_num+=9
        else:
            for orb_num in range(0,numOrb):
                coefMat[orb_num][coef_num]=tmpCoefMat[orb_num][coef_num]
            coef_num+=1

    return coefMat

# Write QMeCha Slater coefficients' file
def writeQmechaFile ( qmechaFileName, numBas, numAlphaOrbs, numBetaOrbs, alphaCoefMat, betaCoefMat ):
    qmechaFile = open(qmechaFileName,"w")
    qmechaFile.write("# Slater coefficients for Spin up matrix\n")

    for j1 in range (0,numAlphaOrbs,6) :
        for i in range (0,numBas ) :
            qmechaFile.write("  ")
            for j in range (j1, j1 + 6 ) :
                if j < numAlphaOrbs:
                    qmechaFile.write("% .9E " % alphaCoefMat[j][i] )
            qmechaFile.write("\n")

    qmechaFile.write("# Slater coefficients for Spin down matrix\n")
    for j1 in range (0,numBetaOrbs,6) :
        for i in range (0,numBas ) :
            qmechaFile.write("  ")
            for j in range (j1, j1 + 6 ) :
                if j < numBetaOrbs:
                    qmechaFile.write("% .9E " % betaCoefMat[j][i] )
            qmechaFile.write("\n")

    qmechaFile.close

# List of non-Zero elements in coeffs Matrix
def findNonZeroEle ( numBas,numOrbs, coefMat):
    nonZeroEleList =[]
    
    for morb in range(0,numOrbs):
        for aorb in range(0,numBas):
            if abs(coefMat[morb][aorb])>10.0e-09:
                nonZeroEleList.append([aorb,morb])
                
    return nonZeroEleList

# List of non-Zero elements in coeffs Matrix
def checkSymmOrbs (numBas, orb1, orb2):
    
    isSymm = True
    for i1 in range(0,numBas):
        if abs(orb1[i1])>2e-6:
            eleFound = False
            for i2 in range(0,numBas):
                if ( abs(abs(orb1[i1])-abs(orb2[i2]))<2e-6 ):
                    eleFound = True
                    break
        else:
            eleFound = True

        if (eleFound == False): 
            isSymm = False
            break
                
    return isSymm

# Write QMecha Symmetry file for Slater determinants
def writeQmechaSymFile ( qmechaSymFileName, nzLstalpha, nzListbeta ):
    qmechaFile = open(qmechaSymFileName,"w")
    qmechaFile.write("# List of non-zero elements for spin-up electrons\n")
    numEle = int(len(nzLstalpha))
    numMolorb = nzLstalpha[numEle-1][1]+1
    qmechaFile.write("{:8d}\n".format(numEle))
    for i in range (0,numEle) :
        qmechaFile.write("{:8d} {:8d}\n".format(nzLstalpha[i][0]+1, nzLstalpha[i][1]+1))

    qmechaFile.write("# List of symmetries for spin-up electrons\n")
    qmechaFile.write("{:8d}\n".format(numEle-numMolorb))
    initOrb=0
    for i in range (0,numEle) :
        if nzLstalpha[i][1]+1==initOrb:
            qmechaFile.write("{:8d} {:8d} {:8d}\n".format(1,nzLstalpha[i][0]+1, nzLstalpha[i][1]+1))
        else:
            initOrb=nzLstalpha[i][1]+1

    qmechaFile.write("# List of non-zero elements for spin-down electrons\n")
    numEle = int(len(nzListbeta))
    qmechaFile.write("{:8d}\n".format(numEle))
    for i in range (0,numEle) :
        qmechaFile.write("{:8d} {:8d}\n".format(nzListbeta[i][0]+1, nzListbeta[i][1]+1))

    numMolorb = nzListbeta[numEle-1][1]+1
    qmechaFile.write("# List of symmetries for spin-down electrons\n")
    qmechaFile.write("{:8d}\n".format(numEle-numMolorb))
    initOrb=0
    for i in range (0,numEle) :
        if nzListbeta[i][1]+1==initOrb:
            qmechaFile.write("{:8d} {:8d} {:8d}\n".format(1,nzListbeta[i][0]+1, nzListbeta[i][1]+1))
        else:
            initOrb=nzListbeta[i][1]+1


    qmechaFile.close 

if __name__ == "__main__":
    orcaFileName = sys.argv[1]
    qmechaFileName = orcaFileName + ".slde.sav"
    qmechaSymFileName = orcaFileName + ".slde_s.sav"
    
    print("ORCA file              :", orcaFileName)
    print("QMECHA file            :", qmechaFileName)
    print("QMECHA Symmetries file :", qmechaSymFileName)

    orcaFileLines = readOrcaFile( orcaFileName )

    n_orbs, n_occ_alpha, n_occ_beta, scftyp = readOrcaHead ( orcaFileLines )

    # Converting Orca coefficients to QMeCha
    if scftyp == "RHF" or scftyp == "ROHF":
        label_vector, tmp_coef = readOrcaMolOrb ( scftyp, orcaFileLines, n_occ_alpha, n_occ_beta, n_orbs)
        alpha_coef = reordOrcaOrbs ( label_vector, n_occ_alpha, n_orbs, tmp_coef )
        writeQmechaFile ( qmechaFileName, n_orbs, n_occ_alpha, n_occ_beta, alpha_coef, alpha_coef )
        nonZeroEleList_alpha = findNonZeroEle (n_orbs, n_occ_alpha, alpha_coef )
        nonZeroEleList_beta = findNonZeroEle (n_orbs, n_occ_beta, alpha_coef )
        writeQmechaSymFile ( qmechaSymFileName, nonZeroEleList_alpha, nonZeroEleList_beta )
    else:
        label_vector, tmp_coefAlpha, tmp_coefBeta = readOrcaMolOrb ( scftyp, orcaFileLines, n_occ_alpha, n_occ_beta, n_orbs)
        alpha_coef = reordOrcaOrbs ( label_vector, n_occ_alpha, n_orbs, tmp_coefAlpha )
        beta_coef = reordOrcaOrbs ( label_vector, n_occ_beta, n_orbs, tmp_coefBeta )
        writeQmechaFile ( qmechaFileName, n_orbs, n_occ_alpha, n_occ_beta, alpha_coef, beta_coef )
        nonZeroEleList_alpha = findNonZeroEle (n_orbs, n_occ_alpha, alpha_coef )
        nonZeroEleList_beta = findNonZeroEle (n_orbs, n_occ_beta, beta_coef )
        writeQmechaSymFile ( qmechaSymFileName, nonZeroEleList_alpha, nonZeroEleList_beta )


