import json

def extract_info(file_name=None):
    '''
    extract the information of a github archive json file
    returned data includes:
    "repos", "type", "actors"
    '''
    data_to_return = {
        "repos": [],
        "information": []
    }
    if file_name is None:
        return data_to_return
    f = open(file_name, "r", encoding="utf-8")
    data = f.readlines()
    for line in data:
        try:
            d = json.loads(line)
            tmp = [d["type"], d["actor"]["login"], d["repo"]["name"]]
            data_to_return["information"].append(tmp)
            if tmp[2] not in data_to_return["repos"]:
                data_to_return["repos"].append(tmp[2])
        except:
            pass

    print(len(data_to_return["information"]))
    return data_to_return