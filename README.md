
```
    _______   _______         _______  _                    
   (_______) (_______)       (_______)| |                   
    _    _    _  _  _  _____  _       | |__   _____         
   | |  | |  | ||_|| || ___ || |      |  _ \ (____ |        
   | |__| |_ | |   | || ____|| |_____ | | | |/ ___ |        
   \________)|_|   |_||_____)\_______)|_| |_|\_____|        
                                                    
   Matteo Barborini (matteo.barborini@gmail.com)
```

### Basis sets and the pseudopotentials in QMeCha format.

The organization of the files is discussed in depth in the manual. Here we briefly recall the basic aspects.

### Basis sets format.

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

Aterwards the contracted orbitals are listed in no particular order.
For each contracted orbital, the first line contains the angular momentum followed by the number of primitive functions in the contraction:
```
 S   9
```
afterwords the parameters of the contracted orbital are listed, and for each line
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
On each line we have the exponent of the polinomial, the exponential factor and the coefficient of the expansion.

In this case the first three terms are associated to the local part of the pseudopotential, while the last row is related to the first non-local term.