with open("c:/Users/user/Desktop/bac.txt", "r")as f:
    lista = []
    note=[]
    m=[]
    z=[]
    bac = f.readlines()
    for i in bac:
        lista.append(i[0:-1])
print("Nume", "Prenume", "Nota")
for i in lista:
    print(i)
    for o in i.split():
        if o.isdigit():
            note.append(int(o))
print("Nota medie a clasei este: ", sum(note)/len(note))
with open("Germana.txt", "w") as f:
    s=0
    f.write("Nume "+"Prenume "+ "Nota "+"\n")
    for i in lista:
        if i[-7::]=="germana":
            f.write(str(i)+"\n")
            for n in i.split():
                if n.isdigit():
                    z.append(int(n))
    f.write("Germana: "+ str(round(sum(z)/len(z))))
with open("Engleza.txt", "w") as f:
    s=0 
    f.write("Nume "+"Prenume "+ "Nota "+"\n")
    for i in lista:
        if i[-7::]=="engleza":    
            f.write(str(i)+"\n")
            for p in i.split():
                if p.isdigit():
                    m.append(int(p))
    f.write("Engleza: " + str(round(sum(m)/len(m))))
                                    



