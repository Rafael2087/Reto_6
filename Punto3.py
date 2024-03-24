def Cantidad (N : float , M : float , K : float):
    Gallina : float = 6*N
    Gallos : float = 7*M
    Pollitos : float = K

    return ("la cantidad de carne de aves en kilos que se tiene son: "+str(Gallina)+" de gallina, "+str(Gallos)+" de gallo, "+str(Pollitos)+" de pollito.")

if __name__ == "__main__":
    a : int = int(input("Dijite la cantidad de Gallinas: "))
    b : int = int(input("Dijite la cantidad de Gallos: "))
    c : int = int(input("Dijite la cantidad de Pollitos: "))

    print(Cantidad(a,b,c))