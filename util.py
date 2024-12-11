import requests

def get_input(day: int)-> list[str]:
    url = f"https://adventofcode.com/2024/day/{day}/input"
    session = "53616c7465645f5fd0a500e8412f0b98f627e468aaecb231b51fe287be23598166a8e8aa3173b695f7703ff76b1bae6d622bfb0a1c99cd81ec63535ce505b78f"
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