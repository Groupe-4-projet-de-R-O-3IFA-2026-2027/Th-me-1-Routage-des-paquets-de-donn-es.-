import heapq

# Les données du réseau : (capacité, délai)
reseau = {
    'A' : {'B': (8,2), 'C': (8,5)},
    'B' : {'D': (8,2)},
    'C' : {'D': (8,5)}
}

def dijkstra(depart, arrivee):
    # File de priorité : (délai_cumulé, noeud, chemin)
    file = [(0, depart, [depart])]
    visites= set()

    while file:
        delai, noeud, chemin = heapq.heappop(file)
        if noeud == arrivee:
            return chemin, delai
        if noeud not in visites:
            visites.add(noeud)
            for voisin, (cap, poids) in reseau[noeud].items():
                                               heapq.heappush(file, (delai + poids, voisin, chemin + [voisin]))

# ---Exécution---
chemin, latence = dijkstra('A', 'D')

#Calcul de la congestion U pour le lien le plus chargé (10 Mbps / 8 Mbps)
U=10 / 8

print(f"chemin : {' -> '.join(chemin)}")
print(f"latence : {latence}")
print(f"congestion U : {U}")
