import json

def get_data(fayl):
    try:
        with open(fayl, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return []

def save_data(fayl, malumot):
    with open(fayl, 'w', encoding='utf-8') as f:
        json.dump(malumot, f, ensure_ascii=False, indent=2)

def get_new_id(malumotlar):
    if not malumotlar:
        return 1
    return max([m.get('id', 0) for m in malumotlar]) + 1

