# RS²Lab - Analíse do Nível de Estresse Hídrico Recorrendo a Uma Camera Multispectral Mapir Survey 3

Para a referida análise as imagens terão de ser capturadas através de um veículo aéreo não tripulado (um drone) recorrendo a câmara multispectral [Mapir Survey 3](https://www.mapir.camera/pages/survey3-cameras) (que foi o modelo utilizado neste estudo em específico).

## Descrição do Processo

### Coleta de Imagens no Campo Agrícola Usando um Drone​

As imagens deverão ser coletadas num campo agrícola que contenha preferencialmente plantas de cor natural verde. Para tal a câmara terá de ser implantada num drone, e deslocar o drone através do espaço aéreo do campo agrícola nas partes que se quiser analisar. Lembre-se de seguir os procedimentos recomendados no site oficial da câmara Mapir Survey 3. Algo a ter em conta é que será necessário ter as imagens JPG capturadas pela câmara junto do ficheiro RAW contendo mais informações relevantes em relação às capturas feitas. 

### Tratamento e Processamento das Imagens Coletadas​

As imagens coletadas terão de ser convertidas para o formato tiff para depois serem processadas, e para tal terá dois caminhos:

1. (**Recomendado**) Descarregar o software [Mapir Camera Control](https://www.mapir.camera/products/mapir-camera-control) distribuido pelo criador da câmara para fazer esse processo de conversão
2. Utilizar o programa encontrado no repositório em [survey3-raw-tiff-converter](https://github.com/rs2lab/survey3-raw-tiff-converter) para fazer os processo

Nesses casos o primeiro é o mais recomendado pois dá resultados bem melhores do que na segunda opção.

Após coletar as imagens pode seguir com os procedimentos encontrados no notebook [water stress detection](water_stress_detection.ipynb)

<!-- TODO
### Análise das Imagens
 -->
## Referências Bibliográficas

- *[1] C. Z. Espinoza, L. R. Khot, S. Sankaran, e P. W. Jacoby, «High Resolution Multispectral and Thermal Remote Sensing-Based Water Stress Assessment in Subsurface Irrigated Grapevines», Remote Sensing, vol. 9, n.º 9. MDPI AG, p. 961, set. 16, 2017. doi: 10.3390/rs9090961.*

- *[2] M. R. Khomarudin e P. Sofan, «CROP WATER STRESS INDEX (CWSI) ESTIMATION USING MODIS DATA», International Journal of Remote Sensing and Earth Sciences (IJReSES), vol. 3, n.º. Indonesian National Institute of Aeronautics and Space (LAPAN), out. 11, 2010. doi: 10.30536/j.ijreses.2006.v3.a1208.*

- *[3] G. F. Capristo S et al., «NDVI Response to Water Stress in Different Phenological Stages in Culture Bean», Journal of Agronomy, vol. 15, n.º 1. Science Alert, pp. 1–10, dez. 15, 2015. doi: 10.3923/ja.2016.1.10.*

- *[4] K. Wang e Y. Jin, «Mapping Walnut Water Stress with High Resolution Multispectral UAV Imagery and Machine Learning». arXiv, 2024. doi: 10.48550/ARXIV.2401.01375.​*

- *[5] M. Gerhards, M. Schlerf, K. Mallick, e T. Udelhoven, «Challenges and Future Perspectives of Multi-/Hyperspectral Thermal Infrared Remote Sensing for Crop Water-Stress Detection: A Review», Remote Sensing, vol. 11, n.º 10. MDPI AG, p. 1240, mai. 24, 2019. doi: 10.3390/rs11101240.​*

- *[6] S. S. Virnodkar, V. K. Pachghare, V. C. Patil, e S. K. Jha, «DenseResUNet: An Architecture to Assess Water-Stressed Sugarcane Crops from Sentinel-2 Satellite Imagery», Traitement du Signal, vol. 38, n.º 4. International Information and Engineering Technology Association, pp. 1131–1139, ago. 31, 2021. doi: 10.18280/ts.380424.*
