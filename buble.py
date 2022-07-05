import random


def ordenamiento_de_burbuja(lista):
  length = len(lista)

  for item in range(length):
    for item2 in range(0, length - item - 1):
      if lista[item2] > lista[item2 + 1]: # change 8 > 2, then my 8 index will be my 2 index and both
        lista[item2], lista[item2 + 1] = lista[item2 + 1], lista[item2] # intercambio

  return lista


if __name__ == '__main__':
  tamano_de_lista = int(input('What size will be of list? '))

  lista = [random.randint(0, 100) for i in range(tamano_de_lista)]
  print(lista)

  lista_ordenada = ordenamiento_de_burbuja(lista)
  print(lista_ordenada)

