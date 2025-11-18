from views.DetailsView import DetailsView
from views.FavoritesView import FavoritesView
from views.HomeView import HomeView

def GetPages(page):
    return {
        "/": HomeView(page),
        "/favorites": FavoritesView(page),
        "/detailsView": DetailsView(page)
    }