#%%
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def detect_drifting_sensors(df, ref_rows):
    """
    Detecta sensores con drift comparándolos contra un período de referencia.
    
    Parámetros:
    -----------
    df : pd.DataFrame
        DataFrame con lecturas de sensores (columnas = sensores, filas = lecturas)
    ref_rows : int
        Número de filas iniciales que representan funcionamiento normal
        
    Retorna:
    --------
    list
        Nombres de sensores con más del 15% de lecturas fuera de ±3σ, 
        ordenados alfabéticamente
        
    Raises:
    -------
    ValueError: Si ref_rows es inválido o el DataFrame está vacío
    """
    
    # Validaciones
    if ref_rows <= 0 or ref_rows >= len(df):
        raise ValueError(f"ref_rows debe estar entre 1 y {len(df)-1}")
    
    if df.empty:
        raise ValueError("El DataFrame no puede estar vacío")
    
    # 1. Definir el periodo de referencia (sano)
    df_ref = df.iloc[:ref_rows]
    
    # 2. Entrenar StandardScaler solo con el período de referencia
    scaler = StandardScaler()
    scaler.fit(df_ref)
    
    # 3. Normalizar todo el DataFrame usando estadísticas del período sano
    df_scaled = pd.DataFrame(
        scaler.transform(df), 
        columns=df.columns,
        index=df.index  # Preservar índice original
    )
    
    # 4. Aislar el período de evaluación (después de ref_rows)
    df_eval = df_scaled.iloc[ref_rows:]
    
    # 5. Identificar lecturas fuera de ±3 desviaciones estándar
    # (al estar normalizado, abs > 3 implica salir del intervalo)
    outliers_mask = df_eval.abs() > 3
    
    # 6. Calcular el porcentaje de anomalías por sensor
    outliers_percentage = outliers_mask.mean()
    
    # 7. Identificar sensores con drift (>15% de anomalías)
    drifting_sensors = outliers_percentage[
        outliers_percentage > 0.15
    ].index.tolist()
    
    return sorted(drifting_sensors)