import requests

def get_world_bank_data(api_url, indicator, country_code):
    url = f"{api_url}/country/{country_code}/indicator/{indicator}?format=json"
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    # API URL for World Bank
    api_url = "https://api.worldbank.org/v2"

    # Indicator code for GDP (Gross Domestic Product)
    indicator = "NY.GDP.MKTP.CD"

    # Country code for the United States
    country_code = "USA"

    try:
        # Retrieve data from the World Bank API
        data = get_world_bank_data(api_url, indicator, country_code)

        # Print the first data point (latest value)
        latest_data = data[1][0]
        print(f"GDP of {latest_data['country']['value']} in {latest_data['date']}: {latest_data['value']}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred: {e}")
