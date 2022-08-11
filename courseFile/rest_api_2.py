import requests
# https://api.github.com/users/avielb/repos
# http://localhost:5001/whatismyname
response = requests.get("https://api.github.com/users/avielb/repos")
# json() takes the http response and convert it to be python object
result = []
for repo in response.json():
    result.append(repo["full_name"])

print(result)

# we can write the same in one row
result = [repo["full_name"] for repo in response.json()]

# I want to get repositories contain the string "first"
repos_with_first = [repo["full_name"] for repo in response.json() if repo["full_name"] == 'first']
for repo in repos_with_first:
    print(repo)

repos_private_false = [repo["full_name"] for repo in response.json() if repo["private"] == False]
for repo in repos_with_first:
    print(repo)

repos_with_two_values = [{"name": repo["full_name"], "tags": repo["git_tags_url"]} for repo in response.json() if repo["private"] == False]

for repo in repos_with_two_values:
    print(repo)
# full
# for repo in response.json():
#     if "first" in repo["full_name"]:
#         result.append(repo["full_name"])