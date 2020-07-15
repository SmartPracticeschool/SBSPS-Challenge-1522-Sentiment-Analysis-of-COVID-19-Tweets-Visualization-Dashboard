import pandas as pd
import plotly.express as px  # (version 4.7.0)
import plotly.graph_objects as go

import dash  # (version 1.12.0) pip install dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__)


# ----------------------------------------------------------------------------------------------------------------------------------------
#Import and clean data (importing csv into pandas)
df = pd.read_csv("Res.csv")
print(df[:5])

# ----------------------------------------------------------------------------------------------------------------------------------------
# App layout
app.layout = html.Div([

    html.H1("COVID-19 Sentiment Analysis", style={'text-align': 'center'}),

    dcc.Slider(id="slct_period",
                min=0,
                max=4,
                marks={
                    0:'Live',
                    1:'LD1',
                    2:'LD2',
                    3:'LD3',
                    4:'Predict'
                },
                value=0
                ),

    # html.Div(id='trending_topics', children=[]),
    # html.Br(),
    # html.Div(id='trending_hashtags', children=[]),
    # html.Br(),
    dcc.Graph(id='sentiment_analysis')

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [#Output(component_id='output_container', component_property='children'),
     Output(component_id='sentiment_analysis', component_property='figure')],
    [Input(component_id='slct_period', component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    # Plotly Express
    dff = df.copy()
    #dff = px.data.gapminder().query("date == '2020-03-25'")

    #fig = px.line(dff, x="date", y="no of tweets", color="sentiment")
    fig = px.line(dff, x="date", y="sentiment", title='Single Sentiment Graph')

    return fig


# ------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)