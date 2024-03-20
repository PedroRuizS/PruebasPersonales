#####################
###DEFINICION FUNCION
#####################
def guardianesGaleriaICPC(grafo, reco, tiempoLim):
  # Definimos la función guardianesGaleriaICPC()
  # Definimos los valores necesarios, que son el grafo que define las salas, la recompensa dada por el tiempo, esta siendo positiva o negativa y el tiempo limite que es afectado poir esta recompensa
  costos = [float("inf")] * len(grafo)
  costos[0] = tiempoLim
  # Inicializamos los "costos" al infinito, antes de definir su valor real


  for _ in range(len(grafo)):
    # Hacemos iteraciones sobre los nodos de el grafo
    for u in range(len(grafo)):
      for v in range(len(grafo)):
        # Iteramos sobre los "vecinos" de cada nodo del cual hemos iterado
        if grafo[u][v] > 0:
          new_cost = costos[u] - reco[u] + reco[v] + grafo[u][v]
          # Si el costo del nodo "vecino" es menor que el costo del nodo actual mas el tiempo que se tarda en recorrer la arista, actualizamos el costo del nodo actual.

          if 0 <= u < len(costos) and new_cost < costos[v]:
            costos[v] = new_cost

  # Hacemos que se devuelva el camino mas largo o decimos que los valores dados hacen un resultado imposible
  path = []
  u = len(grafo) - 1
  while u > 0:
    path.append(u)
    u = costos[u] - reco[u]
  if path[0] != 0:
    path.reverse()
    return path, len(path)
  else:
    return "Los valores dados son imposibles "

#####################
###/uso de el algoritmo
################

opcion = 0
print("¿Qué problema quieres resolver?")
print("1.-Guardianes de la galería")
print("2.-a qui noai nada")
opcion = int(input())

if opcion == 1:
  grafo = eval(input("Ingresa los valores de el grafo en formato de cadena, ejemplo [a1,a2,a3,...,aN]: "))
  recompensas = eval(input("Ingresa la recompensa dada en formato de cadena, ejemplo [a1,a2,a3,...,aN]: "))
  tiempo_limite = eval(input("Ingresa el tiempo limite: "))
  camino = guardianesGaleriaICPC(grafo, recompensas, tiempo_limite)
  print(camino)
else:
  print("TODAVIA NO HAY SEGUNDA OPCION")

