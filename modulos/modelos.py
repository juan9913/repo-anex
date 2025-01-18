# librerias y paquetes
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Funciones para modelado


def comparar_modelos(X, y):
    """Aplica varios modelos, realiza validación cruzada y compara los resultados."""
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)

    modelos = {
        "Regresión Lineal": LinearRegression(),
        "Árbol de Decisión": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    resultados = {}
    for nombre, modelo in modelos.items():
        modelo.fit(X_train, y_train)
        predicciones = modelo.predict(X_test)
        rmse = np.sqrt(mean_squared_error(y_test, predicciones))
        resultados[nombre] = rmse

    return resultados
