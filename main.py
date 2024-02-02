from fastapi import FastAPI
from route import get_cities_route, get_city_route, create_city, delete_city

app = FastAPI()

@app.get("/")
def root():
    return {"Hello":"World"}

@app.get('/cities')
def get_cities():
    return get_cities_route

@app.get('/cities/{city_id}')
def get_city(city_id: int):
    return get_city_route(city_id)