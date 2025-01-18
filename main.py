import os
from modulos import datos, modelos

# Ruta de las carpetas
ruta_datos = 'data/train.csv'
ruta_img = 'img/'
os.makedirs(ruta_img, exist_ok=True)

# Cargar datos
df = datos.cargar_datos(ruta_datos)

datos.visualizar_datos(df, ruta_img)

# Preparacion y seleccion de variables predictoras
X, y = datos.preparar_datos(df)

# Aplicacion de modelos y validacion
resultados = modelos.comparar_modelos(X, y)
