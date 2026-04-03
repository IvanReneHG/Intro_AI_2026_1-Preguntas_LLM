#%%
# question-0003-usecase-generator.py
import numpy as np
from sklearn.preprocessing import PolynomialFeatures

def generar_caso_de_uso_generar_interacciones_puras():
    """
    Genera un caso donde tenemos 3 variables y queremos ver sus combinaciones.
    Si X tiene columnas [A, B, C], el output debe ser [A, B, C, A*B, A*C, B*C].
    """
    # 5 muestras de 3 variables (ej: Precio, Publicidad, Descuento)
    X = np.array([
        [10, 2, 1],
        [20, 5, 0],
        [15, 3, 1],
        [25, 8, 0],
        [30, 10, 1]
    ], dtype=float)
    
    # Lógica de validación
    # interaction_only=True evita que salga A^2, B^2, etc.
    poly = PolynomialFeatures(degree=2, interaction_only=True, include_bias=False)
    X_expected = poly.fit_transform(X)
    
    return {'X': X}, X_expected

if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_generar_interacciones_puras()
    
    print("=== INPUT (Variables Originales A, B, C) ===")
    print(entrada['X'])
    
    print("\n=== OUTPUT (Originales + Interacciones A*B, A*C, B*C) ===")
    print(salida_esperada)
    print(f"\nNúmero de columnas final: {salida_esperada.shape[1]} (Esperado: 6)")
