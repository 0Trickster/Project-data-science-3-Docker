# Project-data-science-3-Docker

"""# 🐳 Proyecto de Predicción con Machine Learning en Docker

Este proyecto implementa un sistema de predicción utilizando un modelo de Machine Learning entrenado con Scikit-Learn, empaquetado y ejecutado mediante Docker.

---

## Descripción

- Cargar datasets CSV
- Preprocesamiento de datos
- Predicciones con modelo entrenado
- Guardado de resultados

---

## Tecnologías

- Python 3.12
- Scikit-Learn
- Pandas
- NumPy
- Joblib
- Docker

---

## Estructura

project/
├── src/
├── models/
├── data/
├── requirements.txt
├── Dockerfile
└── README.md

---

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