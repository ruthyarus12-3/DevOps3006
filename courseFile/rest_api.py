import requests
# response = requests.get("http://localhost:5001")
# expected = "hello and welcome to the world of games"
# actual = response.text
# assert expected == actual

# response = requests.post("http://localhost:5001/whatismyname")
# expected = "saved new car"
# actual = response.text
# assert expected == actual

response = requests.post("http://localhost:5001/whatismyname", data="aaa")
expected = "saved new car"
actual = response.text
assert expected == actual