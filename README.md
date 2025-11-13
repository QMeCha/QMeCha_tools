
<img src="logo_extended_tools.png" >

<b>Quantum MeCha (QMeCha)[^a] - Tools </b>

This repository contains some of the tools to initialize the molecular system file, the basis set and the pseudopotential of the QMeCha code.

QMeCha is a quantum Monte Carlo package started in 2017 by [Dr. Matteo Barborini](https://www.uni.lu/fstm-en/people/matteo-barborini/) a Research Scientist at the [HPC Platform](https://www.uni.lu/research-en/core-facilities/hpc/) of the [University of Luxembourg](https://www.uni.lu), that is also the main developer of the code till now.

For questions regarding the code please contact the creator directly.

QMeCha is an endeavor that takes time and effort. \
In order to support the young researchers that are behind its development, please cite the papers below that refer to the methods used. 

Furthermore, please keep the creator of the code updated regarding the research that you are publishing with QMeCha. \
This will enable the creator to use it to further promote his work, that serves your research. 

Naturally, the creator is always willing to open new collaborations as contributor and co-supervisor.

<b>Creator, main developer and scientific supervisor:</b>\
Barborini, Matteo

<b>Collaborators:</b>\
Charry Martinez, Jorge Alfonso : Electron-Positron systems\
Ditte, Matej : El-QDO method of electrons embedded in quantum Drude Oscillators and point charges\
Andronikos, Leventis : Electronic wave functions and correlation effects\
Kafanas, Georgios : Compilation, portability and optimization

### Citing the code

**QMeCha: quantum Monte Carlo package for fermions in embedding environments**\
Matteo Barborini, Jorge Charry, Matej Ditte, Andronikos Leventis, Georgios Kafanas, Alexandre Tkatchenko\
[*arXiv* (2025)](https://doi.org/10.48550/arXiv.2511.03439)


### Basis sets and pseudopotentials in QMeCha format

The organization of the files is discussed in depth in the manual. Here we briefly recall the basic aspects.
The Basis sets and pseudopotentials contained in this repository are adjusted from the repository of [M. Burkatzki, C. Filippi and M. Dolg](http://burkatzki.com/pseudos/index.2.html) and from the [Pseudopotential Library](https://pseudopotentiallibrary.org/).

Up till now the repository contains the BFD[^1], ccECP[^2] and eCEPP[^3] pseudopotentials with the corresponding basis sets.

### Basis sets format

**It is important to underline that all the basis sets have been reduced up to the G primitive functions. H Orbitals have been removed.**

Let us consider the cc-pVDZ basis set for the ccECP pseudopotential of the Oxygen atom.
```
O 5 0
 S   9
      54.7752160 -0.0012444 1G
      25.6168010  0.0107330 1G
      11.9802450  0.0018889 1G
       6.9923170 -0.1742537 1G
       2.6202770  0.0017622 1G
       1.2254290  0.3161846 1G
       0.5777970  0.4512023 1G
       0.2680220  0.3121534 1G
       0.1253460  0.0511167 1G
 S   1
       0.2585510  1.0000000 1G
 P   9
      22.2172660  0.0104866 1G
      10.7475500  0.0366435 1G
       5.3157850  0.0803674 1G
       2.6607610  0.1627010 1G
       1.3318160  0.2377791 1G
       0.6786260  0.2811422 1G
       0.3336730  0.2643189 1G
       0.1670170  0.1466014 1G
       0.0835980  0.0458145 1G
 P   1
       0.2678650  1.0000000 1G
 D   1
       1.2327530  1.0000000 1G
```
The first line

```
O 5 0
```
contains the atom's name, the number of contracted orbitals in the basis set, and the number of contracted orbitals in the Jastrow basis set (which is initialized to zero in all basis set files).

Afterwards the contracted orbitals are listed in no particular order.
For each contracted orbital, the first line contains the angular momentum followed by the number of primitive functions in the contraction:
```
 S   9
```
afterwards the parameters of the contracted orbital are listed, and for each line
```
      54.7752160 -0.0012444 1G
      25.6168010  0.0107330 1G
          .           .     .
          .           .     .
          .           .     .
```
we have the exponent of the primitive orbital, the coefficient of the contraction, and the type of orbital. 
Here 1G indicates a Gaussian type orbital (GTO), 2G a GTO multiplied by the distance between the electron and the nucleus $re^{-Zr^2}$, and so on.

For the list of primitive types please check the manual.


### Pseudopotentials format.

Let us consider the ccECP pseudopotential for Oxygen
```
O 2 2
3 1
1 12.30997   6.00000
3 14.76962  73.85984
2 13.71419 -47.87600
2 13.65512  85.86406
```
In the first line we have
```
O 2 2
```
the name of the atom, the number of components in the pseudopotential and the number of core electrons that are substituted by the pseudopotential.

This is followed by a row with the number of entries
```
3 1
```
for each pseudopotential component, starting from the local term. 

Afterwards each term of the pseudopotential is listed without separations:
```
1 12.30997   6.00000
3 14.76962  73.85984
2 13.71419 -47.87600
2 13.65512  85.86406
```
On each line we have the exponent of the polynomial, the exponential factor and the coefficient of the expansion.

In this case the first three terms are associated to the local part of the pseudopotential, while the last row is related to the first non-local term.

### References

[^a]: From [Wikipedia](https://en.wikipedia.org/wiki/Mecha): *``In science fiction, mecha (Japanese: メカ, Hepburn: meka) or mechs are giant robots or machines, typically depicted as piloted, humanoid walking vehicles. The term was first used in Japanese after shortening the English loanword 'mechanism' (メカニズム, mekanizumu) or 'mechanical' (メカニカル, mekanikaru), but the meaning in Japanese is more inclusive, and 'robot' (ロボット, robotto) or 'giant robot' is the narrower term.''* 

[^1]: (a) M. Burkatzki, C. Filippi, M. Dolg *Energy-consistent pseudopotentials for QMC calculations.* [*J. Chem. Phys.* **126**, 234105 (2007)](https://doi.org/10.1063/1.2741534) (b) M. Burkatzki, C. Filippi, M. Dolg *Energy-consistent small-core pseudopotentials for 3d-transition metals adapted to quantum Monte Carlo calculations.* [*J. Chem. Phys.* **129**, 164115 (2008)](https://doi.org/10.1063/1.2987872) 

[^2]: (a) M. C. Bennett, C. A. Melton, A. Annaberdiyev, G. Wang, L. Shulenburger, L. Mitas *A new generation of effective core potentials for correlated calculations.* [*J. Chem. Phys.* **147 (22)**, 224106 (2017)](https://doi.org/10.1063/1.4995643) (b) M. C. Bennett, G. Wang, A. Annaberdiyev, C. A. Melton, L. Shulenburger, L. Mitas *A new generation of effective core potentials from correlated calculations: 2nd row elements.* [*J. Chem. Phys.* **149 (10)**, 104108 (2018)](https://doi.org/10.1063/1.5038135) (c) G. Wang, A. Annaberdiyev, C. A. Melton, M. C. Bennett, L. Shulenburger, L. Mitas *A new generation of effective core potentials from correlated calculations: 4s and 4p main group elements and first row additions.* [*J. Chem. Phys.* **151 (14)**, 144110 (2019)](https://doi.org/10.1063/1.5121006) (d) G. Wang, B. Kincaid, H. Wang, A. Annaberdiyev, M. C. Bennett, J. T. Krogel, L. Mitas *A new generation of effective core potentials from correlated and spin–orbit calculations: Selected heavy elements.* [*J. Chem. Phys.* **157 (5)**, 054101 (2022)](https://doi.org/10.1063/5.0087300) (e) H. Zhou, B. Kincaid, G. Wang, A. Annaberdiyev, P. Ganesh, L. Mitas *A new generation of effective core potentials: Selected lanthanides and heavy elements.* [*J. Chem. Phys.* **160 (8)**, 084302 (2024)](https://doi.org/10.1063/5.0180057)

[^3]: J. R. Trail, R. J. Needs *Shape and energy consistent pseudopotentials for correlated electron systems.* [*J. Chem. Phys.* **146 (20)**, 204107 (2017)](https://doi.org/10.1063/1.4984046)

