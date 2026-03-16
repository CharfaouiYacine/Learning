""" So basically the idea of this project is that the user enter a name, you check if the name exist or no in GitHub, if yes the program should give some
infos about the profile such as name , location , fav repos, number of followers and so on.... """
import requests
user_name = input("Enter The Username to give you infos about it: ")
api_url = "https://api.github.com/users/"+user_name
response = requests.get(api_url)
data = response.json() # this case the type will be a dict
if 'message' in data:
    print("user doesn't exist")
else:
    print(f"Username: {data['login']}\nBio: {data['bio']}\nId:{data['id']}\nFollowers: {data['followers']}\nFollowing: {data['following']}\nLocation: {data['location']}")
    print(response.status_code)
    repos_url = "https://api.github.com/users/"+user_name+"/repos"
    response2 = requests.get(repos_url)
    data2 = response2.json() # in this case the type will be a list of dicts
    print(response2.status_code)
    print("Repos:")
    for i in data2:
        print(f"{i['html_url']}")
