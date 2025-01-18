import os
from modulos import datos, modelos

# Ruta de las carpetas
ruta_datos = 'data/train.csv'
ruta_img = 'img/'
# os.makedirs(ruta_img, exist_ok=True)

# Cargar datos
df = datos.cargar_datos(ruta_datos)

datos.visualizar_datos(df, ruta_img)

# Preparacion y seleccion de variables predictoras
X, y = datos.preparar_datos(df)

# Aplicacion de modelos y validacion
resultados = modelos.comparar_modelos(X, y)

# Mostrar resultados
# print("\nResultados finales:")
# for modelo, resultado in resultados.items():
#    print(f"{modelo}: {resultado}")

# Guardar resultados en un archivo de texto

resultados_path = os.path.join(ruta_img, "resultados.txt")

with open(resultados_path, "w") as f:
    f.write("Resultados de los modelos:\n")
    for modelo, rmse in resultados.items():
        f.write(f"{modelo}: RMSE = {rmse:.2f}\n")

print(f"Resultados guardados en {resultados_path}")
