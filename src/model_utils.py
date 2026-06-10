import joblib
import pandas as pd
import os

MODEL_PATH = r"models\random_forest_model.pkl"
PREPROCESSOR_PATH = r"models\preprocessor.pkl"
DATA_PATH = r"data"


def cargar_modelo():
    """Carga el modelo entrenado."""
    return joblib.load(MODEL_PATH)


def cargar_preprocesador():
    """Carga el preprocesador."""
    return joblib.load(PREPROCESSOR_PATH)


def realizar_prediccion(csv_path):
    """
    Realiza predicciones y probabilidades sobre un dataset.
    """

    print(f"\nCargando dataset: {csv_path}")

    df = pd.read_csv(csv_path)

    preprocessor = cargar_preprocesador()
    model = cargar_modelo()

    # Transformación de datos
    X = preprocessor.transform(df)

    # Predicciones
    predicciones = model.predict(X)

    # Probabilidades (clase positiva = 1)
    probabilidades = model.predict_proba(X)[:, 1]

    # Resultado final
    resultado = df.copy()
    resultado["Prediccion"] = predicciones
    resultado["Prob_Depression"] = probabilidades

    return resultado


def guardar_resultados(df_resultado, csv_original):
    """
    Guarda el DataFrame con predicciones en un CSV.
    """

    nombre_archivo = os.path.basename(csv_original)

    output_name = nombre_archivo.replace(".csv", "_predictions.csv")

    output_path = os.path.join(DATA_PATH, output_name)

    df_resultado.to_csv(output_path, index=False)

    print(f"\nPredicciones guardadas en:\n{output_path}")
