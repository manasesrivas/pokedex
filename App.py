from flet import *
import routes

class App:
    
    def __init__(self, page):
        self.page = page



        self.navigationBar = self.initNavigationbar()

        self.PAGES = routes.GetPages(self.page)


        self.page.on_resized = self.on_resized
        self.page.on_route_change = self.on_route_change
        self.page.go("/detailsView")


    async def on_route_change(self, e):
        self.page.views.clear()
        page = self.PAGES[self.page.route]
        page.navigation_bar = self.navigationBar

        page.page = self.page
        self.page.views.append(page)
        await page.start()
        self.page.update()
        
    def on_change_navbar(self, e):
        self.page.go(self.navigationBar.destinations[e.control.selected_index].data)

    def on_resized(self, e):
        gridView = self.page.views[0].gridView
        imgs = self.page.views[0].gridView.controls
        for img in imgs:
            pokeImagen = img.controls[0].content.controls[0]

            pokeImagen.height = gridView.getImgHeight()
    
        self.page.update()

    def initNavigationbar(self):
        return NavigationBar(
            destinations=[
                NavigationBarDestination(
                    icon=Icons.SEARCH,
                    label="Pokemons",
                    data="/"
                ),
                NavigationBarDestination(
                    icon=Icons.FAVORITE_BORDER_ROUNDED,
                    label="Favoritos",
                    data="/favorites"
                )
            ],
            bgcolor="#dc0000",
            indicator_color="red",
            elevation=20,
            on_change=self.on_change_navbar
        )