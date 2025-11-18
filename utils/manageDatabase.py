import aiosqlite

class sqlite:
    tableName = "poke_favorites"
    async def __aenter__(self):
        self.connection = await aiosqlite.connect("db.db")
        await self.connection.execute("CREATE TABLE IF NOT EXISTS poke_favorites(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, url TEXT, visible INTEGER DEFAULT 1)")
        await self.connection.commit()
 
        return self
    

    async def selectAll(self):
        cursor = await self.connection.execute("SELECT name, url, visible FROM poke_favorites")
        selecetAll = await cursor.fetchall()
        await cursor.close()
        return selecetAll
    
    async def selectFavorites(self):
        async with self.connection.execute("SELECT name, url, visible FROM poke_favorites WHERE visible = 1") as cursor:
            res = await cursor.fetchall()
            return res

    async def existPokemon(self, name):
        async with self.connection.execute("SELECT name, url, visible FROM poke_favorites WHERE name = ? COLLATE NOCASE", (name, )) as cursor:
            res = await cursor.fetchone() 
            return res

    async def insertPoke(self, data):
        await self.connection.execute("INSERT INTO poke_favorites(name, url) VALUES (?, ?)", data)
        await self.connection.commit()

    async def changePokeFavorite(self, pokeData):
        await self.connection.execute("UPDATE poke_favorites SET visible = ? WHERE name = ?", pokeData)
        await self.connection.commit()

    async def deleteTable(self):
        await self.connection.execute("DROP TABLE IF EXISTS poke_favorites")
        
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.connection.close()

        

async def main():
    async with sqlite() as a:
        # "registro 1" ya esta ejecutado
        # await a.insertPoke(("registro 1", "url de registro 1"))
        # await a.insertPoke(("registro 2", "url de registro 2"))
        # await a.insertPoke(("registro 3", "url de registro 3"))
        # await a.insertPoke(("registro 4", "url de registro 4"))
        # print(await a.existPokemon("registro 1"))
        # print(await a.existPokemon("bulbasaur"))
        # await a.deleteTable()
#         await a.changePokeFavorite((False, "registro 1"))
        selectAll = await a.selectAll()
        name = selectAll[0][2]
        for i in selectAll:
            print(i)
        print(f'Nombre pokemon {name}')
        print(f'existe pokemon {await a.existPokemon(name)}')

import asyncio

# asyncio.run(main())