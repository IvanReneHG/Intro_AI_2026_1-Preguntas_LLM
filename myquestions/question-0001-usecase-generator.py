import pandas as pd
import numpy as np
import random

def generar_caso_de_uso_limpiar_ventas():
    n_rows = random.randint(10, 20)
    fechas = pd.date_range(start='2023-01-01', periods=n_rows).strftime('%Y-%m-%d').tolist()
    montos = [random.uniform(100, 1000) for _ in range(n_rows)]
    
    # Introducir errores negativos
    indices_error = random.sample(range(n_rows), 2)
    for idx in indices_error:
        montos[idx] = -50.0
        
    df_input = pd.DataFrame({'fecha': fechas, 'monto': montos})
    
    # Calcular Output esperado
    df_expected = df_input.copy()
    df_expected['fecha'] = pd.to_datetime(df_expected['fecha'])
    positivos = [m for m in montos if m > 0]
    promedio = sum(positivos) / len(positivos)
    df_expected.loc[df_expected['monto'] < 0, 'monto'] = promedio
    
    input_data = {'df': df_input, 'col_fecha': 'fecha', 'col_monto': 'monto'}
    output_data = (df_expected, float(promedio))
    
    return input_data, output_data

# --- BLOQUE PARA PROBAR EL GENERADOR ---
if __name__ == "__main__":
    # 1. Llamamos a la función generadora
    entrada, salida_esperada = generar_caso_de_uso_limpiar_ventas()
    
    # 2. Mostramos los resultados para verificar
    print("=== ENTRADA (INPUT) ===")
    print(f"Columna Fecha: {entrada['col_fecha']}")
    print(f"Columna Monto: {entrada['col_monto']}")
    print("DataFrame Original:")
    print(entrada['df'])
    
    print("\n=== SALIDA ESPERADA (OUTPUT) ===")
    df_res, prom = salida_esperada
    print(f"Promedio calculado: {prom}")
    print("DataFrame Procesado:")
    print(df_res)