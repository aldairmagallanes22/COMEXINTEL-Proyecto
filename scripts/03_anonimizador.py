import pandas as pd
from pathlib import Path

# Configurar rutas
PROJECT_ROOT = Path(__file__).parent.parent
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

print("Generando dataset anonimizado completo...")

# 1. Leer el dataset original
ruta_original = PROCESSED_DIR / "dataset_alulosa_procesado.csv"
df_seguro = pd.read_csv(ruta_original)

# 2. Anonimizar importadores y proveedores manteniendo la consistencia en todas las filas
df_seguro['IMPORTADOR'] = 'Importador ' + (df_seguro.groupby('IMPORTADOR').ngroup() + 1).astype(str)
df_seguro['ID IMPORTADOR'] = 'ID_ANONIMO'

df_seguro['SUPPLIERNAME'] = 'Proveedor ' + (df_seguro.groupby('SUPPLIERNAME').ngroup() + 1).astype(str)
df_seguro['ID PROVEEDOR'] = 'ID_ANONIMO'

# 3. Eliminar columnas con direcciones y nombres de personas reales
columnas_sensibles = [
    'DIRECCION DE IMPORTADOR', 'CIUDAD DE IMPORTADOR', 'ESTADO DE IMPORTADOR',
    'DIRECCION DE PROVEEDOR', 'CIUDAD O ESTADO DEL PROVEEDOR', 'AGENTE DE ADUANA'
]
df_seguro = df_seguro.drop(columns=columnas_sensibles, errors='ignore')

# 4. Exportar el dataset completo y seguro para GitHub
ruta_salida = PROCESSED_DIR / "dataset_comexintel_publico.csv"
df_seguro.to_csv(ruta_salida, index=False, encoding='utf-8-sig')

print(f"Dataset público generado con éxito en: {ruta_salida}")