import aiohttp

# async def llamar(e):
        # return str(r.json()["sprites"]["other"]["dream_world"]["front_default"])

class Api:
    BASE_URL = "https://pokeapi.co/api/v2/"
    LEN_POKEMONS = 100

    request: dict = {}

    def __aenter__(self):
        pass


    async def get_pokemon(self, query: str):
        self.request = await self.httpGet(f"pokemon/{query}")
        return self.request
    
    def getPokeName(self):
        return self.request["name"].capitalize()

    def getPokeImg(self):
        return self.request["sprites"]["other"]["dream_world"]["front_default"]

    async def httpGet(self, query: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(self.BASE_URL+query) as response:
                request = await response.json()
                return request
                
    
    def getAboutAbility(self):
        reque = self.httpGet("pokemon/")
        for i in reque["results"]:
            print(i)

    async def getPokemons(self):
        request = await self.httpGet(f"pokemon?limit={self.LEN_POKEMONS}&offset=0")
        return request["results"]
    
    async def __aexit__(self):
        pass
# /pokemon/{id or name}/ para un poquemon en especifico


# https://pokeapi.co/api/v2/ability/{id or name}/ para tener
# varios depende de las habilidades
