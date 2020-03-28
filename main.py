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
    
    try:
        nomFic = input('Entrez le chemin du fichier texte que vous voulez compresser : \n')
        alphaEtFreq = traitFic.getAlphabetEtFreq(nomFic)
    except FileNotFoundError:
        print("")
        nomFic = input('Erreur le fichier saisi n existe pas ou vous vous êtes trompé dans la saisie, recommencez svp : \n')
        alphaEtFreq = traitFic.getAlphabetEtFreq(nomFic)
    
    listeFreq = alphaEtFreq[1]
    listeAlphabet = alphaEtFreq[0]
    
    alpha = listeAlphabet
    
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
    
    convBin.ecrireValBinaire(alpha,tableBin,nomFic)
    
    contenu = traitFic.getContenuFichier(nomFic)
    
    
    listeBin = convBin.convertEnBinaire(contenu,tableBin)
    
    
    convBin.addBitManquant(listeBin)
            
    listeBin8 = convBin.get8pack(listeBin)

            
    convBin.ecrireBinaireFichier(nomFic[:-4]+'_comp.bin',listeBin8)
    
    tailleDepart = (os.path.getsize(nomFic[:-4]+'_comp.bin'))
    tailleArrivee = (os.path.getsize(nomFic))

    #calcul du taux de compression :
    taux_de_compression=1-(tailleDepart/tailleArrivee)

    print("\n Le taux de compression pour "+ nomFic+" est de "+str(round(taux_de_compression,2)*100)+"%")


    charTot = 0 
    
    #pour chaque char de l'alphabet on multiplie le nombre de bits sur lequel il est codé par le nombre de fois qu'il apparait
    for i in range(0,len(listeAlphabet)):
        charTot = charTot + len(tableBin[listeAlphabet[i]])*listeFreq[i]
    nb_moy_bits=round(charTot/sum(listeFreq),2)

    print("\n Le nombre moyen de bits pour un caractère du fichier "+ nomFic +" est de "+str(nb_moy_bits))