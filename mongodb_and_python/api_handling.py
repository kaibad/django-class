import requests

base_url = "https://prod-main-api-704464-00tre1p1erm.compute.instacloud-edge.com/api/v1"

def fetch_random_user():
    url = f"{base_url}/public/randomusers/user/random"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data:
        user_data = data["data"]
        username = user_data["login"]["username"]
        email = user_data["email"]
        country = user_data["location"]["country"]
        return {
            "username": username,
            "email": email,
            "country": country
        }
    else:
         raise Exception(f"Failed to fetch random user. Status code: {response.status_code}, Response: {data}")


def main():
    try:
        user_info = fetch_random_user()
        print("Random User Information:")
        print(f"Username: {user_info['username']}")
        print(f"Email: {user_info['email']}")
        print(f"Country: {user_info['country']}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()