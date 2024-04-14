api_key = "141f1e2933d63a5393594213470a9ccd"
import requests  # requests is a library for making HTTP requests


# to get data from an API
def get_data(place, forecast_days=None, kind=None):
    url = (f"http://api.openweathermap.org/data/2.5/forecast?"
           f"q={place}&appid={api_key}")
    # http://api.openweathermap.org/data/
    # 2.5/forecast?q=tokyo&appid=141f1e2933d63a5393594213470a9ccd

    # at this point it is a good idea to test tha data works by running
    # the url in the browser as shown above

    response = requests.get(url)  # sends a GET request
    data = response.json()  # converts the response to a JSON
    filtered_data = data["list"]
    len(filtered_data)  # this will return the number 40 which is the
    # number of forecasts you have before your free subscription runs
    # out 40 values for 5 days which is 8 for 24 hours
    nr_values = 8 * forecast_days  # 8 data sets per day
    filtered_data = filtered_data[0:nr_values]
    # 0:8 is the first 8 values
    return filtered_data


if __name__ == "__main__":
    # makes sure this script is only triggered when it is executed directly
    print(get_data(place="Tokyo", forecast_days=3))
# good point to test the data at
