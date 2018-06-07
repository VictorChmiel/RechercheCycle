G0 = [[1],[2],[0]]
G1=[[1],[2],[4,5],[2],[],[3]]
G2 =[[1],[2],[3],[4],[5],[]]
G3 =[[1],[2],[3],[4],[5],[0]]
G4 = [[0]]


#on utilise les listes d'adjacence

def detectGraph3(G):
    n = len(G)
    label = n*[0]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if(G[i].count(j) == 1):
                    if label[i] >= label[j]:
                        label[j] = label[i] +1
    isCycle = False
    for k in range(n):
        if label[k] >= n:
            isCycle = True
    return isCycle

# print(detectGraph3(G))
# print(detectGraph3(G2))
# print(detectGraph3(G3))
# print(detectGraph3(G4))
























