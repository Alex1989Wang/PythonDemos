from weather_station import get_description as do_it
import sys

description = do_it() 
print("Today's weather is:", description)


# system files path
for place in sys.path:
    print(place)

