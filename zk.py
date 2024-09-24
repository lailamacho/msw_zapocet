from typing import List

m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

def det(a):
    a.append(a[0])
    a.append(a[1])

    leva_strana = 0
    for i in range(0, len(a)-2):
        y = 1     
        for j in range(0, len(a)-2):    
            y *= a[i+j][j]      
        leva_strana += y

    prava_strana = 0
    for i in range(0, len(a)-2):
        y = 1
        z = 0
        for j in range(2, -1, -1):  
            y *= a[i+z][j]  
            z += 1        
        z += 1
        prava_strana += y  

    return (leva_strana - prava_strana)

print(det(m))