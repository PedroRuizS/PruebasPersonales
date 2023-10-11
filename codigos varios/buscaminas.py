###un codigo de un buscaminas medio feo, a ver como sale
###(probablemente no me vaya a salir y lo abandone)
print("Elige tu dificultad\n 1.-Principiante (9x9, 10 minas)\n 2.-Intermedio (16x16, 40 minas)\n 3/-Experto(16x30, 120 minas)")
numeroIn = input("Ingresa la dificultad de tu juego: ")
dificultad = int(numeroIn)
pointer0=0

numeroIn = input("Ingresa la dificultad de tu juego: ")    
if dificultad==1:
       i=9
       j=9
       minas=10
       pointer0=1
elif dificultad==2:
       i=16
       j=16
       minas=40
       pointer0=1
elif dificultad==3:
       i=16
       j=30
       minas=120
       pointer0=1   
