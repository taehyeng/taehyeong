# -*- coding: cp949 -*-
#-*- cording: utf-8 -*-
def yoonnun(num):
    if (num % 4 == 0) & (num % 100 == 0) & (num % 400 == 0) :
        out = u"����"    
    elif (num % 4 == 0) & (num % 100 == 0):
        out = u"���"
    elif (num % 4 == 0) :
        out = u"����"
    else:
        out = u"����"
        
    return out
