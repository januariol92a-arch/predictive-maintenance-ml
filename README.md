# Mantenimiento Predictivo con Machine Learning

Proyecto completo y didáctico para predecir **fallas de equipos** y **vida útil restante (RUL)** usando Python y Scikit-learn.
Incluye **regresión, clasificación, clustering, PCA**, evaluación rigurosa (CV, F1, ROC, RMSE), y prevención de *data leakage* con `Pipeline`.

## 🎯 Objetivos
- **Clasificación**: predecir si el equipo fallará en la próxima ventana de tiempo.
- **Regresión**: estimar la **vida útil restante (RUL)**.
- **Clustering + PCA**: detectar patrones operativos y posibles anomalías.

## 🧱 Estructura
```
maintenance_predictive_ml_project/
├── data/                 # (opcional) datasets reales
├── models/               # modelos guardados (.joblib)
├── notebooks/
│   └── 01_predictive_maintenance_end_to_end.ipynb
├── reports/              # gráficas exportadas y resumen ejecutivo
├── src/                  # utilidades
└── README.md
```

## 🚀 Cómo ejecutar
1. Crear un entorno virtual e instalar dependencias:
```
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate
pip install -U pip
pip install numpy pandas scikit-learn matplotlib joblib
```
*(Opcional para t-SNE):* `pip install --upgrade scikit-learn`

2. Abrir el notebook:
```
jupyter notebook notebooks/01_predictive_maintenance_end_to_end.ipynb
```
> El notebook **genera un dataset sintético reproducible**, por lo que puedes ejecutarlo sin descargar datos. Luego podrás **reemplazarlo** por un dataset real (Kaggle NASA CMAPSS, etc.).

## 📝 Reemplazar por dataset real (opcional)
- Coloca los archivos en `data/` y adapta la celda "Cargar dataset real".
- Respeta la separación **train / validation / test** para evitar *data leakage*.

## 🧑‍💼 Para LinkedIn
- Título sugerido: **Mantenimiento Predictivo con Machine Learning (Clasificación, Regresión, Clustering + PCA)**
- Descripción breve incluida en `reports/LinkedIn_summary.txt`

---

© 2025
