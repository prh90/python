cities = ["Adelaide", "Alice Springs", "Darwin", "Melbourne", "Brisbane", "Sydney"]
with open("c:/Users/pablo/Desktop/cities.txt", 'w') as city_file:
    for city in cities:
        print(city, file=city_file)
