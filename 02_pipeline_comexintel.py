"""
02_pipeline_comexintel.py

Propósito: Automatizar la limpieza, transformación y consolidación de 
archivos mensuales de DataSur para el dashboard de ComexIntel.
Autor: Roberto
"""

import pandas as pd
import numpy as np
from pathlib import Path
from datetime import datetime

# ------------------------------------------------------------------
# 1. Configuración de Rutas 
# ------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).parent.parent
RAW_DIR = PROJECT_ROOT / "data" / "raw"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

# ------------------------------------------------------------------
# 2. Funciones de Transformación (Extraídas de tu Notebook)
# ------------------------------------------------------------------
def fechas(fila):
    # Columnas año, mes y día se importan a la función para hacer el datetime
    anio = fila["AÑO"]
    mes = fila["MES"]
    dia = fila["DIA"]

    # Evalua si año es menor a 100 para sumarle 2000 y que quede normalizado
    if anio < 100:
        anio += 2000

    # Evalua si el año tiene formato de 4 digitos para mantenerlo y no tener que convertirlo
    elif anio >= 1900:
        pass

    else:
        print(f"Warning: año {anio} fuera de rangos esperados")
        return None

    return datetime(anio, mes, dia)

# ------------------------------------------------------------------
# 3. Ejecución del Pipeline
# ------------------------------------------------------------------
def ejecutar_pipeline():
    print(f"{'='*60}")
    print(" INICIANDO PIPELINE DE DATOS - COMEXINTEL")
    print(f"{'='*60}")
    
    archivos_excel = list(RAW_DIR.rglob('*.xlsx'))
    
    if not archivos_excel:
        print("❌ Error: No se encontraron archivos Excel en la carpeta raw.")
        return
    
    print(f"Archivos detectados para procesar: {len(archivos_excel)}")
    
    lista_dfs = []
    for archivo in archivos_excel:
        print(f"  -> Leyendo: {archivo.name}")
        df_temp = pd.read_excel(archivo)
        lista_dfs.append(df_temp)
        
    df_maestro = pd.concat(lista_dfs, ignore_index=True)
    print(f"\nDatos consolidados. Total de filas crudas: {len(df_maestro)}")
    
    print("\nAplicando transformaciones de negocio...")
    
    # Aplicando tu lógica exacta del notebook
    df_maestro["FECHA"] = df_maestro.apply(fechas, axis=1)
    
    df_maestro["PESO_KG"] = df_maestro["CANTIDAD ESTADISTICA"]
    
    df_maestro["USD_KG"] = (
        (df_maestro["FOB USD"] / df_maestro["PESO_KG"]).replace([np.inf, -np.inf], np.nan).round(3)
    )
    
    # Deduplicación por NRO DOCUMENTO
    filas_antes = len(df_maestro)
    df_maestro = df_maestro.drop_duplicates(subset=['NRO DOCUMENTO'])
    filas_despues = len(df_maestro)
    if filas_antes != filas_despues:
        print(f"  [!] Se eliminaron {filas_antes - filas_despues} registros duplicados.")
    
    # Exportación del archivo maestro único
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    ruta_salida = PROCESSED_DIR / "dataset_comexintel_maestro.csv"
    df_maestro.to_csv(ruta_salida, index=False, encoding='utf-8-sig')
    
    print(f"\n{'='*60}")
    print(f" PIPELINE COMPLETADO EXITOSAMENTE")
    print(f" Archivo maestro guardado en: data/processed/dataset_comexintel_maestro.csv")
    print(f" Total filas finales: {len(df_maestro)}")
    print(f"{'='*60}")

if __name__ == "__main__":
    ejecutar_pipeline()