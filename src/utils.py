import numpy as np
import pandas as pd

def make_synthetic_maint_data(n_units=220, cycles=130, random_state=42):
    """
    Genera un dataset sintético de mantenimiento predictivo.
    Cada unidad tiene lecturas de sensores a lo largo de múltiples ciclos.

    Parámetros:
        n_units (int): número de máquinas/unidades simuladas.
        cycles (int): número de ciclos por cada unidad.
        random_state (int): semilla para reproducibilidad.

    Retorna:
        pd.DataFrame: dataset con variables de sensores y etiqueta de fallo.
    """
    np.random.seed(random_state)
    
    records = []
    for unit in range(1, n_units + 1):
        for cycle in range(1, cycles + 1):
            temperature = np.random.normal(70, 10)
            pressure = np.random.normal(30, 5)
            vibration = np.random.normal(0.5, 0.1)
            hours_in_service = cycle * np.random.randint(5, 15)
            
            # Probabilidad de fallo
            fail_prob = (
                0.3 * (temperature > 80) +
                0.4 * (vibration > 0.6) +
                0.2 * (hours_in_service > 1500)
            )
            fail = int(np.random.rand() < fail_prob)
            
            records.append([unit, cycle, temperature, pressure, vibration, hours_in_service, fail])
    
    df = pd.DataFrame(records, columns=[
        "unit", "cycle", "temperature", "pressure", "vibration", "hours_in_service", "fail_in_H"
    ])
    
    return df


# Bloque de verificación (solo se ejecuta si corres "python src/utils.py")
if __name__ == "__main__":
    print("✅ utils.py cargado correctamente")
    print("Docstring:", make_synthetic_maint_data.__doc__)
    print("Parámetros:", make_synthetic_maint_data.__code__.co_varnames)
