#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 12:16:35 2020

@author: bernardintheo
"""

class ConvertisseurBinaire:
    
    
    def convertEnBinaire(self,contenu,tableBinaire):
        contenuBinaire = ""
        for i in contenu:
            contenuBinaire = contenuBinaire + tableBinaire[i]
        return contenuBinaire
    
    
    def addBitManquant(self,contenu):
        while len(contenu)%8 != 0:
            contenu = contenu+"0"
            

    def get8pack(self,contenu):
        listeBin = []
        for i in range(8,len(contenu),8):
            listeBin.append(contenu[i-8:i])
        return listeBin
            
    def ecrireBinaireFichier(self,fileName,contenu):
        with open(fileName, "wb") as f:
            for octet in contenu:
                f.write((int(octet, base=2)).to_bytes((len(octet)//8), byteorder='big')) 
        f.close()
        
        
    
    def ecrireValBinaire(self,alphabet,tableBinaire,nomFic):
        with open(nomFic[:-4]+'_valCharBin.txt','a') as f:
            for i in alphabet:
                f.write(i+" : "+str(tableBinaire[i])+'\n')
            f.close()