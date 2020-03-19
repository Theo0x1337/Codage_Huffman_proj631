#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:33:59 2020

@author: bernardintheo
"""
import os
from TraitementFichier import TraitementFichier
from arbreHuffman import arbreHuffman
from ConvertisseurBinaire import ConvertisseurBinaire

class main:
    
    traitFic = TraitementFichier()
    alphaEtFreq = traitFic.getAlphabetEtFreq('donnees/alice.txt')
    
    listeFreq = alphaEtFreq[1]
    listeAlphabet = alphaEtFreq[0]
    
    liste_arbre=[]
    for i in range(0,len(listeFreq)):
        liste_arbre.append(arbreHuffman(listeFreq[i],listeAlphabet[i]))
        
    while(len(liste_arbre)>1):
        min1=min(liste_arbre)
        liste_arbre.remove(min1)
        min2=min(liste_arbre)
        liste_arbre.remove(min2)
        liste_arbre.append(arbreHuffman(min1.freq+min2.freq,"",min1,min2))
    
    #Quand notre arbre est fini la racine est le premier (et unique) élément de notre liste d'arbre
    racine = liste_arbre[0]
    
    tableBin = racine.parcourir()
    
    convBin = ConvertisseurBinaire()
    
    contenu = traitFic.getContenuFichier('donnees/extraitalice.txt')
    
    
    listeBin = convBin.convertEnBinaire(contenu,tableBin)
    
    convBin.addBitManquant(listeBin)
    
    listeBin8 = convBin.get8pack(listeBin)

            
    convBin.ecrireBinaireFichier('donnees/extraitalice.bin',listeBin8)
    
    size_final=(os.path.getsize("donnees/extraitalice.bin"))
    size_initial=(os.path.getsize('donnees/extraitalice.txt'))

    #calcul du taux de compression :
    taux_de_compression=1-(size_final/size_initial)

    #affichage : 
    print("Le taux de compression pour extraitalice.txt est de :"+str(taux_de_compression))


    #definition variable :
    total = 0 

    #calcul de la moyene de bits d'un caractère :
    for i in range(0,len(listeAlphabet)):
        total = total + len(tableBin[listeAlphabet[i]])*listeFreq[i]
    nb_moy_bits=total/sum(listeFreq)

    #affichage : 
    print("Le nombre moyen de bits pour un caractère pour extraitAlice est de : "+str(nb_moy_bits))