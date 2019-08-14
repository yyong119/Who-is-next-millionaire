from utils import extract_info, analyse_for_each_repo

file_name = "sample.json"
actions = extract_info(file_name=file_name)

repos = actions["repos"]
information = actions["information"]

for i in range(len(repos)):
    cnt = analyse_for_each_repo(repo_name=repos[i], data=information)
    print(cnt)