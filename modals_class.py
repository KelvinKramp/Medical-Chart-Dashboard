from jupyter_dash import JupyterDash
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import dash_table

class Modals_Class:
    # DEFINE MODAL WINDOW
    modal1 = html.Div(
        [
            dbc.Button("Choose medical institute", id="open"),
            dbc.Modal(
                [
                    dbc.ModalHeader("Header"),
                    dcc.Dropdown(
                        id='NH',
                        options=[
                            {'label': 'Medical institute 1', 'value': 1},
                            {'label': 'Medical institute 2', 'value': 2},
                            {'label': 'Medical institute 3', 'value': 3}
                        ],
                    value= None),
                    dbc.ModalFooter(
                        dbc.Button("Close", id="close", className="ml-auto")
                    ),
                ],
                id="modal",
            ),
        ]
    )