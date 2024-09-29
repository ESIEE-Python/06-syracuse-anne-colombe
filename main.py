    ###Fonctions secondaires
'''On importe le module math pour utiliser inf'''
from math import inf
# imports
from plotly.graph_objects import Scatter, Figure
### NE PAS MODIFIER ###
def syr_plot(lsyr):
    '''Création du graphique de la suite de Syracuse'''
    title = "Syracuse" + " (n = " + str(lsyr[0]) + " )"
    fig = Figure({  'layout':   { 'title': {'text': title},
                                'xaxis': {'title': {'text':"x"}},
                                'yaxis': {'title': {'text':"y"}},
                                }
                }
    )

    x = list(range(len(lsyr)))
    t = Scatter(x=x, y=lsyr, mode="lines+markers", marker_color = "blue")
    fig.add_trace(t)
    fig.show()
    # fig.write_html('fig.html', include_plotlyjs='cdn')

#######################

def syracuse_l(n: int) -> list:
    """retourne la suite de syracuse"""
    l = []
    while n != 1:
        l.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    l.append(1)
    return l


def temps_de_vol(l: list) -> int:
    """retourne le temps de vol d'une suite de syracuse
    """
    k = inf
    for e in l :
        if e == 1 and l.index(e) < k :
            k = l.index(e) + 1
    return k

def temps_de_vol_en_altitude(l: list) -> int:
    """retourne le temps de vol en altitude
    """
    k = inf
    for e in l :
        if e < l[0] and l.index(e) < k :
            k = l.index(e)
    return k

def altitude_maximale(l: list) -> int:
    """retourne l'altitude maximale 
    """
    return max(l)


    #Fonction pricipale

def main():
    '''Utilise les fonctions secondaires pour les différents
    éléments de la suite de Syracuse'''
    lsyr = syracuse_l(6)
    syr_plot(lsyr)
    print(syracuse_l(6))
    print(temps_de_vol(lsyr))
    print(temps_de_vol_en_altitude(lsyr))
    print(altitude_maximale(lsyr))

if __name__ == "__main__":
    main()
