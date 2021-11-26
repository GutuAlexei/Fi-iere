vocale='aAeEiIoOuU'
x=0
with open ('c:/Users/user/Desktop/Text1.txt' , 'r') as f:
    v=f.read()
with open ('Text2.txt', 'w') as f:
    for i in v:
        if i in vocale:
            f.write(i)
            x+=1
print('Vocalele sunt',x)