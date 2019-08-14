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
    import json
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

def analyse_for_each_repo(repo_name=None, data=None):
    '''
    analyse the feature of a repository when it grows quickly
    '''
    actions_of_the_repo = []
    action_count = {
        "PushEvent": 0,
        "IssueCommentEvent": 0,
        "GollumEvent": 0,
        "PullRequestReviewCommentEvent": 0
    }
    action_names = ["PushEvent", "IssueCommentEvent", "GollumEvent", "PullRequestReviewCommentEvent"]
    for i in data:
        if i[2] == repo_name:
            actions_of_the_repo.append(i)
            if i[1] in action_names:
                action_count[i[1]] += 1
    print(actions_of_the_repo)
    return action_count