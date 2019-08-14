import json
def extract_info(file_name=None):
    data = []
    if file_name is None:
        return data
    f = open(file_name, "r", encoding="utf-8")
    data = f.readlines()
    for line in data:
        try:
            d = json.loads(line)
            tmp = [d["type"], d["actor"]["login"], d["repo"]["name"]]
            data.append(tmp)
        except:
            pass
    print(len(data))
    return data