import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

# Load the data
data_path = 'C:/Users/admin/Downloads/archive/Astar-0.9_Ustar-8_Re-4000_sample/sample/1/fourD_U_vorticity.csv'  # Update path to your file
data = pd.read_csv(data_path)
vorticity_columns = [col for col in data.columns if 'vorticity' in col]

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout
app.layout = html.Div([
    html.H1("Interactive Vorticity Plot"),
    
    # Dropdown for selecting vorticity component
    html.Label("Select Vorticity Component:"),
    dcc.Dropdown(
        id='vorticity-dropdown',
        options=[{'label': col, 'value': col} for col in vorticity_columns],
        value=vorticity_columns[0]  # Default to the first vorticity component
    ),
    
    # Slider for selecting spatial dimension range (y)
    html.Label("Select y Range:"),
    dcc.RangeSlider(
        id='y-slider',
        min=data['y'].min(),
        max=data['y'].max(),
        value=[data['y'].min(), data['y'].max()],
        marks={int(y): str(y) for y in range(int(data['y'].min()), int(data['y'].max()) + 1, 1)}
    ),
    
    # Graph for displaying the vorticity plot
    dcc.Graph(id='vorticity-plot')
])

# Define the callback to update the plot based on user inputs
@app.callback(
    Output('vorticity-plot', 'figure'),
    [Input('vorticity-dropdown', 'value'),
     Input('y-slider', 'value')]
)
def update_vorticity_plot(selected_vorticity, y_range):
    # Filter data based on the selected y range
    filtered_data = data[(data['y'] >= y_range[0]) & (data['y'] <= y_range[1])]
    
    # Create the plot
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=filtered_data['y'],
        y=filtered_data[selected_vorticity],
        mode='lines',
        name=selected_vorticity
    ))
    
    # Customize the layout
    fig.update_layout(
        title=f"{selected_vorticity} across Spatial Dimension (y)",
        xaxis_title="Spatial Dimension (y)",
        yaxis_title=selected_vorticity
    )
    
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
