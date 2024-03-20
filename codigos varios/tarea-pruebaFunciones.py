import FuncionesCompiladores as fc
from FuncionesCompiladores import *

print("1.-Separador")
print("2.-Simbolos especiales")
print("3.-Quita comentarios")
print("4.-Tokeniza")
print("5.-Id")
print("6.-Es palabra reservada?")
print("7.-Tipo")

inputOpcion = input("¿Qué función deseas probar?: ")

match inputOpcion:
    case "1":
        cSeparador = input("Ingresa el caracter a probar si es separador: ")
        resultado = fc.esSeparador(cSeparador)
        print("El resultado de la operación es:")
        print(resultado)
    case "2":
        cSimboloEsp = input("Ingresa el caracter a probar si es simbolo especial: ")
        resultado = fc.esSimboloEsp(cSimboloEsp)
        print("El resultado de la operación es:")
        print(resultado)
    case "3":
        cadQuitaComen = input("Ingresa la cadena a la que quitarle el comentario: ")
        resultado = fc.quitaComentarios(cadQuitaComen)
        print("El resultado de la operación es:")
        print(resultado)
    case "4":
        cadTokeniza = input("Ingresa la cadena a Tokenizar: ")
        resultado = fc.tokeniza(cadTokeniza)
        print("El resultado de la operación es:")
        print(resultado)
    case "5":
        cadId = input("Ingresa el caracter a probar si es Id: ")
        resultado = fc.esId(cadId)
        print("El resultado de la operación es:")
        print(resultado)
    case "6":
        cadPalReservada = input("Ingresa la cadena a probar si es Palabra reservada: ")
        resultado = fc.esPalReservada(cadPalReservada)
        print("El resultado de la operación es:")
        print(resultado)
    case "7":
        cadTipo = input("Ingresa las cadenas a verificar si son identificadores de tipo: ")
        resultado = fc.esTipo(cadTipo)
        print("El resultado de la operación es:")
        print(resultado)

