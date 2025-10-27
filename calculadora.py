from suma import sumar
from dividir import dividir
from resta import resta
from multiplicacion import multiplicacion
opcion=input("""Dime que opcion quieres
             1- Sumar
             2- Restar
             3-Multiplicar
             4-Dividir
             5-Salir""")
opcion=int(opcion)

match opcion:
    case 1:
        num1=input("Dime el primer numero para sumar ")
        num2=input("Dime el segundo numero para sumar ")
        num1=int(num1)
        num2=int(num2)
        resultado=sumar(num1,num2)
        print(f" El resultado es {resultado}")

        
    case 2:
        num1=input("Dime el primer numero para restar ")
        num2=input("Dime el segundo numero para restar ")
        num1=int(num1)
        num2=int(num2)
        resultado=resta(num1,num2)
        print(f" El resultado es {resultado}")
        
    case 3:
        num1=input("Dime el primer numero para restar ")
        num2=input("Dime el segundo numero para restar ")
        num1=int(num1)
        num2=int(num2)
        resultado=multiplicacion(num1,num2)
        print(f" El resultado es {resultado}")
    case 4:
        num1=input("Dame el primer numero a dividir ")
        num2=input("Ahora dame el divisor del primero ")
        num1=int(num1)
        num2=int(num2)
        try:
            resultado=dividir(num1,num2)
            print(f" El resultado es {resultado}")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
        
        
        
       
    case 5:
        print("Saliendo de la calculadora ")
        
    case _:
        print("El valor indicado no esta entre las opciones dadas ")
        