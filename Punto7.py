def Promedio (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    Suma : float = num_uno + num_dos + num_tres + num_cuatro + num_cinco
    Med : float = Suma/5
    return Med
def Ascendente (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno 
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro :
        num_tres , num_cuatro = num_cuatro, num_tres
    if num_cuatro > num_cinco :
        num_cuatro , num_cinco = num_cinco , num_cuatro
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro:
        num_tres, num_cuatro = num_cuatro , num_tres
    if num_uno > num_dos :
        num_uno, num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    return ("Los numeros en forma ascendente son: " + str(num_uno) + ", " + str(num_dos) + ", " + str(num_tres) + ", "  + str(num_cuatro) + ", "  + str(num_cinco))
    
def Descendente (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    if num_uno < num_dos :
        num_uno , num_dos = num_dos , num_uno 
    if num_dos < num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres < num_cuatro :
        num_tres , num_cuatro = num_cuatro, num_tres
    if num_cuatro < num_cinco :
        num_cuatro , num_cinco = num_cinco , num_cuatro
    if num_uno < num_dos :
        num_uno , num_dos = num_dos , num_uno
    if num_dos < num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres < num_cuatro:
        num_tres, num_cuatro = num_cuatro , num_tres
    if num_uno < num_dos :
        num_uno, num_dos = num_dos , num_uno
    if num_dos < num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_uno < num_dos :
        num_uno , num_dos = num_dos , num_uno
    return ("Los numeros en forma descendente son: " + str(num_uno) + ", " + str(num_dos) + ", " + str(num_tres) + ", "  + str(num_cuatro) + ", "  + str(num_cinco))    

def Mediana (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno 
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro :
        num_tres , num_cuatro = num_cuatro, num_tres
    if num_cuatro > num_cinco :
        num_cuatro , num_cinco = num_cinco , num_cuatro
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro:
        num_tres, num_cuatro = num_cuatro , num_tres
    if num_uno > num_dos :
        num_uno, num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    Med : int = num_tres

    return Med

def PromMul (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    
    Prom : float = (num_uno * num_dos * num_tres * num_cuatro * num_cinco)**(1/5)

    return Prom

def Potencia (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno 
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro :
        num_tres , num_cuatro = num_cuatro, num_tres
    if num_cuatro > num_cinco :
        num_cuatro , num_cinco = num_cinco , num_cuatro
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro:
        num_tres, num_cuatro = num_cuatro , num_tres
    if num_uno > num_dos :
        num_uno, num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    
    Pot : float = num_cinco ** num_uno
    return Pot

def Raiz (num_uno : float, num_dos : float, num_tres : float , num_cuatro : float , num_cinco : float):
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno 
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro :
        num_tres , num_cuatro = num_cuatro, num_tres
    if num_cuatro > num_cinco :
        num_cuatro , num_cinco = num_cinco , num_cuatro
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_tres > num_cuatro:
        num_tres, num_cuatro = num_cuatro , num_tres
    if num_uno > num_dos :
        num_uno, num_dos = num_dos , num_uno
    if num_dos > num_tres :
        num_dos , num_tres = num_tres , num_dos
    if num_uno > num_dos :
        num_uno , num_dos = num_dos , num_uno

    Rai : float = (num_uno)**(1/3)

if __name__ == "__main__":
    a : float = float(input("Dijite un número: "))
    b : float = float(input("Dijite un número: "))
    c : float = float(input("Dijite un número: "))
    d : float = float(input("Dijite un número: "))
    e : float = float(input("Dijite un número: "))  
    print("El promedio es: " + str(Promedio(a,b,c,d,e)))
    print("La mediana es: " + str(Mediana(a,b,c,d,e)))
    print(Ascendente(a,b,c,d,e))
    print(Descendente(a,b,c,d,e))
    print("El promedio multiplicativo es: " + str(PromMul(a,b,c,d,e)))
    print("El número más grande elevado al más pequeño es igual a: " + str(Potencia(a,b,c,d,e)))
    print("La raiz cubica del número más pequeño es: " + str(Raiz(a,b,c,d,e)))


