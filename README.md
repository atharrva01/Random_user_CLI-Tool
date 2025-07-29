# 🧑‍💻 Random User CLI Tool

A simple Python command-line interface (CLI) tool that fetches and displays random user information based on gender using the [randomuser.me](https://randomuser.me) API.

---

## 🚀 Features

- Get a random user profile based on gender
- Outputs:
  - Full Name
  - Location (City, State, Country)
  - Email Address
  - Phone Number
- Fast and lightweight CLI experience

---

## 📦 Requirements

- Python 3.x
- `requests` module

Install dependencies:

```bash
pip install requests
⚙️ Usage
bash
Copy
Edit
python random_user_cli.py --gender male
Options:

--gender: Specify the gender of the user to fetch
Accepts: male or female

📋 Example Output
pgsql
Copy
Edit
Name of the user is Mr John Doe
John lives in Paris, Île-de-France, France
Email of John is johndoe@example.com
Contact no. of John is 01-23-45-67-89
🧠 How It Works
Takes gender input using argparse

Sends a GET request to the API endpoint:
https://randomuser.me/api/?gender=male

Parses the JSON response

Prints formatted output to the console

📁 Project Structure
objectivec
Copy
Edit
RandomUser-CLI/
├── random_user_cli.py
└── README.md
🙋‍♂️ Author
Atharva

Building tools daily as part of a 30-day transformation challenge before college 🚀

🌐 API Reference
https://randomuser.me/

✅ License
This project is open-source and free to use.

yaml
Copy
Edit

---

Let me know once it’s pushed — and we’ll jump to **Tool 2: News CLI.**
