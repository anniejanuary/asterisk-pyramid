#left-aligned  

a=1

while a<=20:
    print("*"*a)
    a+=1 #numery linijek i o nie +1 pomnożymy kolejne gwiazdki w kolejnych linijkach
    
    
    
#center-aligned
    
def pyramid(rows=8):
    for i in range(rows):
        print(' '*(rows-i-1) + '*'*(2*i+1))

pyramid(8)
