from flet import  *
from constants import RUNS_COUNT, PERCENT_LESS_TO_WIDTH
from .PokeCard import create_card
from utils.manageDatabase import sqlite

class ContentGridView(GridView):

    def __init__(self, page):
        super().__init__()
        self.runs_count=RUNS_COUNT
        self.page = page
        self.height = page.height - (0.3 * page.height)
        self.expand = 1
        self.child_aspect_ratio = 1.0
        self.spacing = 5
        self.run_spacing = 5
        

        

    
    def pushCard(self):
        card = create_card()
        self.controls.append(card)
        self.page.update()
        return card
    

    
    def getImgHeight(self) -> int:
        return (self.page.width/2)-(PERCENT_LESS_TO_WIDTH * self.page.width)
    
    '''
    metodos para la los cards
    '''
    
    async def iLikeIt(self, e):
        pokeData = e.control.data
        icon = Icons.FAVORITE
        msg = "Se agregó a tus favoritos"
        async with sqlite() as db:
            query = await db.existPokemon(pokeData[0])
            if query == None:
                await db.insertPoke(pokeData)
                
            elif query[2] == True:
                await db.changePokeFavorite((False, pokeData[0]))
                icon = Icons.FAVORITE_OUTLINE_SHARP
                msg = "Se eliminó de tus favoritos"
                
            else: 
                await db.changePokeFavorite((True, pokeData[0]))
        self.page.open(
            SnackBar(
                Text(msg),
                show_close_icon=True
            )
        )
        e.control.icon = icon
        self.page.update()

    async def putLikeButtonIcon(self, pokeData):
        return IconButton(
                icon=await self.verifyIcon(pokeData[0]),
                right=0, 
                top=0, 
                icon_color="#7a0000",
                on_click=self.iLikeIt,
                data=pokeData
        )
    
    async def verifyIcon(self, pokeName):
        icon = Icons.FAVORITE_OUTLINE_SHARP
        async with sqlite() as db:
            res = await db.existPokemon(pokeName)
            if res != None and res[2] == True:
                icon = Icons.FAVORITE
    
        return icon
    
    def createContent(self, pokeImg, pokeName):
        
        content = Column(
                [
                    Image(pokeImg, height=self.getImgHeight()),
                    Text(
                        pokeName,
                        color="white", 
                        weight=FontWeight.W_500
                    ),
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER
            )
        
        self.page.update()

        return content
    
    """
    funciones para la cambiar a la pagina de detalles
    """

    def changeToDetails(self, e):
        self.page.go("/detailsView")