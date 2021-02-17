from statistics import mean, median

class Parser:
    @staticmethod
    def get_maximum(data):
        days_max_temp = [i['day']['maxtemp_c'] for i in data]
        return max(days_max_temp)

    @staticmethod
    def get_minimum(data):
        days_min_temp = [i['day']['mintemp_c'] for i in data]
        return min(days_min_temp)

    @staticmethod
    def get_average(data):
        all_temps = []
        for day in data:
            for hour in day['hour']:
                all_temps.append(hour['temp_c'])

        avg = mean(all_temps)
        return round(avg, 2)

    @staticmethod
    def get_median(data):
        all_temps = []
        for day in data:
            for hour in day['hour']:
                all_temps.append(hour['temp_c'])

        med = median(all_temps)
        return round(med, 2)
