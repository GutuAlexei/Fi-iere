with open('c:/Users/user/Desktop/bac.txt', 'rt')as f: 
    linii=list(f) 
n=media=0 
print('Nume   Prenume Nota ') 
for linie in linii: 
    campuri=linie.split()
    nota=int(campuri[2]) 
    n,media=n+1, media+nota 
    print(linie) 

print('Media celor ', n , 'Destepti din a 11 A este',media/float(n))