def Contagiados(C : int, D : int):
    Total : int = C * 2 ** D
    return Total
if __name__ == "__main__":
    a : int = int(input("Dijite el número inicial de contagiados: "))
    b : int = int(input("Dijite la cantidad de días: "))
    print("El número de contagiados hasta la fecha es de " + str(Contagiados(a,b)))