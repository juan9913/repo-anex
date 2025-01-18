# Proyecto de Predicción de Precios de Viviendas

Este proyecto utiliza un conjunto de datos estandar para explorar, visualizar y modelar los precios de venta de viviendas.

## Estructura del Proyecto
- `main.py`: Archivo principal que ejecuta el flujo general del proyecto.
- `modulos/`: Contiene módulos para la carga y análisis de datos (`datos.py`) y modelado (`modelos.py`).
- `data/`: Carpeta que contiene los datos del proyecto.
- `img/`: Carpeta donde se guardan las visualizaciones generadas.

## Requisitos
Instalar las dependencias ejecutando:
```
pip install -r requirements.txt
```
## Analisis exploratorio de datos
Como parte del analisis exploratorio del conjunto de datos se observa la distribución del precio de venta con ayuda de un histograma
![](https://github.com/juan9913/repo-anex/blob/main/img/dist_saleprice.png)

Ahora se observa la relación entre el precio de vivienda y el area de las casas, se observa una relación directa donde a medida que el área de la casa es más grande el precio de la misma tambien es más grande.

![](https://github.com/juan9913/repo-anex/blob/main/img/scatter_GrLivArea.png)

finalmente se observa la relación entre el año de construcción y el precio de la casa, mostrando que entre más reciente el año de construcción de la misma, más alto es el precio.

![](https://github.com/juan9913/repo-anex/blob/main/img/scatter_YearBuilt.png)

## Ejecución
Ejecutar el archivo principal:
```
python main.py
```
## Resultados
## Resultados de Modelos

| Modelo             | RMSE       |
|--------------------|------------|
| Regresión Lineal   | 39,710.99  |
| Árbol de Decisión  | 41,283.35  |
| Random Forest      | 28,943.62  |

