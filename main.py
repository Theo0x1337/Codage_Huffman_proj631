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
    
    
    nomFic = input('Entrez le chemin du fichier texte que vous voulez compresser : ')
    traitFic = TraitementFichier()
    alphaEtFreq = traitFic.getAlphabetEtFreq(nomFic)
    
    listeFreq = alphaEtFreq[1]
    listeAlphabet = alphaEtFreq[0]
    
    dictioAlphaFreq = traitFic.dictioAlphabetFreq(listeFreq,listeAlphabet)
    dictioFreqPuisASCII = traitFic.triDictioParFreqPuisASCII(dictioAlphaFreq)
    
    
    tailleAlphabet = len(listeAlphabet)
    
    listeFreq = []
    listeAlphabet = []
    
    traitFic.ecrireFreqDansFichier("Taille de l'alphabet : "+ str(tailleAlphabet),None,nomFic);
    for couple in dictioFreqPuisASCII:
        traitFic.ecrireFreqDansFichier(couple[0],couple[1],nomFic)
        listeFreq.append(couple[1])
        listeAlphabet.append(couple[0])
    
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
    
    contenu = traitFic.getContenuFichier(nomFic)
    
    
    listeBin = convBin.convertEnBinaire(contenu,tableBin)
    
    
    convBin.addBitManquant(listeBin)
        
    listeBin8 = convBin.get8pack(listeBin)

            
    convBin.ecrireBinaireFichier(nomFic[:-3]+'bin',listeBin8)
    
    size_final=(os.path.getsize(nomFic[:-3]+'bin'))
    size_initial=(os.path.getsize(nomFic))

    #calcul du taux de compression :
    taux_de_compression=1-(size_final/size_initial)

    #affichage : 
    print("Le taux de compression pour "+ nomFic+" est de "+str(round(taux_de_compression,2)*100)+"%")


    #definition variable :
    total = 0 

    #calcul de la moyene de bits d'un caractère :
    for i in range(0,len(listeAlphabet)):
        total = total + len(tableBin[listeAlphabet[i]])*listeFreq[i]
    nb_moy_bits=round(total/sum(listeFreq),2)

    #affichage : 
    print("Le nombre moyen de bits pour un caractère du fichier"+ nomFic +" est de "+str(nb_moy_bits))