from exhaustif import detectGraph1 as exhaustif
from parcours import detectGraph2 as parcours
from label import detectGraph3 as label
from time import time

#

G0 = [[1],[2],[0]]
G1=[[1],[2],[4,5],[2],[],[3]]
G2 =[[1],[2],[3],[4],[5],[]]
G3 =[[1],[2],[3],[4],[5],[0]]
G4 = [[0]]

# Avec Cycle
G5 =[[4,5,9,8],[1,2],[6,4],[],[3,1,6],[5,3],[9,2],[2,5],[7,4,3],[3,7]]
G6 =[[4,5,9,2],[1,2],[6,7],[],[3,9,6],[9,3],[8,6],[2,5],[7,4,3],[3,8],[5,4,3,2,1]]
G7 =[[4,5,9,10],[1,2],[6,10],[],[3,9,6],[3,4],[11,10],[2,5],[7,4,3],[3,8],[5,4,3,2,1],[6,3,4,8]]
G8 =[[4,5,9,12],[1,2],[6,10],[],[3,9,6],[3,4],[11,12],[2,5],[7,4,3],[3,8],[5,4,3,2,1],[6,3,4,8],[12,8]]

# Sans Circuit

G9 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[]]

# Avec un long circuit

G10 = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[0]]

# Avec beaucoup d'arretes

G11 = [[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13],[0,1,2,3,4,5,6,7,8,9,10,11,12,13]]

def print_result(G,methode):
    t0 = time()
    if methode == 1:
        result = exhaustif(G)
        t1 = time()
        print("graphe : " + str(G))
        print("methode exhaustive")
        print(result)
        print("calcul en " + str(t1 - t0) + " secondes")
        print("")
    elif methode == 2:
        result = parcours(G)
        t1 = time()
        print("graphe : " + str(G))
        print("methode par parcours")
        print(result)
        print("calcul en " + str(t1 - t0) + " secondes")
        print("")
    elif methode == 3:
        result = label(G)
        t1 = time()
        print("graphe : " + str(G))
        print("methode par label")
        print(result)
        print("calcul en " + str(t1 - t0) + " secondes")
        print("")
    else:
        print("methode =")
        print("1 : methode exhaustive")
        print("2 : methode par parcours")
        print("3 : methode par label")
    return 0

# Temps d execution pour exhaustif


print_result(G0, 1)
print_result(G1, 1)
print_result(G2, 1)
print_result(G3, 1)
print_result(G4, 1)
print_result(G5, 1)
print_result(G6, 1)
print_result(G7, 1)
print_result(G8, 1)


# Temps d execution pour parcours

print_result(G1, 2)
print_result(G2, 2)
print_result(G3, 2)
print_result(G4, 2)
print_result(G5, 2)
print_result(G6, 2)
print_result(G7, 2)
print_result(G8, 2)
print_result(G9, 2)
print_result(G10, 2)
print_result(G11, 2)


# Temps d execution pour label

print_result(G1, 3)
print_result(G2, 3)
print_result(G3, 3)
print_result(G4, 3)
print_result(G5, 3)
print_result(G6, 3)
print_result(G7, 3)
print_result(G8, 3)
print_result(G9, 3)
print_result(G10, 3)
print_result(G11, 3)
