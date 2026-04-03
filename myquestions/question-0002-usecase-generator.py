#%%
import pandas as pd
import random

def generar_caso_de_uso_valor_por_categoria():
    cats = ['A', 'B', 'C']
    df_in = pd.DataFrame({
        'categoria': [random.choice(cats) for _ in range(10)],
        'stock': [random.randint(1, 10) for _ in range(10)],
        'precio_unitario': [random.uniform(10, 20) for _ in range(10)]
    })
    df_exp = df_in.copy()
    df_exp['valor_total'] = df_exp['stock'] * df_exp['precio_unitario']
    output = df_exp.groupby('categoria')[['valor_total']].sum()
    return {'df': df_in}, output

if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_valor_por_categoria()
    
    print("=== ENTRADA (DataFrame de Inventario) ===")
    print(entrada['df'])
    
    print("\n=== SALIDA ESPERADA (Suma de Valor Total) ===")
    print(salida_esperada)