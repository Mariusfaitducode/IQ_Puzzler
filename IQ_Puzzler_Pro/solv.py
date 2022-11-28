from resolution import *

def isolated(grid): #Forme la liste des groupes de cases vides
    gridtmp = grid
    list = []
    listtmp = []
    
    while is_empty(gridtmp)!=[]:

        listtmp=[]
        l,c =is_empty(gridtmp)
        gridtmp[l][c]=-9
        listtmp.append((l,c))

        for i in range(0,NB_COLUMN*NB_LINE):

            emptynearcase(gridtmp,listtmp,i)

        #print(listtmp)
        listtmp.sort()
        #print(listtmp)

        list.append(listtmp)

    print(list)

    return list


def emptynearcase(gridtmp,ltmp,i): #Renvoie les cases vides cote à cote d'une case donnée

    if i<len(ltmp):

        line,column=ltmp[i]

        for d in range(-1,2,2):

            if 0<=line+d<NB_LINE and 0<=column<NB_COLUMN and gridtmp[line+d][column] == VIDE :# vérifie l'existence puis la validité de la case

                gridtmp[line+d][column]=-9
                ltmp.append((line+d,column))

            if 0<=line<NB_LINE and 0<=column+d<NB_COLUMN and gridtmp[line][column+d]==VIDE:

                gridtmp[line][column+d]=-9
                ltmp.append((line,column+d))

        return ltmp



def is_empty(gridtmp):  #renvoie la prochaine case vide dans la liste

    for l in range(NB_LINE):

        for c in range(NB_COLUMN) :

            if gridtmp[l][c]==VIDE :

                return((l,c))

    #print("Sortie")
    return []

