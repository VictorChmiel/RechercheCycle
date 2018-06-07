
# Methode du parcours en profondeur
G0 = [[1],[2],[0]]
G1=[[1],[2],[4,5],[2],[],[3]]
G2 =[[1],[2],[3],[4],[5],[]]
G3 =[[1],[2],[3],[4],[5],[0]]
G4 = [[0]]

def detectGraph2(G):
    n = len(G)
    file = []
    niveau = n*[None]
    k = 0
    while file == [] and k < n :
        if G[k] != []:
            file.append(k)
            niveau[k] = 0
        k += 1
    while file != []:
        u = file.pop(0)
        for v in G[u]:
            if niveau[v] == None:
                niveau[v] = niveau[u] + 1
                file.append(v)
            elif niveau[v] < niveau[u]:
                return True

    return False

# print(detectGraph2(G1))
# print(detectGraph2(G2))
# print(detectGraph2(G3))
# print(detectGraph2(G4))