# COMEXINTEL-Proyecto
# 🚢 ComexIntel: Análisis Estratégico y Automatizado de Importaciones

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)

📊 Ver Dashboard Interactivo aquí: [Dashboard](https://app.powerbi.com/view?r=eyJrIjoiNDkwYTcyMzYtY2VlYi00NGYzLTkyMDUtNWZmMDNjNGZjNWQ2IiwidCI6IjM5OTYyZjgwLTkyMTItNGIxZi04Yjk1LWU3OTYyYzRhY2IzMCIsImMiOjR9)

## 📌 Resumen del Proyecto
ComexIntel es una solución analítica *end-to-end* diseñada para procesar, limpiar y visualizar datos aduanales de importaciones del mercado alimenticio (en este primer análisis únicamente de Alulosa) en México (Enero - Abril 2026). 

El proyecto reemplaza los análisis estáticos en Excel con un **pipeline de datos automatizado en Python** y un **dashboard interactivo en Power BI**, permitiendo identificar tendencias de precios, volumen de mercado y estrategias de competidores clave en tiempo real.

## 🎯 Problema de Negocio
El análisis manual de reportes de importación (vía plataformas como DataSur) es propenso a errores, duplicidad de registros y consume demasiado tiempo operativo. Además, la dispersión de los datos dificulta responder preguntas estratégicas rápidas como:
* ¿Quiénes son los jugadores principales en la importación de un producto?
* ¿Se está pagando un "premium" por intermediación logística?
* ¿Cómo fluctúa el precio promedio de mercado (USD/kg) frente a variaciones de volumen?

## ⚙️ Arquitectura y Flujo de Datos

El ciclo de vida del dato consta de tres fases:

1. **Extracción (Raw Data):** Archivos mensuales `.xlsx` con registros a nivel de pedimento aduanal.
2. **Pipeline ETL (Python / Pandas):** 
   * Se desarrolló el script `02_pipeline_comexintel.py` que consolida los archivos de la carpeta fuente.
   * Transforma y normaliza tipos de datos (fechas, variables numéricas).
   * Genera métricas unitarias (Precio USD/KG).
   * Aplica reglas de negocio para **deduplicación** utilizando el `NRO DOCUMENTO` como llave primaria.
3. **Visualización (Power BI):** Consumo del dataset procesado para un modelado star simple y aplicación de funciones DAX para el cálculo dinámico de KPIs.

## 📊 Dashboard y Hallazgos Clave

El dashboard incluye navegación por marcadores (bookmarks), filtros dinámicos colapsables y formato condicional basado en rangos de rentabilidad de precios.

**<img width="749" height="840" alt="image" src="https://github.com/user-attachments/assets/b789c981-66c8-43b4-8314-36dbb8bafe03" />**

### 💡 Insights Destacados:
* **Volatilidad y Anomalía de Mercado (Marzo - Abril)**: Se identificó una fuerte fluctuación en el primer cuatrimestre. Mientras que marzo registró el pico de precio más alto ($2.80 USD/kg) con el volumen más bajo del periodo, abril rompió drásticamente la tendencia con un salto masivo en volumen (superando los 500,000 kg) y una corrección de precio a la baja ($2.34 USD/kg). Esto sugiere compras de pánico preventivas en meses previos o una entrada agresiva de inventario a bajo costo en abril.

* **Dominio Asiático**: El análisis geográfico revela una dependencia absoluta del mercado oriental. El 66.67% de las transacciones de importación (32 registros) provienen directamente de China, consolidándose como el principal proveedor, dejando a Estados Unidos en un segundo lugar estratégico con el 31.25%.

* **Concentración de Transacciones**: El mercado está fuertemente liderado por dos actores clave ("Importador 2" e "Importador 5"), quienes encabezan la frecuencia operativa con 7 transacciones cada uno en el periodo. El formato condicional del ranking evidencia brechas de eficiencia (colores verde, amarillo y rojo) entre los importadores principales y aquellos con menor volumen.

El color de cada barra evalúa el precio promedio por kg de producto

- Barra verde es que el precio es igual o menor a 2.20
- Barra naranja es que el precio es mayor o igual a 2.2 pero menor a 2.7
- Barra roja precio es mayor a 2.7

## 🚀 Instrucciones de Ejecución

Para replicar este pipeline de transformación en un entorno local:

1. Clona este repositorio.
2. Asegúrate de tener instaladas las dependencias: `pip install pandas openpyxl`
3. Coloca tus reportes mensuales en la carpeta `data/raw/`.
4. Ejecuta el pipeline desde la terminal:
   ```bash
   python scripts/02_pipeline_comexintel.py
