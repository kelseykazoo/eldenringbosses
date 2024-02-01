import requests

api_url = "https://eldenring.fanapis.com/api/bosses"


def get_boss_details(boss_name):
    try:
        
        response = requests.get(api_url)

        
        if response.status_code == 200:
            
            boss_data = response.json()

            
            bosses = boss_data.get('data', [])
            for boss in bosses:
                if boss['name'].lower() == boss_name.lower():
                    print(f"Boss Name: {boss['name']}")
                    print(f"Location: {boss['location']}")
                    break
            else:
                print(f"No information found for the boss: {boss_name}")
        else:
            
            print(f"Error: Unable to fetch boss data (Status code: {response.status_code})")

    except Exception as e:
        print(f"Error: {e}")

user_input = input("Enter the name of the boss: ")


get_boss_details(user_input)