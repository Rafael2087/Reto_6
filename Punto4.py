def Cantidad (N : int , M : int , K : int, Plata : int):
    Panes : int = 300 * N
    Leche : int = 3300 * M
    Huevos : int = 350 * K
    Gastos : int = Panes + Leche + Huevos
    Vueltas : int = Plata - Gastos
    return Vueltas   

if __name__ == "__main__":
    a : int = int(input("Dijite la cantidad de plata que le dio su mamá: "))
    b : int = int(input("Dijite la cantidad de huevos: "))
    c : int = int(input("Dijite la cantidad de bolsas de leche: "))
    d : int = int(input("Dijite la cantidad de panes: "))

    if Cantidad(d,c,b,a) > 0 :
        print("Le debes devolver a tu mamá" + str(Cantidad(d,c,b,a))+ " pesos" )
    else:
        print("Falta plata para hacer las compras")
