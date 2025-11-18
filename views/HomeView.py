from flet import View
from components.ContentGridView import ContentGridView
from constants import *
from flet import *
from utils.api import Api
from utils.manageDatabase import sqlite
from asyncio import create_task


class HomeView(View):
    inicialized = False

    def __init__(self, page):

        super().__init__("/")
        
        self.page = page
        self.bgcolor=BACKGROUND_COLOR
        self.searchBar = self.initSearchBar()
        self.gridView = self.initGridView()
        self.controls = [
            Container(
                content=Column(
                    [
                        self.searchBar,
                        self.gridView
                    ]
                ),
                margin=margin.only(top=MARGIN_TOP),
            )
        ]

        self.gridView.data = []

    
    def initSearchBar(self):
        return SearchBar(
            view_elevation=4,
            height=40,
            bar_hint_text="Busca un pokemon",
            on_tap=self.on_tap,
            controls=[],
            view_leading=IconButton(icon=Icons.ARROW_BACK_IOS_SHARP, on_click=self.close_search),
            on_submit=self.on_submit
        )
    

    def initGridView(self):
        return ContentGridView(self.page)
    
    def close_search(self, e):
        self.searchBar.close_view("")
        # self.page.update()

    async def on_submit(self, e):
        if self.searchBar.value == "": return
        if sum(1 for i in self.gridView.controls if i.visible) == 1: self.gridView.controls.pop(-1)
        for i in self.gridView.controls: i.visible = False
        self.searchBar.bar_leading = IconButton(Icons.ARROW_BACK_IOS_SHARP, on_click=self.on_return)
        self.page.update()
        await self.drawPokemon(self.searchBar.value)

    def on_return(self, e):
        self.searchBar.bar_leading = None
        self.searchBar.value = ""
        self.gridView.controls.pop(-1)
        for i in self.gridView.controls: i.visible = True

        self.page.update()

    def on_tap(self, e):
        pass
        # self.searchBar.open_view()
        # self.page.update()

    async def start(self):
        if self.inicialized: 
            async with sqlite() as db:
                pokemons = [pokemon[0] for pokemon in await db.selectFavorites()]
                print(pokemons)
                for i in self.gridView.controls:
                    if i.controls[0].content.controls[1].value not in pokemons:
                        i.controls[1].icon = Icons.FAVORITE_OUTLINE_SHARP
            self.page.update()
            return


        self.inicialized = True
        api=Api()
        pokemons = await api.getPokemons()
        for pokemon in pokemons:
           self.gridView.data.append(pokemon["name"])
           await self.drawPokemon(pokemon["name"])


    async def drawPokemon(self, pokeName):
        api = Api()
        card = self.gridView.pushCard()
        try:
            await api.get_pokemon(pokeName)
        except:
            self.showSnackBar("Pokemon NO encontrado")
            self.on_return(None)
            return

        pokeImg = api.getPokeImg()
        pokeNam = api.getPokeName()
        card.controls[0].content = self.gridView.createContent(
            pokeImg,
            pokeNam
        )

        card.controls.append(
            await self.gridView.putLikeButtonIcon((pokeNam ,pokeImg))
        )

        card.controls[0].on_click = self.gridView.changeToDetails

        self.page.update()
        

    def showSnackBar(self, msg):
        self.page.open(
            SnackBar(
                Text(msg),
                show_close_icon=True
            )
        )
        self.page.update()