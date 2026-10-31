import hashlib
from pathlib import Path

import pandas as pd
from PIL import Image, ImageDraw

ROOT = Path("data/raw/plantdoc")
OUT = Path("reports")
OUT.mkdir(exist_ok=True)
EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}

# 1. Inventario
rows = []
for split in ["train", "test"]:
    for f in sorted((ROOT / split).rglob("*")):
        if f.is_file():
            rows.append({"split": split, "clase": f.parent.name, "path": f, "ext": f.suffix.lower()})
df = pd.DataFrame(rows)
otros = df[~df["ext"].isin(EXTS)]
df = df[df["ext"].isin(EXTS)].copy()

# 2. Metadatos por imagen
def leer(p):
    try:
        with Image.open(p) as im:
            im.verify()
        with Image.open(p) as im:
            w, h, modo = im.size[0], im.size[1], im.mode
        ok = True
    except Exception:
        w, h, modo, ok = None, None, None, False
    md5 = hashlib.md5(p.read_bytes()).hexdigest()
    return pd.Series({"ancho": w, "alto": h, "modo": modo, "ok": ok, "md5": md5})

df = pd.concat([df, df["path"].apply(leer)], axis=1)
df["cultivo"] = df["clase"].str.split().str[0].str.lower()
df["sana"] = df["clase"].str.lower().str.strip() == df["cultivo"] + " leaf"

# 3. Resúmenes
por_clase = (df.pivot_table(index="clase", columns="split", values="md5",
                            aggfunc="count", fill_value=0)
               .reindex(columns=["train", "test"], fill_value=0))
por_clase["total"] = por_clase.sum(axis=1)
por_clase = por_clase.sort_values("total", ascending=False)

clases_tr = set(df.loc[df.split == "train", "clase"])
clases_te = set(df.loc[df.split == "test", "clase"])
tr = por_clase["train"][por_clase["train"] > 0]

dups = df[df.duplicated("md5", keep=False)]
fuga = int((df.groupby("md5")["split"].nunique() > 1).sum())
conflicto = int((df.groupby("md5")["clase"].nunique() > 1).sum())

lineas = [
    "# EDA PlantDoc",
    f"Imágenes: {len(df)} (train {sum(df.split=='train')}, test {sum(df.split=='test')})",
    f"Archivos no imagen: {len(otros)}",
    f"Corruptas: {int((~df.ok).sum())}",
    f"Clases: {df.clase.nunique()} | cultivos: {df.cultivo.nunique()} | clases 'sanas': {df.loc[df.sana,'clase'].nunique()}",
    f"Solo en train: {sorted(clases_tr - clases_te)}",
    f"Solo en test: {sorted(clases_te - clases_tr)}",
    f"Desbalance train (máx/mín por clase): {tr.max()}/{tr.min()} = {tr.max()/tr.min():.1f}x",
    f"Clases con <10 imágenes en test: {int((por_clase['test'] < 10).sum())}",
    f"Imágenes duplicadas (exactas): {len(dups)} en {dups.md5.nunique()} grupos",
    f"Duplicados entre train y test (fuga): {fuga}",
    f"Duplicados con etiqueta distinta: {conflicto}",
    "", "## Imágenes por clase", "```", por_clase.to_string(), "```",
    "", "## Tamaños (px)", "```", df[["ancho", "alto"]].describe().round(0).to_string(), "```",
    "", "## Modos de color", "```", df["modo"].value_counts(dropna=False).to_string(), "```",
    "", "## Extensiones", "```", df["ext"].value_counts().to_string(), "```",
]
reporte = "\n".join(lineas)
print(reporte)
(OUT / "eda_plantdoc.md").write_text(reporte, encoding="utf-8")

# 4. Hoja de muestra: 1 imagen por clase
T, COLS = 180, 6
clases = list(por_clase.index)
filas = -(-len(clases) // COLS)
hoja = Image.new("RGB", (COLS * T, filas * (T + 22)), "white")
d = ImageDraw.Draw(hoja)
for i, c in enumerate(clases):
    sub = df[(df.clase == c) & df.ok]
    if sub.empty:
        continue
    with Image.open(sub["path"].sample(1, random_state=42).iloc[0]) as im:
        im = im.convert("RGB")
        im.thumbnail((T, T))
        x, y = (i % COLS) * T, (i // COLS) * (T + 22)
        hoja.paste(im, (x, y))
        d.text((x + 2, y + T + 5), c[:28], fill="black")
hoja.save(OUT / "muestra_plantdoc.jpg", quality=90)
print("\nGuardado: reports/eda_plantdoc.md y reports/muestra_plantdoc.jpg")
