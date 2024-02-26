import numpy as np

from sklearn.cluster import KMeans
from multispectral_image import MultispectralRGNImage, IMAGE_HEIGHT, IMAGE_WIDTH


def window_mean(input_image: np.ndarray, window_shape: tuple[int, int]) -> float:
    assert window_shape[0] < input_image.shape[0] and window_shape[1] < input_image.shape[1]
    output_image = np.zeros_like(input_image)
    for v_step in range(0, input_image.shape[0], window_shape[0]):
        v_lim = min(window_shape[0] + v_step, input_image.shape[0])
        for h_step in range(0, input_image.shape[1], window_shape[1]):
            h_lim = min(window_shape[1] + h_step, input_image.shape[1])
            window = input_image[v_step:v_lim, h_step:h_lim]
            output_image[v_step:v_lim, h_step:h_lim] = window.mean()
    return output_image


def zero_one_norm(arr: np.ndarray) -> np.ndarray:
    return (arr - arr.min()) / (arr.max() - arr.min())


def clusterize_multispectral_image(model: KMeans, mimage: MultispectralRGNImage) -> np.ndarray:
    ndvi_image_band = zero_one_norm(mimage.ndvi().image)
    gndvi_image_band = zero_one_norm(mimage.gndvi().image)
    nir_image_band = zero_one_norm(mimage.nir_band)

    flat_data = np.empty((IMAGE_HEIGHT * IMAGE_WIDTH, 3))

    for i, band in enumerate((ndvi_image_band, gndvi_image_band, nir_image_band)):
        flat_data[:, i-1] = band.flatten()

    return model.predict(flat_data)
