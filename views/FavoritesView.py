from components.ContentGridView import ContentGridView
from constants import *
from flet import *
from utils.manageDatabase import sqlite
from utils.api import Api

class FavoritesView(View):
    def __init__(self, page):
        super().__init__("/favorites")
        self.page = page
        self.route = "/favorites"
        self.bgcolor=BACKGROUND_COLOR
        self.searchBar = self.initSearchBar()
        self.gridView = self.initGridView()
        self.controls = [
            Container(
                content=Column(
                    [   
                        Text(
                            "Favoritos",
                            color="white",
                            size=40,
                            weight=FontWeight.W_600
                        ),
                        self.gridView
                    ]
                ),
                margin=margin.only(top=MARGIN_TOP),
            )
        ]

        self.gridView.data = []

        from asyncio import create_task



    async def start(self):
        self.gridView.page = self.page
        async with sqlite() as db:
            pokemons = await db.selectFavorites()
            print(f"contenido de la data de gridview: {self.gridView.data}")
            self.gridView.controls.clear()
            for pokemon in pokemons:
                await self.drawPokemon(pokemon[0], pokemon[1])

            
    def initSearchBar(self):
        return SearchBar(
            view_elevation=4,
            # height=40,
            bar_hint_text="Busca un pokemon",
        )
    

    def initGridView(self):
        return ContentGridView(self.page)
    
    
    async def drawPokemon(self, pokeName, url):
        card = self.gridView.pushCard()
        card.controls[0].content = self.gridView.createContent(
            url,
            pokeName
        )

        card.controls.append(
            await self.gridView.putLikeButtonIcon((pokeName, url))
        )
        self.page.update()
        

    def showSnackBar(self, msg):
        self.page.open(
            SnackBar(
                Text(msg),
                show_close_icon=True
            )
        )
        self.page.update()