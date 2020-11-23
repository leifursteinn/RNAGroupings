# RNAGroupings
These script(s) find the starting and stopping points of RNA Translation of nucleotides. 

## What exactly does it do?
Say you have the translated line of UACAUGUCAUAA.

### When completed these scripts should do these steps in this order;

- Find the starting point of the translation
  - always AUG
- Find the stopping point of the translation 
  - divisble by 3 as translation goes in groupings of 3.
  - always UAG, UAA or UGA

