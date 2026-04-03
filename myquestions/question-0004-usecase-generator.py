#%%
import numpy as np
from sklearn.metrics import confusion_matrix, accuracy_score
import random

def generar_caso_de_uso_evaluar_clasificacion():
    y_real = np.array([random.randint(0, 1) for _ in range(20)])
    y_pred = np.array([random.randint(0, 1) for _ in range(20)])
    
    matriz = confusion_matrix(y_real, y_pred)
    acc = accuracy_score(y_real, y_pred)
    
    return {'y_real': y_real, 'y_pred': y_pred}, {'matriz': matriz, 'exactitud': float(acc)}

if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_evaluar_clasificacion()
    
    print("=== ENTRADA (Clasificación) ===")
    print(f"Valores Reales: {entrada['y_real']}")
    print(f"Valores Predichos: {entrada['y_pred']}")
    
    print("\n=== SALIDA ESPERADA (Métricas) ===")
    print(f"Exactitud (Accuracy): {salida_esperada['exactitud']:.4f}")
    print("Matriz de Confusión:")
    print(salida_esperada['matriz'])
# %%
