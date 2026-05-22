from app.clients.pokeapi_client import PokeAPIClient

class PokemonService:
    def __init__(self):
        self.client = PokeAPIClient()

    async def get_pokemon(self, name:str):
        data = await self.client.get_pokemon(name)

        if not data:
            return None
        
        # normalização do dados
        return {
            'id': data['id'],
            'name': data['name'],
            'height': data['height'],
            'weight': data['weight'],
            'types': [t['type']['name'] for t in data['types']],
            'sprite': data['sprites']['front_default'],
            'stats': {
                stat['stat']['name']: stat['base_stat']  
                for stat in data['stats']  
            }    
        }
    async def get_pokemons(
        self,
        limit: int = 20,
        offset: int = 0
    ):
        
        data = await self.client.get_pokemons(
            limit=limit,
            offset=offset
        )

        pokemons = []

        for pokemon in data['results']:
            details = await self.client.get_pokemon(
            pokemon['name']
            )

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
                'next': data['next'],
                'previous': data['previous']
            }    
        }
    