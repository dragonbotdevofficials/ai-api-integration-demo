import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_users():
response = requests.get(f"{BASE_URL}/users")
response.raise_for_status()
return response.json()

def display_users(users):
for user in users[:5]:
print(f"Name: {user['name']}")
print(f"Email: {user['email']}")
print("-" * 30)

if **name** == "**main**":
users = fetch_users()
display_users(users)
