# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 09:15:16 2023

@author: 52331
"""

import numpy as np
import os
import random

matriz=([["cristiano ronaldo","moreno","fuerte",33,"futbolista"],["messi","blanco","delgado",32,"futbolista"],["Leonardo di caprio","rubio","delgado",48,"actor"],["Rey misterio","moreno","fuerte",48,"luchador"],["jonhy depp","moreno","robusto",60,"actor"]])


print("Tienes que tratar de adivinar mi personaje, puedes hacer 2 preguntas relacionadas con lo siguiente:");
print("Aspecto:moreno,blanco,rubio");
print("edad: numero entero");
print("complexion: fuerte, delgada robusta");
print("ocupacion: actor, futbolista, luchador, etc........");
print("----------------------------------------------------------------------------------");
personajeasignado=matriz[random.randint(0, 4)];
for i in range (2):

    print("Digite el numero de  el dato que desea conocer del personaje: ");
    print("1----aspecto");
    print("2----complexion");
    print("3----edad");
    print("4----ocupacion");
    dato = input("")
    if(dato=="1"):
        print("aspecto : " , personajeasignado[1]);
    if(dato=="2"):
        print("complexion: ",personajeasignado[2]);
    if(dato=="3"):
        print("edad:  ", personajeasignado[3]);
    if(dato=="4"):
        print("ocupacion:  ", personajeasignado[4]);
        
print("--------------------------------------------------------------------------------");
print("ahora si , ¿cual es el nombre del personaje?");
print("");
dato1=input("");
if(dato1==personajeasignado[0]):
    print("su personaje es correcto");
else:
    print("Usted a fallado")
