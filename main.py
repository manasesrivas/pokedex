from flet import *
from utils.api import Api
import gc

    


async def main(page: Page):
    page.window.width = 400

 
    from App import App
    


    App(page)

    # page.add(app)
    
app(target=main)