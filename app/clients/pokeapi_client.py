import httpx

class PokeAPIClient:
    BASE_URL = 'https://pokeapi.co/api/v2'

    async def get_pokemon(self, name:str):
        url = f'{self.BASE_URL}/pokemon/{name.lower()}'

        async with httpx.AsyncClient() as client:
            response = await client.get(url)

        if response.status_code != 200:
            return None
        
        return response.json()
    