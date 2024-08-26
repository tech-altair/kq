from dash import dcc, html
import dash
import pandas as pd
import base64

# Function to read the model results
def read_model_results():
    with open('model_results.txt', 'r') as file:
        return file.read()

# Load and encode images from the visualization folder
def load_image(image_path):
    with open(image_path, 'rb') as file:
        encoded = base64.b64encode(file.read()).decode()
    return f'data:image/png;base64,{encoded}'

# Define paths to images
image_paths = {
    'wordcount': './visualization/wordcount.png',
    'sentiment_distribution': './visualization/Preliminary_Sentiment_Distribution.png',
    'verified_distribution': './visualization/Distribution_of_Verified_Reviews.png',
    'most_used_words': './visualization/most_used_words.png',
    'confusion_matrix': './visualization/confusion_matrix.png',
    'word_cloud_positive': './visualization/Word_Cloud_for_Positive_Sentiment.png',
    'word_cloud_negative': './visualization/Word_Cloud_for_Negative_Sentiment.png',
    'vader_sentiment_distribution': './visualization/vader_sentiment_distribution.png',  # Add VADER sentiment distribution image
}

# Generate encoded images for dashboard display
images = {key: load_image(path) for key, path in image_paths.items()}

# Load model results
model_results = read_model_results()

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Kenya Airways Customer Reviews Dashboard', style={'textAlign': 'center', 'marginBottom': '50px'}),

    html.Div(children='''
        Overview and Analysis of Customer Sentiment for Kenya Airways.
    ''', style={'textAlign': 'center', 'marginBottom': '50px'}),

    html.Div(style={'display': 'flex', 'flexDirection': 'row', 'justifyContent': 'space-between'}, children=[

        html.Div(style={'width': '48%'}, children=[
            html.H3('Word Count Distribution', style={'textAlign': 'center'}),
            html.Img(src=images['wordcount'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('Distribution of Verified Reviews', style={'textAlign': 'center'}),
            html.Img(src=images['verified_distribution'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('Confusion Matrix of Sentiment Analysis Model', style={'textAlign': 'center'}),
            html.Img(src=images['confusion_matrix'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('VADER Sentiment Distribution', style={'textAlign': 'center'}),
            html.Img(src=images['vader_sentiment_distribution'], style={'width': '100%', 'marginBottom': '50px'}),  # Display VADER sentiment distribution
        ]),

        html.Div(style={'width': '48%'}, children=[
            html.H3('Sentiment Distribution', style={'textAlign': 'center'}),
            html.Img(src=images['sentiment_distribution'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('Most Used Words', style={'textAlign': 'center'}),
            html.Img(src=images['most_used_words'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('Word Cloud for Positive Sentiment', style={'textAlign': 'center'}),
            html.Img(src=images['word_cloud_positive'], style={'width': '100%', 'marginBottom': '50px'}),

            html.H3('Word Cloud for Negative Sentiment', style={'textAlign': 'center'}),
            html.Img(src=images['word_cloud_negative'], style={'width': '100%', 'marginBottom': '50px'}),
        ]),
    ]),

    html.Div(style={'marginTop': '50px'}, children=[
        html.H3('Model Evaluation Results', style={'textAlign': 'center', 'marginBottom': '20px'}),
        html.Pre(model_results, style={
            'border': '1px solid #ddd',
            'padding': '20px',
            'backgroundColor': '#f9f9f9',
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all',
            'overflowX': 'auto',
            'textAlign': 'left',
            'margin': '0 auto',
            'width': '80%',
        }),
    ]),

])

if __name__ == '__main__':
    app.run_server(debug=True)
