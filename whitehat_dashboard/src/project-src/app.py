from flask import Flask, render_template, request
from flask_cors import CORS
from dash import Dash, dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Create Flask app
server = Flask(__name__)
CORS(server)

# Create Dash app and bind it to Flask
app = Dash(__name__, server=server, url_base_pathname='/dashboard/')

# Define Dash layout
app.layout = html.Div([
    html.H1('📊 My Dashboard'),
    dcc.Dropdown(
        id='dropdown',
        options=[
            {'label': 'Option 1', 'value': 'option1'},
            {'label': 'Option 2', 'value': 'option2'}
        ],
        value='option1'
    ),
    dcc.Graph(id='graph'),
    dcc.Graph(id='bar-graph'),
    dcc.Graph(id='scatter-graph')
])

# Define Dash callback
@app.callback(
    [Output('graph', 'figure'),
     Output('bar-graph', 'figure'),
     Output('scatter-graph', 'figure')],
    [Input('dropdown', 'value')]
)
def update_plots(value):
    df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [2, 4, 6, 8, 10]})
    return (
        px.line(df, x='x', y='y'),
        px.bar(df, x='x', y='y'),
        px.scatter(df, x='x', y='y')
    )

# Start Flask (with Dash mounted)
if __name__ == '__main__':
    server.run(debug=True)
