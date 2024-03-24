import math
def Volumen_y_Area (r1 : float, r2 : float, h : float) :
    
    VolumenEsfera : float = (4/3)*math.pi*(r1)**3
    VolumenCono : float = math.pi*(r2)**2*h/3
    VolumenTotal : float = VolumenEsfera + VolumenCono
    AreaEsfera : float = 4*math.pi*(r1)**2
    AreaCono : float = math.pi*(r2**2 + h**2)
    AreaTotal : float = AreaEsfera + AreaCono
    return ("El volument total es " + str(VolumenTotal) + " y el area total es " + str(AreaTotal) + ".")


if __name__ == "__main__":
    a : float = float(input("DIjite el radio de la Esfera (cm): "))
    b : float = float(input("DIjite el radio del Cono (cm): "))
    c : float = float(input("DIjite la altura del Cono (cm): "))

    Resultado : str = Volumen_y_Area(a,b,c)
    print(Resultado)