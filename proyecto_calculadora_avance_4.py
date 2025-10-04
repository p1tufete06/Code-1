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
    opciones = [
        "Peso Mexicano → Dólar Canadiense",
        "Peso Mexicano → Dólar Americano",
        "Peso Mexicano → Euro",
        "Peso Mexicano → Yen Japonés",
        "Peso Mexicano → Libra Esterlina",
        "Peso Mexicano → Franco Suizo",
        "Peso Mexicano → Peso Argentino",
        "Peso Mexicano → Real Brasileño",
        "Peso Mexicano → Peso Colombiano",
        "Peso Mexicano → Sol Peruano"
    ]
    
    print("\nCALCULADORA DE CONVERSIONES DE MONEDA")
    print("DESDE PESO MEXICANO:\n")
    
    for i, opcion in enumerate(opciones, start=1):
        print(f"{i}.  {opcion}")
    
    print("0.  Salir")

def main():
    conversiones = [
        (peso_mexicano_a_dolar_canadiense, "CAD"),
        (peso_mexicano_a_dolar_americano, "USD"),
        (peso_mexicano_a_euro, "EUR"),
        (peso_mexicano_a_yen, "JPY"),
        (peso_mexicano_a_libra_esterlina, "GBP"),
        (peso_mexicano_a_franco_suizo, "CHF"),
        (peso_mexicano_a_peso_argentino, "ARS"),
        (peso_mexicano_a_real_brasileno, "BRL"),
        (peso_mexicano_a_peso_colombiano, "COP"),
        (peso_mexicano_a_sol_peruano, "PEN")
    ]
    
    while True:
        mostrar_menu_monedas()
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 0:
            print("\n¡Gracias por usar la calculadora!")
            break
        elif 1 <= opcion <= len(conversiones):
            pesos = float(input("Ingrese cantidad en Pesos Mexicanos: "))
            funcion, moneda = conversiones[opcion - 1]
            resultado = funcion(pesos)
            print(f"\n{pesos} MXN = {resultado:.2f} {moneda}")
        else:
            print("\nOpción no válida")
        
        input("\nPresione Enter para continuar...")

if __name__ == "__main__":
    main()
