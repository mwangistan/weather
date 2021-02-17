from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    days = serializers.IntegerField()
    city = serializers.CharField(max_length=20)

    def validate_days(self, days):
        if int(days) < 1 or int(days) > 10:
            raise serializers.ValidationError("Days range should be between 1 and 10")
        return days

    def validate_city(self, city):
        if city.isnumeric():
            raise serializers.ValidationError("No location found matching the city")
        return city
