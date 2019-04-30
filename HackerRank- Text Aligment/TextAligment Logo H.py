# srednyaya polosa 25 esli sivra budet 5
import math
width = 20
C = '*'
b = 1
dl = int(input())
# dl = 9# dlina bukvi
ss = dl*dl
mmm = math.ceil(dl/2) # vidayet srednyee kol stolbikov
b1 = dl*2-1

for i in range(dl):
    h = '*'*b
    print(h.center(dl*2))
    b = b+2

for i in range(dl+1):
    C = '*'*dl
    print(C.center(dl*2),''.center(dl*2-2),C.center(dl*2))

for i in range(mmm):
    C = '*'*(dl*5)
    print(C.center(dl*6))
for i in range(dl+1):
    C = '*'*dl
    print(C.center(dl*2),''.center(dl*2-2),C.center(dl*2))

#Bottom Cone
for i in range(dl):
    h1 = '*'*b1
    print(''.ljust(dl*4-1),h1.center(dl*2))
    b1 = b1-2

#polnaya dline 7go chisla eto 41
#polnaya dlina 5go chisla eto 29
