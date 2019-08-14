from extract_info import extract_info

file_name = "sample.json"
actions = extract_info(file_name=file_name)
repos = actions["repos"]
print(len(repos))
print(actions["information"][10000][0])