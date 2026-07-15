import json

with open(r'd:\Textmining\Ejercicio1_clasificacion_resuelto.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for cell in nb['cells']:
    if cell['cell_type'] == 'code' and '!pip install datasets' in ''.join(cell['source']):
        cell['source'] = [
            "# Instalamos dependencias (solo lo que Colab no trae)\n",
            "!pip install -q datasets --upgrade\n",
            "!pip install -q evaluate\n",
            "!pip install -q wordcloud\n",
            "!pip install -q accelerate>=0.21.0\n",
            "!pip install -q torchvision --upgrade\n",
        ]
        break

with open(r'd:\Textmining\Ejercicio1_clasificacion_resuelto.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Fix aplicado.")
