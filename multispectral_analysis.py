import numpy as np


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
