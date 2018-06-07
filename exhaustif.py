from copy import deepcopy

# Methode d'enumeration de tous les sous-graphes
G0 = [[1],[2],[0]]
G1=[[1],[2],[4,5],[2],[],[3]]
G2 =[[1],[2],[3],[4],[5],[]]
G3 =[[1],[2],[3],[4],[5],[0]]
G4 = [[0]]

#on utilise les listes d'adjacence


def inListe(L,G):
    # return true if G is in L , return false otherwise

    for sG in L:
        if sG == G :
            return True
    return False


def subGraph(G):
    L = []
    L.append(G)
    current = list(L)
    # print("current = " + str(current))
    n = len(G)
    if n <= 1:
        return current
    else:
        for k in range(n-1) :
            temp = []
            for sG in current :
                for j in range(len(sG)) :
                    temp2=deepcopy(sG)
                    temp2[j]=[]
                    for p in range(len(sG)):
                        while(temp2[p].count(j) > 0):
                            temp2[p].pop(temp2[p].index(j))
                    if not inListe(L, temp2):
                        temp.append(temp2)
                        L.append(temp2)
            current = list(temp)
    return L


def nombre_Arretes(G):
    s = 0
    for list_vois in G:
        s += len(list_vois)
    return s

def nombre_Sommets(G):
    som = []
    for k in range(len(G)):
        if G[k] != []:
            if som.count(k) == 0:
                som.append(k)
            for ele in G[k]:
                if som.count(ele) == 0 :
                    som.append(ele)
    return(len(som))

def detectGraph1(G):
    subG = subGraph(G)
    for Graph in subG:
        if nombre_Arretes(Graph) >= nombre_Sommets(Graph) and nombre_Sommets(Graph) != 0:
            return True
    return False

#print(detectGraph1(G1))
#print(detectGraph1(G2))
#print(detectGraph1(G3))
#print(detectGraph1(G4))


