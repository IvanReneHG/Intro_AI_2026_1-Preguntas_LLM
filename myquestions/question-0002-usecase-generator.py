#%%
# question-0002-usecase-generator.py
import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_promedio_por_sensor_2023():
    n_rows = 20
    sensores = ['S1', 'S2', 'S3']
    fechas = pd.to_datetime(['2022-05-10', '2023-01-15', '2023-06-20', '2024-01-01'] * 5)
    
    df_in = pd.DataFrame({
        'timestamp': fechas.strftime('%Y-%m-%d'),
        'sensor_id': [random.choice(sensores) for _ in range(20)],
        'lectura': [random.uniform(20.0, 30.0) for _ in range(20)]
    })
    
    # Lógica esperada
    temp_df = df_in.copy()
    temp_df['timestamp'] = pd.to_datetime(temp_df['timestamp'])
    df_2023 = temp_df[temp_df['timestamp'].dt.year == 2023]
    output = df_2023.groupby('sensor_id')['lectura'].mean()
    
    return {'df': df_in}, output

if __name__ == "__main__":
    entrada, salida = generar_caso_de_uso_promedio_por_sensor_2023()
    print("=== INPUT (Sensores) ===\n", entrada['df'].head())
    print("\n=== OUTPUT (Promedio 2023) ===\n", salida)
