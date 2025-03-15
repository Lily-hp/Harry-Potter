from dash import Dash, html, dcc, Input, Output, State, callback
import dash_bootstrap_components as dbc

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

images_1_a_6 = ["/assets/harry potter " + str(i) + ".jpg" for i in range(1,7)]

images_7_a_8 = ["/assets/harry potter 7 part " + str(i) + ".jpg" for i in range(1,3)]

images = images_1_a_6 + images_7_a_8

dicoParam = {
    1: {"Titre": "Harry Potter à l'école des sorciers",
        "Image": images[0]},
    2: {},
    3: {},
    4: {},
    5: {},
    6: {},
    7: {},
    8: {},
    }

rows = [
    dbc.Row(
        [
            dbc.Col(html.Img(src=image, style={"cursor": "pointer", "border": "1px solid black", "width": "200px"}), width=3)
            for image in images[i:i+4]
        ],
        className="mb-4"
    )
    for i in range(0, len(images), 4)
    ]

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
    html.H1("Harry Potter", style={"text-align": "center", "padding": "40px", "font-size": "50px"}),
    dbc.Container(rows, fluid=True)
    # html.A(
    #     html.Img(
    #         src="/assets/harry potter 1.jpg",
    #         style={"cursor": "pointer", "border": "1px solid black", "width": "200px"}
    #     ),
    #     href="/hp1"
    # )
])

page_2_layout = html.Div([
    html.H1("Harry Potter film 1"),
    html.A(
        html.Img(
            src="/assets/harry potter 1.jpg",
            style={"cursor": "pointer", "border": "1px solid black", "width": "200px"}
        ),
    ),
    html.A("Retour", href="/")
])


@callback(
    Output('page-content', 'children'),
    Input('url', 'pathname'),
)

def display_page(pathname):
    if pathname == "/hp1":
        return page_2_layout

if __name__ == '__main__':
    app.run(debug=True)