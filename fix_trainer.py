import json

for fname in ['Ejercicio1_clasificacion_resuelto.ipynb', 'Ejercicio1_clasificacion_resuelto_2.ipynb']:
    path = rf'd:\Textmining\{fname}'
    try:
        with open(path, 'r', encoding='utf-8') as f:
            nb = json.load(f)
    except:
        continue

    changed = False
    for cell in nb['cells']:
        if cell['cell_type'] != 'code':
            continue
        new_source = []
        for line in cell['source']:
            if 'processing_class=tokenizer' in line:
                line = line.replace('processing_class=tokenizer', 'tokenizer=tokenizer')
                changed = True
            new_source.append(line)
        cell['source'] = new_source

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, ensure_ascii=False, indent=1)
        print(f"Corregido: {fname}")
    else:
        print(f"Sin cambios: {fname}")
