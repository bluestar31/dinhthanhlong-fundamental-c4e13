from haversine import haversine

cities = [
    {
        'name': 'Hà Nội',
        'lat': 21.0277644,
        'long': 105.83415979999995
    },
    {
        'name': 'Đà Nẵng',
        'lat': 16.0544068,
        'long': 108.20216670000002
    },
    {
        'name': 'TP Hồ Chí Minh',
        'lat': 10.8230989,
        'long': 106.6296638
    },
    {
        'name': 'Nha Trang',
        'lat': 12.2387911,
        'long': 109.19674880000002
    }
]

n = len(cities)

for i in range(0, n - 1):
    for j in range(i + 1, n):
        city1 = cities[i]
        city2 = cities[j]

        # haversine
        cord1 = [city1['lat'], city1['long']]
        cord2 = [city2['lat'], city2['long']]

        distance = haversine(cord1, cord2)

        print('Khoảng cách từ {0} đến {1} là {2}'.format(city1['name'], city2['name'], distance))
