# EDA PlantDoc
Imágenes: 2578 (train 2342, test 236)
Archivos no imagen: 0
Corruptas: 0
Clases: 28 | cultivos: 13 | clases 'sanas': 10
Solo en train: ['Tomato two spotted spider mites leaf']
Solo en test: []
Desbalance train (máx/mín por clase): 180/2 = 90.0x
Clases con <10 imágenes en test: 18
Imágenes duplicadas (exactas): 24 en 12 grupos
Duplicados entre train y test (fuga): 11
Duplicados con etiqueta distinta: 9

## Imágenes por clase
```
split                                 train  test  total
clase                                                   
Corn leaf blight                        180    12    192
Tomato Septoria leaf spot               140    11    151
Squash Powdery mildew leaf              124     6    130
Raspberry leaf                          112     7    119
Potato leaf early blight                109     8    117
Blueberry leaf                          106    11    117
Corn rust leaf                          106    10    116
Peach leaf                              103     9    112
Tomato leaf late blight                 101    10    111
Tomato leaf bacterial spot              101     9    110
Potato leaf late blight                  97     8    105
Strawberry leaf                          88     8     96
Apple Scab Leaf                          83    10     93
Apple leaf                               82     9     91
Tomato mold leaf                         85     6     91
Apple rust leaf                          79    10     89
Tomato Early blight leaf                 79     9     88
Tomato leaf yellow virus                 70     6     76
Bell_pepper leaf spot                    62     9     71
grape leaf                               57    12     69
Corn Gray leaf spot                      64     4     68
Soyabean leaf                            57     8     65
grape leaf black rot                     56     8     64
Tomato leaf                              55     8     63
Bell_pepper leaf                         53     8     61
Cherry leaf                              47    10     57
Tomato leaf mosaic virus                 44    10     54
Tomato two spotted spider mites leaf      2     0      2
```

## Tamaños (px)
```
        ancho    alto
count  2578.0  2578.0
mean   1068.0   911.0
std     869.0   754.0
min     115.0    69.0
25%     500.0   403.0
50%     800.0   667.0
75%    1300.0  1181.0
max    6000.0  6000.0
```

## Modos de color
```
modo
RGB     2567
CMYK       5
RGBA       5
L          1
```

## Extensiones
```
ext
.jpg     2576
.jpeg       1
.png        1
```