def tex(num, money, children):
    if (num < 66) & (num > 15) :
        if 20000 < money :
            if children == "children":
                tax = money*0.5*0.9
            else:
                tax = money*0.2*0.9
        else:
            if children == "children":
                tax = money*0.5
            else:
                tax = money*0.2
    else:
        tax = 0
        
    return int(tax)
