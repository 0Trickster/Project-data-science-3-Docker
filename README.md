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

## ⚠️ Consideraciones

El docker debe ejecutarse de la siguiente manera:

```bash
docker run -it data-science-app
