# Weather
Temperature API that returns the maximum, minimum, average and median temperature forecast in Celcius for a city within a number of days

![alt text](https://github.com/mwangistan/weather/blob/main/static/temp.png)

### Prerequisites
```
python 3.6.9
virtualenv
```

### Installation

1. Clone the repo
```
git clone https://github.com/mwangistan/weather.git
```

2. Cd to the project directory
```
cd weather
```

3. Create a virtualenv and activate it
```
virtualenv -p python3 .env
source .env/bin/activate
```

4. Install project requirements located in the repo's requirements.txt file in the virtual environment
```
pip3 install -r requirements.txt
```

## Start the server
To start the django server run 
```
python manage.py runserver
```

## Usage
The API url is 
```
/api/locations/{city}/?days={number_of_days}
```
Where the 
{city} = city name for which to get forecast data e.g Nairobi
{number_of_days} = number of days of forecast required. 
**Days should range between 1 and 10**

## Running tests
To run the unit tests
```
python manage.py test
```


## API Errors
If there is an error, the API response contains the error message and status code

| HTTP code     | Description                                                         |
| ------------- |:-------------------------------------------------------------------:|
| 400           |  Field validation error. The API will provide the exact field     error in the response                                                                 |
| 500           | This is an internal server error                                    |

## License

This project is licensed under the MIT License

