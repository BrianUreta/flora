# Datasets evaluados y descartados

Los evaluamos antes de elegir el dataset de papa de AgML. Se conservan como registro de la decisión; no se usan en el pipeline.

| Dataset | Por qué lo descartamos |
|---|---|
| PlantVillage | Fotos de laboratorio (hoja aislada, fondo uniforme): no representa condiciones de campo. |
| PlantDoc | Fotos de campo, pero test muy chico (18 de 28 clases con <10 imágenes), 11 duplicados entre train y test, 9 duplicados con etiqueta contradictoria y fotos de stock. Ver `eda_plantdoc.md`. |
| IP102 | Plagas de insectos en general, no específico de papa; descarga manual. |

Para volver a descargarlos (desde la raíz del repo): `bash archive/download_data_plantvillage_plantdoc.sh`
