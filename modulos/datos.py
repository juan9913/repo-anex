# cargar librerias
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# funcion para cargar datos


def cargar_datos(ruta):
    return pd.read_csv(ruta)


# df = cargar_datos(
#     "C:/Users/Juan David/Documents/Cursos/Dalto VS Code/proyecto_inicial/data/train.csv")

# print(df.head(5))
# print(df.shape)
# print(df[['Id', 'Street']])
# print(df.describe())
# sns.histplot(df['SalePrice'])
# plt.show()

def visualizar_datos(df, images_path):

    # Distribución del precio de venta
    plt.figure(figsize=(8, 6))
    sns.histplot(df['SalePrice'], kde=True, color="blue")
    plt.title("Distribución de SalePrice")
    plt.savefig(os.path.join(images_path, "dist_saleprice.png"))
    plt.close()

    # Relación entre variables seleccionadas y SalePrice
    variables = ['GrLivArea', 'TotalBsmtSF', 'OverallQual', 'YearBuilt']
    for var in variables:
        plt.figure(figsize=(8, 6))
        sns.scatterplot(x=df[var], y=df['SalePrice'])
        plt.title(f"Relación entre {var} y SalePrice")
        plt.savefig(os.path.join(images_path, f"scatter_{var}.png"))
        plt.close()


def preparar_datos(df):
    """Prepara los datos para el modelado, seleccionando variables y la variable objetivo."""
    variables = ['OverallQual', 'GrLivArea', 'GarageCars',
                 'TotalBsmtSF', 'FullBath', 'YearBuilt']
    X = df[variables]
    y = df['SalePrice']
    return X, y
