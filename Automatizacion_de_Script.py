import sys
import pandas as pd
import requests

def descargar_datos(url):
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.text
    else:
        print(f"Error al descargar los datos. Código de estado: {response.status_code}")
        sys.exit(1)

def convertir_a_dataframe(datos):
    # Supongamos que los datos están en formato CSV
    df = pd.read_csv(pd.compat.StringIO(datos))
    return df

def categorizar_grupos(df):
    # Aquí puedes realizar las operaciones de categorización o procesamiento que necesites
    # En este ejemplo, simplemente imprimir el dataframe
    print("Dataframe original:")
    print(df)

def exportar_csv(df, nombre_archivo):
    df.to_csv(nombre_archivo, index=False)
    print(f"Datos exportados exitosamente como {nombre_archivo}")

def main():
    # Verificar que se proporciona la URL como argumento
    if len(sys.argv) != 2:
        print("Uso: python script.py <url>")
        sys.exit(1)

    # Obtener la URL del primer argumento
    url = sys.argv[1]

    # Paso 1: Descargar datos
    datos = descargar_datos(url)

    # Paso 2: Convertir a dataframe
    dataframe = convertir_a_dataframe(datos)

    # Paso 3: Categorizar en grupos
    categorizar_grupos(dataframe)

    # Paso 4: Exportar a CSV
    exportar_csv(dataframe, "resultado.csv")

if __name__ == "__main__":
    main()

    # python script.py <url>

