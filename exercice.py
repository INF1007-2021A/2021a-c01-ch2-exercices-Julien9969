#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    #test
    # TODO completer la fonction ici
    nouveau_mot=str()
    
    for lettre in mot:
        lettre_maj=chr((ord(lettre)-32))
        nouveau_mot= nouveau_mot + lettre_maj
       # print(nouveau_mot)
    return print(nouveau_mot)

if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    
    for i in range(len(mots)):
        
        mots[i] = majuscule(mots[i])
       
    #print(mots)
