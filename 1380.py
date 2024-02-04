# -*- coding: utf-8 -*-
# se partirmos de uma população inicial com apenas um indivíduo, no instante seguinte teremos ainda um 
#(ele atinge a maturidade para divisão), no seguinte teremos 2, no outro 3, então 5 e assim por diante.

PISANO = 1500
fibo = [0,1]

# computa o módulo da entrada em niveis diferentes de precisao
def fastmod(s):
    acc = 0
    for char in s:
        acc = (acc * 10 + int(char)) % 1500
    return acc

def fibOf(entrada):
    idx = 2

    if (entrada != 0) or (entrada != 1):
        while len(fibo) <= entrada:
            f = fibo[idx-1]  + fibo[idx-2]
            fibo.append(f % 1000)
            idx = idx + 1
    return fibo[entrada]

fibOf(PISANO)

T = int(input())

instances = []
while (len(instances) < T):
    #K = int(input())
    # num_bacilos = fibo[K%1500] 
    K = str(input())
    num_bacilos = fibo[fastmod(K)]
    instances.append(num_bacilos)

while (len(instances) > 0):
    k = instances.pop(0)
    print('{:0>3}'.format(k))