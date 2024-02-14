import numpy as np


def window_mean(input_image: np.ndarray, window_shape: tuple[int, int]) -> float:
    assert window_shape[0] < input_image.shape[0] and window_shape[1] < input_image.shape[1]
    output_image = np.zeros_like(input_image)
    for v_step in range(0, input_image.shape[0], window_shape[0]):
        v_lim = min(window_shape[0] + v_step, input_image.shape[0] - 1)
        for h_step in range(0, input_image.shape[1], window_shape[1]):
            h_lim = min(window_shape[1] + h_step, input_image.shape[1] - 1)
            window = input_image[v_step:v_lim, h_step:h_lim]
            output_image[v_step:v_lim, h_step:h_lim] = window.mean()
    return output_image


def ndvi(red_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    return (nir_band.astype(float) - red_band.astype(float)) / (nir_band.astype(float) + red_band.astype(float))


def gndvi(green_band: np.ndarray, nir_band: np.ndarray) -> np.ndarray:
    return (nir_band.astype(float) - green_band.astype(float)) / (nir_band.astype(float) + green_band.astype(float))

