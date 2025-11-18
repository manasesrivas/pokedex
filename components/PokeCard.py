from flet import *
from .ProgressRing import progressRing

def create_card():
    return Stack(
        [
            Container(
                content=progressRing,
                bgcolor="red",
                border_radius=10,
                padding=padding.all(10),
                alignment=alignment.center,
                expand=1
            )
        ]
    )
