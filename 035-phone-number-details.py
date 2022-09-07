import phonenumbers as ph
from phonenumbers import carrier, geocoder, timezone

number = "+18668323090"
number = ph.parse(number)

print(timezone.time_zones_for_number(number))
print(carrier.name_for_number(number, "en"))
print(geocoder.description_for_number(number, "en"))
