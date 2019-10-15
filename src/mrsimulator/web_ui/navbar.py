# -*- coding: utf-8 -*-
import dash_bootstrap_components as dbc
import dash_html_components as html
import base64
from os.path import join, split


folder = split(__file__)[0]
mrsimulator_logo = join(folder, "resource/mrsimulator-dark-featured.png")
encoded_image = base64.b64encode(open(mrsimulator_logo, "rb").read())

search_bar = dbc.Row(
    [
        dbc.Col(dbc.Input(type="search", placeholder="Search")),
        dbc.Col(dbc.Button("Search", color="primary", className="ml-2"), width="auto"),
    ],
    no_gutters=True,
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)


nav_items = dbc.Row(
    [
        dbc.Col(
            dbc.NavLink(
                "Documentation",
                href="https://mrsimulator.readthedocs.io/en/stable/",
                className="navbar-light expand-lg",
            )
        ),
        dbc.Col(
            dbc.NavLink(
                children=[html.I(className="fab fa-github-square"), "Github"],
                href="https://github.com/DeepanshS/mrsimulator",
            )
        ),
    ],
    className="ml-auto flex-nowrap mt-3 mt-md-0",
    align="center",
)

navbar_top = dbc.Navbar(
    [
        dbc.Row(
            [
                dbc.Col(
                    html.Img(
                        src="data:image/png;base64,{}".format(encoded_image.decode()),
                        height="60px",
                    )
                )
            ],
            align="center",
            no_gutters=True,
        ),
        dbc.NavbarToggler(id="navbar-toggler"),
        dbc.Collapse([nav_items], id="navbar-collapse", navbar=True),
    ],
    color="dark",
    sticky="top",
    fixed="top",
    dark=True,
    className="navbar navbar-expand-lg navbar-dark bg-dark",
)

navbar_bottom = dbc.Navbar(
    [dbc.Label("mrsimulator 2018-2019", style={"color": "white"})],
    color="dark",
    sticky="bottom",
    # fixed="bottom",
    dark=True,
    # className="navbar navbar-expand-lg navbar-dark bg-dark",
)
