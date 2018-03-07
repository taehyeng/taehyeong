# -*- coding: cp949 -*-
#-*- cording: utf-8 -*-
def yoonnun(num):
    if (num % 4 == 0) & (num % 100 == 0) & (num % 400 == 0) :
        out = u"윤년"    
    elif (num % 4 == 0) & (num % 100 == 0):
        out = u"평년"
    elif (num % 4 == 0) :
        out = u"윤년"
    else:
        out = u"몰라"
        
    return out
