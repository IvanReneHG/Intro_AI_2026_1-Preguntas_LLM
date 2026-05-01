#%%
import pandas as pd
import numpy as np

def suavizar_carga_servidor(df, span_ewma):
    """
    Resamplea datos irregulares de CPU a frecuencia horaria y aplica suavizado exponencial.
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con columnas 'timestamp' (str) y 'cpu_load' (float)
    span_ewma : int
        Parámetro de span para la Media Móvil Exponencial
        
    Retorna:
    --------
    pd.DataFrame
        DataFrame con índice temporal y columnas:
        - cpu_load: carga horaria promediada
        - load_ewma: media móvil exponencial
        
    Raises:
    -------
    ValueError: Si faltan columnas requeridas o span_ewma no es positivo
    """
    
    # Validaciones
    if not isinstance(df, pd.DataFrame):
        raise TypeError("El argumento debe ser un DataFrame de pandas")
    
    required_cols = {'timestamp', 'cpu_load'}
    if not required_cols.issubset(df.columns):
        raise ValueError(f"Columnas requeridas: {required_cols}")
    
    if not isinstance(span_ewma, int) or span_ewma <= 0:
        raise ValueError("span_ewma debe ser un entero positivo")
    
    # Procesamiento
    df_procesado = df.copy()
    
    # 1. Convertir timestamp a datetime y establecer como índice
    df_procesado['timestamp'] = pd.to_datetime(df_procesado['timestamp'])
    df_procesado = df_procesado.set_index('timestamp')
    
    # 2. Resamplear por hora, calcular promedio y rellenar vacíos
    df_procesado = df_procesado.resample('h').mean()
    df_procesado['cpu_load'] = df_procesado['cpu_load'].ffill()
    
    # 3. Calcular Media Móvil Exponencial
    df_procesado['load_ewma'] = df_procesado['cpu_load'].ewm(span=span_ewma).mean()
    
    return df_procesado
# %%
