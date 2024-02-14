import rasterio

import numpy as np


IMAGE_HEIGHT = 3000
IMAGE_WIDTH = 4000


class MultispectralImage:
    def __init__(self, image: np.ndarray, metadata: dict) -> None:
        self._image = image
        self._metadata = metadata

    @property
    def image(self):
        return self._image

    @property
    def metadata(self):
        return self._metadata


class MultispectralRGNImage(MultispectralImage):
    @property
    def red_band(self):
        return self.image[0]

    @property
    def green_band(self):
        return self.image[1]

    @property
    def nir_band(self):
        return self.image[2]

    def ndvi(self) -> MultispectralImage:
        nom = (self.nir_band.astype(float) - self.red_band.astype(float))
        denom = (self.nir_band.astype(float) + self.red_band.astype(float))
        return MultispectralImage(nom / denom, metadata=self.metadata)

    def gndvi(self) -> MultispectralImage:
        nom = (self.nir_band.astype(float) - self.green_band.astype(float))
        denom = (self.nir_band.astype(float) + self.green_band.astype(float))
        return MultispectralImage(nom / denom, metadata=self.metadata)


class MultispectralOCNImage(MultispectralImage):
    @property
    def orange_band(self):
        return self.image[0]

    @property
    def cyan_band(self):
        return self.image[1]

    @property
    def nir_band(self):
        return self.image[2]


def save_multispectral_image(multispec_image: MultispectralImage, filename: str):
    image = multispec_image.image.reshape((-1, IMAGE_HEIGHT, IMAGE_WIDTH))
    metadata = multispec_image.metadata.copy()
    metadata['dtype'] = multispec_image.image.dtype.name
    metadata['count'] = image.shape[0]

    with rasterio.open(filename, 'w', **metadata) as file:
        file.write(image)
