from fastapi import FastAPI
from route import get_cities_route, get_city_route, create_city_route, delete_city_route

app = FastAPI()

@app.get("/")
async def root():
    return await {"Hello":"World"}

@app.get('/cities')
async def get_cities():
    return await get_cities_route

@app.get('/cities/{city_id}')
async def get_city(city_id: int):
    return await get_city_route(city_id)

@app.post('cities')
async def create_city(city:City):
    return await create_city_route(city)

@app.delete('cities/{citiy_id}')
async def delete_city(citiy_id: int):
    return await delete_city_route(citiy_id)