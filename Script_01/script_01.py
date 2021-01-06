def main():
    aumento = float(input("Escriba el valor de aumento: "))
    
    while aumento <= 0:
        aumento = float(input("El aumento debe ser mayor que 0. Intentelo de nuevo: "))

    numero_initial = float(input("numero inicial?: "))
    while numero_initial <= 0:
        numero_initial = float(input("El numero debe ser mayor que 0. Intentelo de nuevo: "))

    numero_final = float(input("un numero final?: "))
    while numero_final <= 0:
        numero_final = float(input("El numero debe ser mayor que 0. Intentelo de nuevo: "))

    acumulador = numero_initial 
    while  acumulador <= numero_final :
        print(acumulador)
        acumulador = acumulador + aumento
         

if __name__ == "__main__":
    main()
