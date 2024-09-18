import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"



def convert_date(iso_string):
    
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date = datetime.fromisoformat(iso_string)
    readable_date = date.strftime("%A %d %B %Y")
    return readable_date
    


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    c_temp = ((float(temp_in_fahrenheit) -32) * (5 / 9))
    round_c_temp = round(c_temp, 1)
    return round_c_temp


from statistics import mean
def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    for num in range(0, len(weather_data)):
        weather_data[num] = float(weather_data[num])

    mean_value = float(mean(weather_data))
    return mean_value


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        print(reader)
        new_list = []

        for line in reader:
            if line:
                new_list.append([line[0], int(line[1]), int(line[2])])
    return new_list 


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data != []:
        min_value = min(weather_data)
        min_index = weather_data.index(min_value)
    
        for item in weather_data:
            if weather_data.count(item) == 2:
                return (float(weather_data[-1]), len(weather_data)-1)
            else:
                return float(min_value), min_index
    else: 
        return ()


    
    




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if weather_data != []:
        max_value = max(weather_data)
        max_index = weather_data.index(max_value)
        for item in weather_data: 
            if weather_data.count(max_value) == 2:
                return (float(max_value), weather_data.index(max_value, weather_data.index(max_value) + 1))
            else:
                return (float(max_value), (max_index))
    else:
        return ()


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    dates = []
    min_temps_f = []
    max_temps_f = []

    for day in weather_data:
        dates.append(day[0])
        min_temps_f.append(find_min(day[1:]))
        max_temps_f.append(find_max(day[1:]))

    all_mins = []
    min_indexes = []
    for item in min_temps_f:
        (min_temps, min_temps_index) = item
        all_mins.append(min_temps)
        min_indexes.append(min_temps_index)

    (min_of_mins, min_date_index) = find_min(all_mins)
  
    min_temps_date = dates[min_date_index]

    min_date_convert = convert_date(min_temps_date)
    min_of_c = convert_f_to_c(min_of_mins)

    all_maxes = []
    max_indexes = []
    for item in max_temps_f:
        (max_temps, max_temps_index) = item
        all_maxes.append(max_temps)
        max_indexes.append(max_temps_index)

    (max_of_maxes, max_date_index) = find_max(all_maxes)
  
    max_temps_date = dates[max_date_index]

    max_date_convert = convert_date(max_temps_date)
    max_of_c = convert_f_to_c(max_of_maxes)

    avg_low = convert_f_to_c(mean(all_mins))
    avg_high = convert_f_to_c(mean(all_maxes))
        
            
    # replace hardcoded strings with your variables
    summary = (
        f"{len(weather_data)} Day Overview\n"
        f"  The lowest temperature will be {min_of_c}°C, and will occur on {min_date_convert}.\n"
        f"  The highest temperature will be {max_of_c}°C, and will occur on {max_date_convert}.\n"
        f"  The average low this week is {avg_low}°C.\n"
        f"  The average high this week is {avg_high}°C.\n"
    )

    return summary





def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    summary = ""

    for data in weather_data:
        date = data[0]
        min_temp_c = convert_f_to_c(float(data[1]))
        max_temp_c = convert_f_to_c(float(data[2]))
        print(min_temp_c)
        print(max)
    
        
        summary += (
           f"---- {convert_date(date)} ----\n"
           f"Minimum Temperature: {min_temp_c}°C\n"
           f"Maximum Temperature: {max_temp_c}°C\n\n"
        )
        
    return summary 
   