import requests

db = []

def get_cities_route():
    results = []
    for city in db:
        strs = "http://worldtimeapi.org/timezone/Asia/Seoul"
        r = requests.get(strs)
        cur_time = r.json()['datetime']
        results.append({'name':city['name']}, {'timezone':city['timezone']}, {'current_time':cur_time})
    return results

def get_city_route(city_id):
    city = db[city_id-1]
    strs= f"http://worldtimeapi.org/timezone/{city['timezone']}"
    r = requests.get(strs)
    cur_time = r.json()['datetime']
    return {'name':city['name'], 'timezone':city['timezone'], 'current_time':cur_time}

def create_city_route(city):
    db.append(city.dict())
    return db[-1]

def delete_city_route(city_id):
    delete_city = db[city_id-1]
    db.pop(city_id-1)
    return delete_city