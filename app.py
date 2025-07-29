import requests
import argparse

parser = argparse.ArgumentParser(description="This is a tool where you get info of random people after enetering the gender")
parser.add_argument("--gender" , required=True , type = str , help = "Enter the Gender Whose info you want.")
args = parser.parse_args()

gender = args.gender
url = requests.get(f'https://randomuser.me/api/?gender={gender}')

url = url.json()

for user in url["results"]:
    
    first_name = user["name"]["first"]
    last_name = user["name"]["last"]
    title = user["name"]["title"]

    print(f"\nName of the user is {title} {first_name} {last_name}\n")


    city  = user["location"]["city"]
    state  = user["location"]["state"]
    country  = user["location"]["country"]
    print(f"{first_name} lives in {city},{state},{country}\n")

    email = user["email"]
    print(f"Email of {first_name} is {email}\n")

    phone = user["phone"]
    print(f"Contact no. of {first_name} is {phone}\n")

    print()


if gender.lower() not in ["male" , "female"]:
    print("Enter a Valid Gender")
    exit()