def Interes (C : float, i : float, n : int):
    Porcentaje = i/100
    Total : float = C*(1 + Porcentaje)**(n)
    return Total

if __name__ == "__main__":
    a : float = float(input("Dijite el Capital Inicial: "))
    b : float = float(input("Dijite el interes en porcentaje (%): "))
    c : int = int(input("Dijite la cantidad de meses: "))
    print("El valor total a pagar es de " + str(Interes(a,b,c)) + "$")