#Variables and lists are icelandic names.
#kirni = nucleotide, is just a spin of the word kirni with drei as in the German 3 in front of it.
#keep in mind that the starting poing it always AUG, the program will print the rest of the translation from there.




kirni = str(input("Hvað á að skipta í búta: "))
x = 0
dreikirni_start = str()

for i in range(len(kirni)):
    if kirni[x] == "A" and kirni[x+1] == "U" and kirni[x+2] == "G" and x+2 <= len(kirni):
        dreikirni_start = kirni[x:len(kirni)] 
    else:
        x+=1
    print(dreikirni_start)
    
