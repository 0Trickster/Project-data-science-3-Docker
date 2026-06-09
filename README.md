# Project-data-science-3-Docker

# 🐳 Proyecto de Predicción con Machine Learning en Docker

Este proyecto implementa un sistema de predicción utilizando un modelo de Machine Learning entrenado con **Scikit-Learn**, empaquetado y ejecutado mediante **Docker** para asegurar portabilidad y reproducibilidad.

---

## 📌 Descripción

El sistema permite:

- Cargar datasets en formato CSV
- Aplicar pipeline de preprocesamiento
- Ejecutar un modelo de clasificación
- Generar predicciones
- Guardar resultados en un nuevo archivo CSV

---

## 🧠 Tecnologías utilizadas

- Python 3.12
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Docker

---

## 📁 Estructura del proyecto

```text
project/
├── src/
│   ├── main.py
│   ├── carga_csv.py
│   ├── predict.py
├── models/
│   ├── random_forest_model.pkl
│   ├── preprocessor.pkl
├── data/
│   ├── dataset.csv
├── requirements.txt
├── Dockerfile
├── .dockerignore
└── README.md

## Uso local

pip install -r requirements.txt
python src/main.py

---

## Docker

### Build
docker build -t <nombre de tu app> .

### Run
docker run -it <nombre de tu app>

---

## Requirements

pandas
numpy
scikit-learn
joblib

---

## Docker issues

EOFError → usar docker run -it

ModuleNotFoundError sklearn → usar scikit-learn

---

## Mejoras futuras

- API con FastAPI
- Deploy en AWS
- Logging
"""