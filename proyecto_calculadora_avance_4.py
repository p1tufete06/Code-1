def peso_mexicano_a_dolar_canadiense(pesos):
    return pesos * 0.073

def peso_mexicano_a_dolar_americano(pesos):
    return pesos * 0.056

def peso_mexicano_a_euro(pesos):
    return pesos * 0.051

def peso_mexicano_a_yen(pesos):
    return pesos * 8.45

def peso_mexicano_a_libra_esterlina(pesos):
    return pesos * 0.044

def peso_mexicano_a_franco_suizo(pesos):
    return pesos * 0.049

def peso_mexicano_a_peso_argentino(pesos):
    return pesos * 56.78

def peso_mexicano_a_real_brasileno(pesos):
    return pesos * 0.28

def peso_mexicano_a_peso_colombiano(pesos):
    return pesos * 245.67

def peso_mexicano_a_sol_peruano(pesos):
    return pesos * 0.21

def dolar_americano_a_peso_mexicano(dolares):
    return dolares * 17.85

def dolar_canadiense_a_peso_mexicano(dolares_can):
    return dolares_can * 13.68

def euro_a_peso_mexicano(euros):
    return euros * 19.45

def yen_a_peso_mexicano(yenes):
    return yenes * 0.118

def libra_esterlina_a_peso_mexicano(libras):
    return libras * 22.73

def franco_suizo_a_peso_mexicano(francos):
    return francos * 20.41

def peso_argentino_a_peso_mexicano(pesos_arg):
    return pesos_arg * 0.0176

def real_brasileno_a_peso_mexicano(reales):
    return reales * 3.57

def peso_colombiano_a_peso_mexicano(pesos_col):
    return pesos_col * 0.00407

def sol_peruano_a_peso_mexicano(soles):
    return soles * 4.76

def mostrar_menu_monedas():
    print("CALCULADORA DE CONVERSIONES\nDE MONEDA\n")
    print("DESDE PESO MEXICANO:\n") 
    print("1.  Peso Mexicano ~ Dólar Canadiense")
    print("2.  Peso Mexicano ~ Dólar Americano")
    print("3.  Peso Mexicano ~ Euro")
    print("4.  Peso Mexicano ~ Yen Japonés")
    print("5.  Peso Mexicano ~ Libra Esterlina")
    print("6.  Peso Mexicano ~ Franco Suizo")
    print("7.  Peso Mexicano ~ Peso Argentino")
    print("8.  Peso Mexicano ~ Real Brasileño")
    print("9.  Peso Mexicano ~ Peso Colombiano")
    print("10. Peso Mexicano ~ Sol Peruano\n")

mostrar_menu_monedas()

def main():
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_dolar_canadiense(pesos)
        print(f"{pesos} MXN = {resultado:.2f} CAD")
    elif opcion == 2:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_dolar_americano(pesos)
        print(f"{pesos} MXN = {resultado:.2f} USD")
    elif opcion == 3:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_euro(pesos)
        print(f"{pesos} MXN = {resultado:.2f} EUR")
    elif opcion == 4:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_yen(pesos)
        print(f"{pesos} MXN = {resultado:.2f} JPY")
    elif opcion == 5:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_libra_esterlina(pesos)
        print(f"{pesos} MXN = {resultado:.2f} GBP")
    elif opcion == 6:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_franco_suizo(pesos)
        print(f"{pesos} MXN = {resultado:.2f} CHF")
    elif opcion == 7:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_peso_argentino(pesos)
        print(f"{pesos} MXN = {resultado:.2f} ARS")
    elif opcion == 8:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_real_brasileno(pesos)
        print(f"{pesos} MXN = {resultado:.2f} BRL")
    elif opcion == 9:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_peso_colombiano(pesos)
        print(f"{pesos} MXN = {resultado:.2f} COP")
    elif opcion == 10:
        pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
        resultado = peso_mexicano_a_sol_peruano(pesos)
        print(f"{pesos} MXN = {resultado:.2f} PEN")
    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


