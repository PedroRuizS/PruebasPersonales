class Etiqueta: ##definimos la clase etiqueta
    def __init__(self, nombre, linea): #la clase tiene dos atributos, nombre y linea, self es usado para inicializar
        self.nombre = nombre #inicializamos nombre y linea
        self.linea = linea


def es_simbolo_esp(caracter): #funcion para saber los caracteres especiales de una cadena
    return caracter in "+-*;,.:!#=%&/(){}[]<><=>=="


def es_separador(caracter): #funcion para saber si una cadena contiene caracteres especiales
    return caracter in " \n\t"


def tokenizar(cadena):
    # Reemplaza las comas por un espacio seguido de una coma
    cadena = cadena.replace(',', ' ,')
   
    # Divide la cadena por espacios y devuelve la lista de tokens
    tokens = cadena.split()
   
    return tokens


instrucciones = [] #declaramos el arreglo  instrucciones en donde se va a guardar todas las instrucciones


arch = open('prog1.txt', 'r') #abrimos el archivo prog1.txt y lo leemos
for ren in arch: #vamos leyendo lineqa por linea el archivo y vamos ejhectuando esto
    if len(ren)>2: #si la longitud de el renglon es menor de dos
        datos = tokenizar(ren)  #tokenizamos la informacion en el renglon y la asignamos a la vaariable tados
        instrucciones.append(datos) # metemos la informacion guardada en datos en el arreglo instrucciones
arch.close() #cerramos el archivo


pc = 0 #inicializamos el program counter en 0
registros = [] #inicializamos el arreglo donde vammos a guardar los registros de el programa
for c in range(32): #como las instrucciones corren en 32 bytes, vamos a agregar hasta 32
    registros.append(0)


# encontrar todas las etiquetas
etiquetas = [] #iniciamos el arreglo etiquetas donde se van a guardar los nombres de las etiquetas
for c in range(len(instrucciones)):
    if instrucciones[c][0] == '%': #las etiquetas se definen como %nombre entonces sacamos de la lista hastea
        etiquetas.append(Etiqueta(instrucciones[c][1], c))#encontrar un %, cuando se encuentra, se agrga a etiquetas
       
def get_dir_etiqueta(etq):
    direccion = -1
#lo que hacemos es ver la linea en la que se encuentra etiquetas, entonces le restamos uno, para conocer si direccion
    for e in etiquetas:
        if e.nombre == etq:
            return e.linea  
    return direccion


# imprimir todas las etiquetas
for e in etiquetas:
    print(e.nombre, e.linea)


while instrucciones[pc][0]!='END': #mientras que el token que estamos leyendo, no sea end, vamos a hacer este codigo
    inst = instrucciones[pc]
    print(pc, registros[2], inst)
    if inst[0]=='ADDI': # si el token es ADDI, haremos la instreuccion de suma inmediata
        destino = int(inst[1][1:]) #el destino es igual a la primera direccion que se nos da en la instruccion
        reg1 = int(inst[3][1:])
        numero = int(inst[5])        
        registros[destino] = registros[reg1] + numero
        pc = pc + 1 #al finalizar la instruccion, agregaremos uno al program counter y cambiaremos de linea
    elif inst[0] == '%': # si el programa encuentra % no hara nada porque es una etiqueta y las etiquetas no hacen nada
        pc = pc + 1
    elif inst[0] == 'MUL':
        destino = int(inst[1][1:])
        reg1 = int(inst[3][1:])
        reg2 = int(inst[5][1:])
        registros[destino] = registros[reg1] * registros[reg2]
        pc = pc + 1 
    elif inst[0] == 'SUB':
        destino = int(inst[1][1:])
        reg1 = int(inst[3][1:])
        reg2 = int(inst[5][1:])
        registros[destino] = registros[reg1] - registros[reg2]
        pc = pc + 1        
    elif inst[0] == 'J': #Jump salta a la dirección indicada
        etq = inst[1]    # encontramos la etiqueta a donde saltar
        pc = get_dir_etiqueta(etq)  #buscamos la direccion en la tabla de etiquetas
        print('saltando a', pc) #indicamos a donde vamos a saltar
    elif inst[0] == 'BGE': #si la instruccion es branch if greater or equal than
        op1 = registros[int(inst[1][1:])] #op1 es el numero uno con el que se va aq comparar, es decir el numero inicial
        num = int(inst[3]) # es el numero con el que se va  aestar comparando
        etq = inst[5]
        print('comparando ' , op1, 'con', num)
        if op1 >= num: #cuando el ciclo se cumpla, es decir que op1 sea mayor o igual a num
            pc = get_dir_etiqueta(etq) #el program counter va a regresar a su valora nterior
        else:
            pc = pc + 1 #si no, se va  acontinuar comparando
