
import requests


def fetch_user(user_id: int) -> None:
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        # Validate the response structure
        if not isinstance(data, dict):
            print("Invalid API response: expected a JSON object.")
            return

        if "name" not in data or "email" not in data:
            print("Invalid API response: missing name or email.")
            return

        address = data.get("address")

        if not isinstance(address, dict) or "city" not in address:
            print("Invalid API response: missing address or city.")
            return

        print("Name:", data["name"])
        print("Email:", data["email"])
        print("City:", address["city"])

    except requests.exceptions.Timeout:
        print("The request timed out. Please try again.")

    except requests.exceptions.ConnectionError:
        print("Could not connect to the API. Check your internet connection.")

    except requests.exceptions.HTTPError as error:
        print("The API returned an HTTP error:", error)

    except requests.exceptions.RequestException as error:
        print("An unexpected request error occurred:", error)


if __name__ == "__main__":
    fetch_user(1)
