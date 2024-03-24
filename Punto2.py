import math
def Volumen_y_Area (b : float, h : float, r : float) :
    AreaRec : float = b * a
    AreaCir : float = math.pi * r**2
    AreaTotal : float = 2 * AreaCir + AreaRec
    PerRec : float = 2 * (a + b)
    PerCir : float = 2 * math.pi * r
    PerTotal : float = PerRec + 2 * PerCir
    return ("El volument total es " + str(PerTotal) + " y el area total es " + str(AreaTotal) + ".")


if __name__ == "__main__":
    a : float = float(input("DIjite la altura del rectangulo (cm): "))
    b : float = float(input("DIjite la base del rectangulo (cm): "))
    c : float = float(input("DIjite el radio de la circunferencia (cm): "))

    Resultado : str = Volumen_y_Area(a,b,c)
    print(Resultado)