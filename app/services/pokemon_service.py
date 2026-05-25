from app.clients.pokeapi_client import PokeAPIClient
from app.core.redis import redis_client
from redis.exceptions import ConnectionError
import json
import asyncio

class PokemonNotFound(Exception):
    pass

class PokemonService:
    def __init__(self):
        self.client = PokeAPIClient()

    async def get_pokemon(self, name:str):
        cache_key = f'pokemon:{name}'

        try: 
            cached_pokemon = await redis_client.get(cache_key)

            if cached_pokemon:
                return json.loads(cached_pokemon)
            
        except ConnectionError:
            pass
            
        data = await self.client.get_pokemon(name)

        if not data:
            raise PokemonNotFound(f'Pokemon {name} not found.')
        
        # normalização do dados
        pokemon_data = {
            'id': data['id'],
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [
                t['type']['name'] 
                for t in data['types']
            ],
            'sprites': {
                'front_default': data['sprites']['front_default'],
                'back_default': data['sprites']['back_default']
            },
            'stats': {
                stat['stat']['name']: stat['base_stat']  
                for stat in data['stats']  
            }    
        }

        try: 
            await redis_client.set(
                cache_key,
                json.dumps(pokemon_data),
                ex=3600
            )
        except ConnectionError:
            pass

        return pokemon_data
    
    async def get_pokemons(
        self,
        limit: int = 20,
        offset: int = 0
    ):
        
        data = await self.client.get_pokemons(
            limit=limit,
            offset=offset
        )

        tasks = [
            self.client.get_pokemon(pokemon['name'])
            for pokemon in data['results']    
        ]

        results = await asyncio.gather(*tasks)

        pokemons = []

        for pokemon, details in zip(data['results'], results):

            pokemons.append({
                'id': details['id'],
                'name': pokemon['name'],
                'height': details['height'],
                'weight': details['weight'],
                'types': [
                    t['type']['name']
                    for t in details['types']
                ],
                'sprites': {
                    'front_default': details['sprites']['front_default'],
                    'back_default': details['sprites']['back_default']
                }
            })

        return {
            'data': pokemons,
            'pagination': {
                'total': data['count'],
                'limit': limit,
                'offset': offset,
                'next': (
                    f'/pokemons?limit={limit}&offset={offset + limit}' 
                    if offset + limit < data['count'] 
                    else None
                ),

                'previous': (
                    f'/pokemons?limit={limit}&offset={max(offset - limit, 0)}'
                    if offset > 0 
                    else None
                )
            }   
        }
    

    