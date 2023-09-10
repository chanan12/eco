import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objects as go
import plotly.express as px
import flask

from process_data import get_processsed_data

# Initialize the Dash app
server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

# Load CSV
data = get_processsed_data()

# Dropdown options
dropdown_options = data["Country Code"].unique()

app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=dropdown_options,
        value='AFE'
    ),
    dcc.Graph(id='feature-graph'),
])


@app.callback(
    Output('feature-graph', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(country):
    df = data[data["Country Code"] == country]
    fig = px.line(df, x="Year", y="eco")
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
