from dash import Dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc
from app import app, dicoParam

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    html.H1(dicoParam[1]["Titre"], style={"text-align": "center", "padding": "40px", "font-size": "50px"}),
    dbc.Container(
        dbc.Row(
            [
            dbc.Col(html.Img(src=dicoParam[1]["Image"], style={"cursor": "pointer", "border": "1px solid black", "width": "200px"}), width=6),
            dbc.Col(html.H2("Harry Potter est cool"), width=6),
        ],
        className="mb-4"
        ), fluid=True)
)