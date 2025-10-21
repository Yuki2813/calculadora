from dividir import dividir
opcion=input("""Dime que opcion quieres
             1- Sumar
             2- Restar
             3-Multiplicar
             4-Dividir
             5-Salir""")

match opcion:
    case 1:

        pass
    case 2:

        # xxxx
        pass
    case 3:

        pass
        # xxxxx
    case 4:
        num1=input("Dame el primer numero a dividir")
        num2=input("Ahora dame el divisor del primero")
        resultado=dividir(num1,num2)
        print(f" El resultado es {resultado}")
        pass
        # xxxxx
    case 5:

        pass
        # xxxx
    case _:

        pass