def esSeparador(c):
    separadores = "\n\t "
    return c in separadores

def esSimboloEsp(c):
    especiales = "¡#$%&/*+-=:;[]{}(),"
    return c in especiales

def quitaComentarios(cad):
    # estados: A, B, C, Z
    estado ="Z"    
    #cad = "a=b/c;"
    cad2 =""
    for c in cad:
        if (estado=="Z"):
            if (c=="/"):
                estado = "A"
            else:
                cad2 = cad2 + c
        elif (estado=="A"):
            if (c=="*"):
                estado="B"
            else:
                estado = "Z"
                cad2=cad2+"/"+c
        elif (estado=="B"):
            if (c=="*"):
                estado = "C"
        elif(estado=="C"):
            if (c=="/"):
                estado="Z"
            else:
                estado="B"
    return cad2

def tokeniza(cad):
    tokens = []
    dentro = False
    token = ""
    for c in cad:
        if dentro:  #esta dentro del token
            if esSeparador(c): 
                tokens.append(token)
                token = ""
                dentro = False
            elif esSimboloEsp(c):
                tokens.append(token)
                tokens.append(c)
                token = ""
                dentro = False
            else:
                token = token + c
        else: #esta fuera del token
            if esSimboloEsp(c):
                tokens.append(c)
            elif esSeparador(c):
                a=0
            else:
                dentro = True
                token = c
    return tokens

def esId(cad):
    return (cad[0] in "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

def esPalReservada(cad):
    reservadas = ["main","char", "int","float","double","if","else","do","while","for","switch","short","long","extern", "static","default","continue","break","register","sizeof","typedef"]
    return cad in reservadas

def esTipo(cad):
    tipos=["int", "char", "float", "double"]
    return cad in tipos