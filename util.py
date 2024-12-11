import requests
import os

def get_input(day: int)-> list[str]:
    url = f"https://adventofcode.com/2024/day/{day}/input"
    session = os.environ.get("AOCSESSION")
    cookies = {'session': session}
    try:
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()
        content = response.text.rstrip('\n')
        lines = content.split('\n')
        return lines
    except requests.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return []
    except Exception as err:
        print(f"An error occurred: {err}")
        return []