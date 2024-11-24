import json

def read_contacts(fullfile):
    try:
        with open(fullfile, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def write_contacts(contact_datas, fullfile):
    with open(fullfile, "w") as f:
        json.dump(contact_datas, f, ensure_ascii=False, indent = 4)