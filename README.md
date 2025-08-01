**Español:**

# 🛒 Supermarket Inventory Optimizer (Batch Data Pipeline)

Proyecto de Data Engineering orientado a negocio y diseñado para optimizar el reabastecimiento de productos en supermercados regionales. Procesa datos históricos de ventas, clima y promociones para generar recomendaciones logísticas automáticas.

---

## 🚀 Objetivos

- Simular e ingestar datos multi-regionales de ventas diarias.
- Enriquecer con información externa (clima, eventos).
- Validar y transformar datos con estándares empresariales.
- Orquestar un pipeline batch reproducible y escalable.
- Generar salidas limpias para consumo de BI, ciencia de datos o automatización logística.

---

## 📦 Stack Tecnológico

| Componente           | Herramienta                     |
|----------------------|----------------------------------|
| Orquestación         | Apache Airflow / Perfect        |
| Transformación       | PySpark + pandas                 |
| Simulación           | Faker                            |
| Calidad de datos     | ydata-profiling + Great Expectations |
| Almacenamiento       | CSV (raw) → Parquet / PostgreSQL |
| Entorno              | Poetry + VSCode + Jupyter        |
| Pruebas              | Pytest               |

---

## 📁 Estructura del Proyecto

supermarket-inventory-optimizer/
├── .vscode/ ← Configuración VSCode
├── data/ ← Datos simulados (raw, processed)
├── notebooks/ ← Exploración y análisis (EDA)
├── scripts/ ← Scripts ejecutables
├── dags/ ← DAGs de Perfect / Airflow
├── src/ ← Código fuente del pipeline
├── tests/ ← Pruebas automáticas
├── pyproject.toml ← Dependencias gestionadas con Poetry
├── README.md ← Este archivo

---

## 🔁 Flujo General

1. **Simulación de datos:** Ventas regionales históricas, promociones y clima.
2. **EDA y validación:** Exploración con `ydata-profiling`, reglas con `Great Expectations`.
3. **Ingesta:** Orquestada con Airflow o Prefect.
4. **Transformación:** Limpieza y normalización con PySpark.
5. **Almacenamiento:** PostgreSQL o Parquet en `data/processed/`.
6. **Reportes / exportación:** Para dashboards o equipos de negocio.

---

## 📈 Ejemplo de resultados
- Reportes HTML automáticos de EDA (ydata-profiling)

- Archivos processed/ optimizados y listos para analítica

- Reglas de validación con Great Expectations

- DAG funcional con múltiples tareas interdependientes

---

## Autor

**Heberth Caripa**
Data Engineering & Machine Learning Enthusiast
📍 Chile | ✉️ [heberthcaripa@gmail.com] | 🔗 [LinkedIn](https://www.linkedin.com/in/heberth-caripa/)

**English:** 

# 🛒 Supermarket Inventory Optimizer (Batch Data Pipeline)

Business-oriented Data Engineering project designed to optimize product restocking in regional supermarkets. It processes historical sales, weather, and promotions data to generate automated logistics recommendations.

---

## 🚀 Objectives

- Simulate and ingest multi-regional daily sales data  
- Enrich with external sources (weather, events)  
- Validate and transform data with enterprise standards  
- Orchestrate a reproducible and scalable batch pipeline  
- Generate clean outputs for BI, data science, or logistics automation  

---

## 📦 Tech Stack

| Component             | Tool                             |
|----------------------|----------------------------------|
| Orchestration         | Apache Airflow / Prefect        |
| Transformation        | PySpark + pandas                 |
| Simulation            | Faker                            |
| Data Quality          | ydata-profiling + Great Expectations |
| Storage               | CSV (raw) → Parquet / PostgreSQL |
| Environment           | Poetry + VSCode + Jupyter        |
| Testing               | Pytest                           |

---

## 📁 Project Structure

supermarket-inventory-optimizer/
├── .vscode/ ← VSCode configuration
├── data/ ← Simulated data (raw, processed)
├── notebooks/ ← Exploration and analysis (EDA)
├── scripts/ ← Executable scripts
├── dags/ ← Perfect / Airflow DAGs
├── src/ ← Pipeline source code
├── tests/ ← Automated tests
├── pyproject.toml ← Poetry-managed dependencies
├── README.md ← This file


---

## 🔁 General Flow

1. **Data Simulation:** Historical regional sales, promotions, and weather  
2. **EDA and Validation:** Exploration with `ydata-profiling`, rules with `Great Expectations`  
3. **Ingestion:** Orchestrated via Airflow or Prefect  
4. **Transformation:** Cleaning and normalization with PySpark  
5. **Storage:** PostgreSQL or Parquet in `data/processed/`  
6. **Reporting / Export:** For dashboards or business teams  

---

## 📈 Sample Outputs

- Automated HTML EDA reports (via ydata-profiling)  
- Optimized processed/ files ready for analytics  
- Validation rules with Great Expectations  
- Working DAG with interdependent tasks  

---

## Author

**Heberth Caripa**  
Data Engineering & Machine Learning Enthusiast  
📍 Chile | ✉️ heberthcaripa@gmail.com | 🔗 [LinkedIn](https://www.linkedin.com/in/heberth-caripa/)
