#%%
import numpy as np
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import random

def generar_caso_de_uso_aplicar_pca():
    n_samples = random.randint(20, 50)
    n_features = random.randint(5, 10)
    n_comp = 2
    
    X = np.random.rand(n_samples, n_features)
    
    # Calcular Output esperado
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    pca = PCA(n_components=n_comp)
    X_expected = pca.fit_transform(X_scaled)
    
    input_data = {'X': X, 'n_comp': n_comp}
    output_data = X_expected
    
    return input_data, output_data

if __name__ == "__main__":
    entrada, salida_esperada = generar_caso_de_uso_aplicar_pca()
    
    print(f"=== ENTRADA (Matriz X de {entrada['X'].shape}) ===")
    print("Primeras 3 filas de X:")
    print(entrada['X'][:3])
    
    print("\n=== SALIDA ESPERADA (PCA transformado) ===")
    print(f"Componentes solicitados: {entrada['n_comp']}")
    print(f"Shape del resultado: {salida_esperada.shape}")
    print("Primeras 3 filas del resultado:")
    print(salida_esperada[:3])