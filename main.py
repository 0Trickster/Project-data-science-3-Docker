from src.model_utils import *
from src.carga_csv import *

def main():
    """
    Punto de entrada principal.
    """

    print("=" * 50)
    print("SISTEMA DE PREDICCIÓN DE DEPRESIÓN ESTUDIANTIL")
    print("=" * 50)

    csv_path = seleccionar_csv()

    resultado = realizar_prediccion(csv_path)

    print("\nPrimeras predicciones:")
    print(resultado.head())

    guardar_resultados(
        resultado,
        csv_path
    )


if __name__ == "__main__":
    main()