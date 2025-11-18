from flet import *
from utils.api import Api


class DetailsView(View):
    pokeName = ""
    def __init__(self, page):
        super().__init__("/searchView")

        self.controls = [
            Container(
                Column(
                    [
                        Image("https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/dream-world/384.svg", height=100),
                        Stack(
                            [
                                Container(
                                    Column(
                                        [
                                            Text("Rayquaza", color="white", size=20),
                                            Container(
                                                    BarChart(
                                                    bar_groups=[
                                                        BarChartGroup(
                                                            x=0,
                                                            bar_rods=[
                                                                BarChartRod(
                                                                    from_y=0,
                                                                    to_y=40,
                                                                    width=10,
                                                                    color="green"
                                                                ),
                                                            ],
                                                        ),
                                                        BarChartGroup(
                                                            x=1,
                                                            bar_rods=[
                                                                BarChartRod(
                                                                    from_y=0,
                                                                    to_y=40,
                                                                    width=10,
                                                                    color="blue"
                                                                )
                                                            ]
                                                        ),


                                                    ],
                                                    # border=border.all(1),
                                                    left_axis=ChartAxis(
                                                        labels_size=40, title=Text("prueba"), title_size=20
                                                    ),
                                                    bottom_axis=ChartAxis(
                                                        labels=[
                                                            ChartAxisLabel(
                                                                value=0, label=Container(Text("apple"), padding=10)
                                                            ),
                                                            ChartAxisLabel(
                                                                value=1, label=Container(Text("apple"), padding=10)
                                                            ),
                                                        ],
                                                        labels_size=40
                                                    ),
                                                    horizontal_grid_lines=ChartGridLines(
                                                        color=Colors.GREY_300, width=1, dash_pattern=[3,3],
                                                    ),
                                                    max_y=110,
                                                    expand=True,
                                                ),
                                                margin=margin.all(10)
                                            )
                                        ],
                                        scroll=True
                                    ),
                                    bgcolor="#bf0000",
                                    width=page.width,
                                    border_radius=border_radius.only(top_left=10, top_right=10)
                                ),
                                IconButton(Icons.CLEAR, width=20, top=0, right=0),
                            ]
                        )
                    ]
                ),
                margin=margin.only(top=40)
            )
            
        ]

        # self.controls.append(
        #     Button("preciona", on_click=lambda x: self.open(bt))
        # )

        self.bgcolor="#dc0000"
        

    async def start(self):
        pass

    def on_handler_tap(self, e):
        pass
        # e.control.open_view()


    async def on_submit(self, e):
        pass
