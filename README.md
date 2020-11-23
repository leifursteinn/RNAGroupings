# RNAGroupings
These script(s) find the starting and stopping points of RNA Translation of nucleotides. 

## What exactly does it do?
Say you have the translated line of UACAUGUCAUAA.

The program does exactly this:

- Find the starting point of the translation
  - always AUG
- Find the stopping point of the translation 
  - divisble by 3 as translation goes in groupings of 3.
  - always UAG, UAA or UGA
  
 ### What does it return?

It returns a list of the actual translation process from AUG to either UAA, UAG or UGA.
The first three letters are the starting point and the last 3 the ending point.

So from: UACAUGUCAUA we get: AUGUCAUAA

