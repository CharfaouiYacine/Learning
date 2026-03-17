""" So basically the idea of this project is that the user enter a name, you check if the name exist or no in GitHub, if yes the program should give some
infos about the profile such as name , location , fav repos, number of followers and so on.... """
import requests
url = "https://api.github.com/users"


def get_user_info(user_name):
    response = requests.get(f"{url}/{user_name}")
    data = response.json()
    if 'message' in data:
        print("user doesn't exist")
    else:
        print(f"Username: {data['login']}\nBio: {data['bio']}\nId:{data['id']}\nFollowers: {data['followers']}\nFollowing: {data['following']}\nLocation: {data['location']}")
def get_repos(user_name):
    response2 = requests.get(f"{url}/{user_name}/repos")
    repos = response2.json()
    if len(repos) == 0:
        print("No repos found")
    else:
        print("Repos:")
        for repo in repos[0:10]:
            print(f"{repo['html_url']}")

def main():
    user_name = input("Enter The Username to give you infos about it: ")
    get_user_info(user_name)
    get_repos(user_name)


main()
