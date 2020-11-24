#Variables and lists are icelandic names.
#kirni = nucleotide, is just a spin of the word kirni with drei as in the German 3 in front of it.
#keep in mind that the starting poing is always AUG, the program will print the rest of the translation from there.




kirni = str(input("Hvað á að skipta í búta: "))
x = 0
dreikirni_start = str()
dreikirni_end = str()
dreikirni = str()

for i in range(len(kirni)):
    if kirni[x] == "A" and kirni[x+1] == "U" and kirni[x+2] == "G" and x+2 <= len(kirni):
        dreikirni_start = kirni[x:len(kirni)] 
    else:
        x+=1


y = 3
z = int(len(dreikirni_start)) - int(len(dreikirni_start) % 3)

for i in range(int(z/3)):
    if dreikirni_start[y] == "U":
        if dreikirni_start[y+1] == "A" and dreikirni_start[y+2] == "G": 
            dreikirni = dreikirni_start[0:y+3]
        elif dreikirni_start[y+1] == "A" and dreikirni_start[y+2] == "A":
            dreikirni = dreikirni_start[0:y+3]
        elif dreikirni_start[y+1] == "G" and dreikirni_start[y+2] == "A":
            dreikirni = dreikirni_start[0:y+3]
        else:
            y+=3
    else: 
        y+=3
print(dreikirni)


    
