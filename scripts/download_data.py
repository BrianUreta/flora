"""Descarga el dataset de papa (AgML) en data/raw/potato_agml/<clase>/."""
import shutil
from collections import Counter
from pathlib import Path

from datasets import Image, load_dataset

REPO = "Project-AgML/potato_leaf_disease_classification"
OUT = Path("data/raw/potato_agml")
CACHE = Path("data/.hf_cache")

if OUT.exists() and any(OUT.iterdir()):
    raise SystemExit(f"Ya existe {OUT}. Bórralo si quieres descargar de nuevo.")

ds = load_dataset(REPO, split="train", cache_dir=str(CACHE))
nombres = ds.features["label"].names
ds = ds.cast_column("image", Image(decode=False))

conteo = Counter()
for i, fila in enumerate(ds):
    clase = nombres[fila["label"]]
    img = fila["image"]
    ext = Path(img.get("path") or "x.jpg").suffix or ".jpg"
    carpeta = OUT / clase
    carpeta.mkdir(parents=True, exist_ok=True)
    (carpeta / f"{clase.lower()}_{i:05d}{ext}").write_bytes(img["bytes"])
    conteo[clase] += 1

shutil.rmtree(CACHE, ignore_errors=True)
for clase, n in sorted(conteo.items()):
    print(f"{clase:<12} {n}")
print(f"Total: {sum(conteo.values())} imágenes en {OUT}")
