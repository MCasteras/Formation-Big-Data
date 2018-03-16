def bisextile(annee) :
    if annee%400 == 0 :
        return True
    elif annee%100 == 0 :
        return False
    elif annee%4 == 0 :
        return True
    else : return False