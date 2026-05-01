#%%
import numpy as np
import pandas as pd

def obtener_maximo_por_categoria(df, columna_categoria, columna_valor):
    """
    Agrupa un DataFrame por una columna categórica, calcula el máximo 
    de una columna numérica para cada categoría, ordena alfabéticamente 
    y devuelve los resultados como un array de NumPy.
    """
    resultado = (
        df.groupby(columna_categoria)[columna_valor]
        .max()           # Calcula el valor máximo por categoría
        .sort_index()    # Ordena las categorías (el índice) alfabéticamente
        .to_numpy()      # Convierte la Serie resultante a un np.ndarray
    )
    
    return resultado
# %%
