
# Proyecto de Mantenimiento Predictivo con Machine Learning

## Objetivo
Desarrollar un sistema de **mantenimiento predictivo** que ayude a anticipar fallos en equipos industriales,
reduciendo costos y mejorando la disponibilidad de la infraestructura.

## Metodología
1. **Generación de datos sintéticos** para simular sensores industriales (temperatura, presión, vibración, horas de servicio).
2. **Modelos supervisados**:
   - Clasificación: predicción de fallos inminentes (Logistic Regression, Random Forest).
   - Regresión: estimación del tiempo de vida útil restante (Ridge, Lasso, Random Forest Regressor).
3. **Modelos no supervisados**:
   - PCA + Clustering (KMeans, DBSCAN) para descubrir patrones de operación y detectar anomalías.
4. **Evaluación** con métricas estándar (F1-score, RMSE, R²).

## Resultados Clave
- El modelo **Random Forest Classifier** obtuvo el mejor desempeño en la detección de fallos.
- El modelo **Random Forest Regressor** logró predecir el tiempo de vida útil restante con buena precisión.
- El análisis no supervisado permitió identificar **patrones operativos** y detectar **anomalías** que podrían anticipar fallos no registrados.

## Impacto para Stakeholders
- Reducción de **costos de mantenimiento** gracias a reparaciones planificadas.
- Incremento en la **disponibilidad de equipos** y reducción de paradas inesperadas.
- Mejora en la **seguridad operacional** al anticipar fallos críticos.

---
Este proyecto integra técnicas de **IA aplicada a la ingeniería industrial**, mostrando cómo el Aprendizaje Automático puede transformar la gestión de mantenimiento.
