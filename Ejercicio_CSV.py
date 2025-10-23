import pandas as pd

NOMBRE_ARCHIVO = "Herramientas_disponibles_Taller_Chepetronica(Inventario).csv"

def extrator_csv() -> list:
    global NOMBRE_ARCHIVO
    with open(NOMBRE_ARCHIVO, "r") as archivo:
        contenido = archivo.readlines()
        # print(contenido)
        
        lista_datos = []
        for linea in contenido:
            lista_datos.append( linea.strip().split(";") )

    return lista_datos    

def main():
    lista_datos = extrator_csv()
    tabla_datos = pd.DataFrame(lista_datos[1:], columns=lista_datos[0])

    print(tabla_datos)
    tabla_datos.set_index("ID", inplace=True)
    print("\nTabla con índice ID:")
    print("Soy un alucin")

    #Primer comit de prueba git
    #Prueba 2
    
if  __name__ == "__main__":
    main()