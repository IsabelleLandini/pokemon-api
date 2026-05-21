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