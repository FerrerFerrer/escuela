# Leer la primera letra del txt, nos lleva al estado 0. En un arreglo guardamos los tipos
# de caracteres que puede tener para entrar al estado.
#arreglo = ["digito","letra","punto","e","_","+","-","/","espacio"]
extras = [".", "e", "_", "+", "-", "/", " "]
estado = 0
columna = 0
archivo = open("texto.txt")
texto = archivo.read()
matriz = [
    # 0
    [1, 7, 205, 7, 207, 208, 209, 8, 0],
    # 1S
    [1, 200, 2, 4, 200, 200, 200, 200, 200],
    # 2
    [3, 300, 300, 300, 300, 300, 300, 300, 300],
    # 3
    [3, 201, 201, 4, 201, 201, 201, 201, 201],
    # 4
    [6, 301, 301, 301, 301, 5, 5, 301, 301],
    # 5
    [6, 302, 302, 302, 301, 302, 302, 302, 302],
    # 6
    [6, 202, 202, 202, 202, 202, 202, 202, 202],
    # 7
    [7, 7, 203, 203, 7, 203, 203, 203, 203],
    # 8
    [206, 206, 206, 206, 206, 206, 206, 9, 206],
    # 9
    [9, 9, 204, 204, 204, 204, 204, 204, 9]
]

status = ["Palabra", "Digito", "Funciones", "Resta", "Suma", "División", "Multiplicación", "Guion bajo", "Espacio"]
# for i in range(0, len(texto)):
#     print(texto[i])
#     print(i)
# print(archivo.read())
# Sino se llega a un estado final se hace i++

# Si llega a estado final con asterisco se hace i--

def matrizEstados(i, j):
    resultado = matriz[i][j]
    if resultado >= 200:
        if resultado >= 300 :
          print("Error") 
          i += 1
        else:
            if resultado == 207:
                print("Guion bajo") 
            elif resultado == 208:
                print("Suma")
            elif resultado == 209:
                print("Resta")
            elif resultado == 205:
                print("Punto")            
    else:
        i = resultado
    return i


def recorrido():
    global estado
    global columna
    for i in range(0, len(texto)):
        # verificar si es una letra
        if texto[i].isalpha() == True:
            columna = 1
           # print("letra")
        # verificar si es un numero
        elif texto[i].isdigit() == True:
            columna = 0
            #print("numero")
        # simbolos o espacios
        else:
            for j in range(0, len(extras)):
                if (extras[j] == texto[i]):
                    columna = j + 2
        estado = matrizEstados(estado, columna)

recorrido()
