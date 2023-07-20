import requests

def post_request(url, data):
    response = requests.post(url, json=data)
    return response

def get_request(url):
    response = requests.get(url)
    return response

def main():
    endpoint = "http://127.0.0.1:8000/dishes"
    with open("query.txt", "r") as query_file:
        for name in query_file:
            data = {"name": name.strip()}
            dish_id = post_request(endpoint, data).json()
            response = get_request(f"{endpoint}/{dish_id}").json()
            with open("response.txt", "a") as results_file:
                results_file.write(f"{name} contains {response['cal']} calories, {response['sodium']} mgs of sodium, and {response['sugar']} grams of sugar\n")
if __name__ == "__main__":
    main()