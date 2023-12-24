from os import write
import random
import csv 

client = {}
Compte = {}
clientCompte = {}

def ajouter(numCl,MPC,numC,soldeC):
    client[numCl]= MPC
    client[numCl]= numC
    client[numCl]= soldeC



def ModifierMPC(numCl,MPC,NewMP):
    if Compte[clientCompte[numCl]] == MPC:
        client[numCl] = NewMP
    else:
        print("impossible modifier mot paase de copmte")
    
def Deposer(numCl,SommeArgent):
    Compte[clientCompte[numCl]] += SommeArgent

def retirer(numCl,SommeArgent):
   if Compte[clientCompte[numCl]] < SommeArgent:
       print("impossible d'effectuer l'opération , solde insuffisant")
   else:
       Compte[clientCompte[numCl]] -= SommeArgent

GenererNumCopmte = lambda numCl : int(numCl + random.randint(0,100))

def EcrirefichierCSV():
    with open("Client.csv","w") as fichier:
        enregistrer = ['numclient','code secrets']
        write = csv.DictWriter(fichier,enregistrer=enregistrer)


