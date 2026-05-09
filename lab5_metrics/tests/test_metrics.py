import numpy as np
from lab5_metrics.analyzer import ImageMetrics


def test_metrics():

    img = np.zeros((10, 10))

    analyzer = ImageMetrics()

    result = analyzer.calcular_metricas(img)

    assert result["mean"] == 0.0
    assert result["std"] == 0.0
    assert result["min"] == 0
    assert result["max"] == 0