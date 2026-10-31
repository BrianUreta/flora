#!/usr/bin/env bash
set -e
mkdir -p data/raw

# PlantVillage (~2 GB): entrenamiento base
[ -d data/raw/plantvillage ] || git clone --depth 1 https://github.com/spMohanty/PlantVillage-Dataset data/raw/plantvillage

# PlantDoc: fotos de campo para test
[ -d data/raw/plantdoc ] || git clone --depth 1 https://github.com/pratikkayal/PlantDoc-Dataset data/raw/plantdoc

# IP102: descarga manual (Google Drive, uso academico)
echo "IP102: descargar desde https://github.com/xpwu95/IP102 y descomprimir en data/raw/ip102"
