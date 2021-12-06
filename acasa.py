with open('c:/Users/user/Desktop/bac.txt', 'rt')as f: 
    lista=f.readline()
for linie in lista: 
    listaengleza=linie.split()
    if listaengleza[3]=='engleza':
        with open ('c:/Users/user/Desktop/listaengleza.txt', 'a')as f: 
            z=listaengleza[0]+''+listaengleza[1]+'/n'
    else:
        with open ('c:/Users/user/Desktop/listagermana.txt', 'a')as f: 
            z=listaengleza[0]+''+listaengleza[1]+'/n'