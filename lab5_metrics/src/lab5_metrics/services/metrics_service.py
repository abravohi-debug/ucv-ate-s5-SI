import cv2
import matplotlib.pyplot as plt

from lab5_metrics.analyzer import ImageMetrics


def analizar(path: str):

    imagen = cv2.imread(path, 0)

    if imagen is None:
        return {"error": "No se pudo leer la imagen"}

    plt.hist(imagen.flatten(), bins=50)
    plt.title("Histograma")
    plt.show()

    analyzer = ImageMetrics()

    return analyzer.calcular_metricas(imagen)