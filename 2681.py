# -*- coding: utf-8 -*-
X = int(input())
minTime = pow(2, X, 60*60*24)-1

A = (minTime//60//60)%24
B = (minTime//60)%60
C = minTime%60

print("{:02d}:{:02d}:{:02d}".format(A,B,C))