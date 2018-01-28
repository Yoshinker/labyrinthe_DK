def listeDouble(hor, col):
    """Permet de faire un tableau de tableaux (tableau double)"""
    
    malist = []
    i1 = 0
    i2 = 0
    while i1 < hor:
        malist.append([])
        i1 += 1
    i1 = 0
    while i1 < hor:
        malist[i1].append("")
        i2 += 1
        if len(malist[i1]) == col:
            i1 += 1
            i2 = 0
    return malist