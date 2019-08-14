from extract_info import extract_info

file_name = "sample.json"
actions = extract_info(file_name=file_name)
print(actions[20000][0])