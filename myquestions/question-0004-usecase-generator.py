#%%
# question-0004-usecase-generator.py
import pandas as pd
import numpy as np

def generar_caso_de_uso_segmentar_por_cuantiles():
    # Generamos una distribución de ingresos aleatoria
    ingresos = [10, 20, 30, 40, 50, 60, 70, 80, 100, 200, 500, 1000]
    df_in = pd.DataFrame({'ingresos': ingresos})
    
    # Lógica de validación
    # Dividir en 4 grupos con el mismo número de registros cada uno
    output_esperado = pd.qcut(df_in['ingresos'], q=4, labels=['Bajo', 'Medio', 'Alto', 'Top'])
    
    return {'df': df_in, 'col_nombre': 'ingresos'}, output_esperado

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_segmentar_por_cuantiles()
    print("=== INPUT (Datos Continuos) ===\n", entrada['df'].T)
    print("\n=== OUTPUT (Categorías por Cuantiles) ===\n", salida.values)
