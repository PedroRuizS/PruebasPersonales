class Variable:
    def __init__(self, nombre, tipo): #En la clase variable estamos definiendo 
        self.nombre = nombre          #Los identificadores de una variable
        self.tipo = tipo
        self.valor = None

def agrega_var(tabla_var, nombre, tipo):
    tabla_var.append(Variable(nombre, tipo)) #Aqui definimos una tabla donde se van a insertar las variables
    pass

def existe_var(tabla_var, nombre):#Aqui verificamos que en la tabla de variables
    encontrado = False            #No se repita la variable que queremos insertar
    for v in tabla_var:           
        if v.nombre == nombre:    
            encontrado = True
    return encontrado

def set_var(tabla_var, nombre, valor):  #set var utiliza existe var para ver el estado y le agrega un 
    if existe_var(tabla_var, nombre):   #valor a la variable existente
        for v in tabla_var:
            if v.nombre == nombre:
                v.valor = valor
    else:
        print('variable ', nombre, 'no encontrada') #si no existe la variable, nos da un mensaje de error
        return None

def imprime_tabla_var(tabla_var): ##aqui solo se imprime la tabla de variables creada
    print()
    print('   Tabla de variables')
    print('nombre\t\ttipo\t\tvalor')
    for v in tabla_var:
        print(v.nombre,'\t\t', v.tipo,'\t\t', v.valor) ##en este ciclo for, vamos recorriendo la tabla e 
    return None                                        #imprimiendo

def es_simbolo_esp(caracter): #una funcion simple para ver si los caracteres contenidos en el string de entrada
    return caracter in "+-*;,.:!#=%&/(){}[]<><=>==" #son caracteres especiales

def es_separador(caracter): #igual que la anterior solo que de separadores
    return caracter in " \n\t"

def es_id(cad): #definimos si los caracteres que conforman la cadena pueden ser parte de un id de variable
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def  es_pal_res(cad): #aqui se definen las palabras reservadas
    palres = ["int","real","string", 'print', 'read', 'tabla']
    return (cad in palres)

def esEntero(caracter):
    return caracter in "1234567890"
def  es_tipo(cad): #aqui se defninen los tipos que pueden tomar las variables
    tipos = ["int","real","string"]
    return (cad in tipos)

def separa_tokens(linea): #una funcion que separa la cadena de entrada en tokenn si la longitud es menor de 3
    if len(linea) < 3:    #aqui vemos si la cadena cumple los requerimiento sminimos para separar, que es
        return []         #tener minimo 3 caracteres
    else:    
        tokens = []   ##Se inicializan los arreglos donde se van a guardar
        tokens2 = []  
        dentro = False   
        for l in linea: #iteramos para cara caracter en la cadena
            if es_simbolo_esp(l) and not(dentro): #verificamos si el caracter es simbolo especial
                tokens.append(l)
            if (es_simbolo_esp(l) or es_separador(l)) and dentro: #verificamos si es un separador
                tokens.append(cad)
                dentro = False
                if es_simbolo_esp(l):
                    tokens.append(l)
            if not (es_simbolo_esp(l)) and not (es_separador(l)) and not(dentro):
                dentro = True
                cad=""
            if not (es_simbolo_esp(l)) and not (es_separador(l)) and dentro:
                    cad = cad + l   
        compuesto = False #verificamos para ver si el caracter es compuesto como == !=
        for c in range(len(tokens)-1):
            if compuesto:
                compuesto = False
                continue
            if tokens[c] in "=<>!" and tokens[c+1]=="=":
                tokens2.append(tokens[c]+"=")
                compuesto = True
            else:
                tokens2.append(tokens[c])
        tokens2.append(tokens[-1])    
        for c in range(1,len(tokens2)-1): #recorremos la cadena menos el ultimo caracter
            if tokens2[c]=="." and esEntero(tokens2[c-1]) and esEntero(tokens2[c+1]):
                tokens2[c]=tokens2[c-1]+tokens2[c]+tokens2[c+1]
                tokens2[c-1]="borrar" 
                tokens2[c+1]="borrar"    
        porBorrar = tokens2.count("borrar")
        for c in range(porBorrar): #Combinar los numeros separados por puntos
            tokens2.remove("borrar")
        tokens=[]
        dentroCad = False
        cadena = ""
        for t in tokens2:        
            if dentroCad:
                if t[-1]=='"':
                    cadena=cadena+" "+t
                    tokens.append(cadena[1:-1])
                    dentroCad = False
                else:
                    cadena = cadena+" "+t
            elif ((t[0]=='"')):
                  cadena= t;
                  dentroCad = True
            else:
                  tokens.append(t)
    return tokens

tabla_var = [] 
ren = "" #se almacena el input del usuario aqui
while (ren != 'end;'):
    ren = input('$:')
    tokens = separa_tokens(ren) #tokenizamos la entrada del usuario
    if es_id(tokens[0]):
        if es_pal_res(tokens[0]):
            if es_tipo(tokens[0]):
                if es_id(tokens[1]):
                    agrega_var(tabla_var, tokens[1], tokens[0])
            elif tokens[0] == 'read':
                if tokens[1] == '(' and es_id(tokens[2]) and tokens[3] == ')':
                    leido = input()
                    set_var(tabla_var, tokens[2], leido)
            elif tokens[0] == 'tabla':               
                imprime_tabla_var(tabla_var)
            elif tokens[0] == "print":##variable agregada para poder imprimir  
                if tokens[1] == '(' and es_id(tokens[2]) and tokens[3] == ')': 
                    for v in tabla_var:
                        if v.nombre == tokens[2]:
                            print(v.valor)

        elif tokens[1] == "=":# agregar funcion para poder declarar
            set_var(tabla_var, tokens[0], tokens[2])

    