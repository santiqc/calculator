# crear el esquema
menu="MENU OPERACIONES\n\n"
menu+="1.Sumar\n"
menu+="2.Restar\n"
menu+="3.Multiplicar\n"
menu+="4.Dividir\n"
menu+="5.Salir"
cod=0
while(cod!=5):
    num1=int(input("\nIngrese el numero 1: "))
    num2=int(input("Ingrese el numero 2: "))
    cod=int(input(menu+"\nIngrese la opcion del menú: "))
    if(cod==1):
        resultado=num1+num2
        print(f"SUMA: {num1}+{num2}={resultado}")
    elif(cod==2):
        resultado=num1-num2
        print(f"RESTA: {num1}-{num2}={resultado}")
    elif(cod==3):
        resultado=num1*num2
        print(f"MULTIPLICACION: {num1}*{num2}={resultado}")
    elif(cod==4):
        if(num2>0):
            resultado=num1/num2
            print(f"DIVISION: {num1}/{num2}={resultado}")
        else:
            print("No puede hacer división por 0")
    elif(cod==5):
        print("\nFinalizar\n")
    else:
        print("Valor Incorrecto")
