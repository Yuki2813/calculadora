from suma import sumar
from dividir import dividir
opcion=input("""Dime que opcion quieres
             1- Sumar
             2- Restar
             3-Multiplicar
             4-Dividir
             5-Salir""")

match opcion:
    case 1:
        num1=input("Dime el primer numero para sumar")
        num2=input("Dime el segundo numero para sumar")
        num1=int(num1)
        num2=int(num2)
        resultado=num1+num2
        print(f" El resultado es {resultado}")

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
        num1=int(num1)
        num2=int(num2)
        resultado=dividir(num1,num2)
        print(f" El resultado es {resultado}")
        pass
        # xxxxx
    case 5:

        pass
        # xxxx
    case _:

        pass