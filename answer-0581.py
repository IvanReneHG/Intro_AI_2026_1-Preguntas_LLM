#%%
import numpy as np
from sklearn.feature_selection import mutual_info_classif

def calcular_ganancia_informacion(X, y):
    """
    Calcula la ganancia de información de cada feature respecto a un objetivo binario.
    
    Proceso:
    1. Binariza cada feature según su mediana
    2. Calcula la mutual information (ganancia de información)
    3. Devuelve los valores de ganancia por feature
    
    Parámetros:
    -----------
    X : array-like, shape (n_samples, n_features)
        Matriz de features (array numpy o DataFrame pandas)
    y : array-like, shape (n_samples,)
        Vector objetivo binario (0 o 1)
        
    Retorna:
    --------
    numpy.ndarray, shape (n_features,)
        Ganancia de información para cada feature, en el mismo orden
        
    Raises:
    -------
    ValueError: Si X no tiene 2 dimensiones o y no es 1D
    """
    
    # Convertir a numpy array
    X_array = np.asarray(X)
    y_array = np.asarray(y)
    
    # Validaciones
    if X_array.ndim != 2:
        raise ValueError(f"X debe tener 2 dimensiones, se recibió {X_array.ndim}")
    
    if y_array.ndim != 1:
        raise ValueError(f"y debe ser 1D, se recibió {y_array.ndim}D")
    
    if len(y_array) != X_array.shape[0]:
        raise ValueError(
            f"X e y deben tener el mismo número de muestras. "
            f"X: {X_array.shape[0]}, y: {len(y_array)}"
        )
    
    n_clases = len(np.unique(y_array))
    if n_clases < 2:
        raise ValueError(f"y debe ser binario, pero tiene {n_clases} clase(s)")
    
    # 1. Calcular la mediana para cada columna
    medianas = np.median(X_array, axis=0)
    
    # 2. Binarizar: 1 si valor > mediana, 0 si valor ≤ mediana
    X_bin = (X_array > medianas).astype(int)
    
    # 3. Calcular ganancia de información (mutual information)
    ganancias = mutual_info_classif(
        X_bin, 
        y_array, 
        discrete_features=True,
        random_state=42
    )
    
    return ganancias