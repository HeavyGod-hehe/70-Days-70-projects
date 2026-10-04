import requests



def fetch_page(url):
    custom_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
    try:
        response = requests.get(url,headers=custom_headers,timeout=5)
        if response.status_code == 200:
            return response.text
        else:
            print(f"Failed to Get the Data Status Code : {response.status_code}")
    except requests.exceptions.Timeout:
        print("The request timed out! The server took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"{e} Issue")

if __name__=="__main__":
    var = fetch_page("https://en.wikipedia.org/wiki/Artificial_intelligence")
    if var is None:
        print("Error")
    else:
        print(var[:200])
