#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 08:46:08 2020

@author: bernardintheo
"""

class TraitementFichier():
    
    
    def getContenuFichier(self,cheminFichier):
        return open(cheminFichier).read()
    
    
    def getAlphabetEtFreq(self,cheminFichier):
        
        contenu = self.getContenuFichier(cheminFichier)
        alphabet = []
        frequence = []
        for i in range(0,len(contenu)):
            if contenu[i] not in alphabet:
                alphabet.append(contenu[i])
                frequence.append(1)
            else:
                rang = alphabet.index(contenu[i])
                frequence[rang] = frequence[rang]+1
        return alphabet, frequence
    
    
    def dictioAlphabetFreq(self,alphabet,freq):
        dictio = dict()
        for i in range(0,len(alphabet)):
            dictio[alphabet[i]] = freq[i]
        return dictio
    
    
    def triDictioByFreq(self,dictio):
        dictioTriFreq = {k: v for k, v in sorted(dictio.items(), key=lambda item: item[1])}
        return dictioTriFreq
    
    
    def triDictioASCII(self,dictio):
        dictioASCII = dict()
        for i in sorted(dictio.keys()):
            dictioASCII[i] = dictio[i]
        return dictioASCII
    
    def triDictioParFreqPuisASCII(self,dictio):
        return sorted(dictio.items(), key=lambda x: (x[1],x[0]))
    
    
traitFic = TraitementFichier()
alphaEtFreq = traitFic.getAlphabetEtFreq('donnees/alice.txt')
print("L'alphabet de ce texte est : ")
print(alphaEtFreq[0])
print("La frequence de ce texte est : ")
print(alphaEtFreq[1])
print("-------")
dictio = traitFic.dictioAlphabetFreq(alphaEtFreq[0],alphaEtFreq[1])

print("Voici l'alphabet trié par freq puis par ascii : ")
print(traitFic.triDictioParFreqPuisASCII(dictio))

    
    
    