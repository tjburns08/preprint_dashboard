import dash
from dash import dash_table
from dash import html
import pandas as pd
from dash.dependencies import Input, Output

# Process the dataframe
import json
import pandas as pd

def read_jsonl(file_path):
    """
    Reads a JSONL (JSON Lines text format) file and converts it to a pandas DataFrame.

    This function iterates over each line in a JSONL file, parses it as JSON, and appends
    the data to a list. It handles JSONDecodeError by printing an error message. Finally, 
    it converts the list of JSON objects into a pandas DataFrame and removes any duplicate entries.

    Args:
        file_path: A string representing the path to the JSONL file to be read.

    Returns:
        A pandas DataFrame containing the data from the JSONL file, with duplicates removed.

    Raises:
        json.JSONDecodeError: An error is printed if a JSON object cannot be decoded.
        
    """
    data_list = []
    with open(file_path, 'r') as jsonl_file:
        for line in jsonl_file:
            try:
                data = json.loads(line.strip())
                data_list.append(data)
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON: {e}")

    result = pd.DataFrame(data_list).drop_duplicates()
    return result

# Specify the path to your JSONL file
source_list = ['biorxiv', 'chemrxiv', 'medrxiv'] 
data_path = 'data/latest/' # Specific to your instance

df = []
for i in source_list:
    curr = read_jsonl(data_path + i + '.jsonl')
    curr['source'] = i
    df.append(curr)

df = pd.concat(df).reset_index()

# Extra filtering
df = df[df['date'] >= '2024-01-01'] 

# Make the doi links clickable (assuming display in markdown presentation)
df['doi'] = df['doi'].apply(lambda x: f"[{x}](https://doi.org/{x})" if pd.notnull(x) else "")


# show only necessary columns
df = df[['title', 'abstract', 'authors', 'doi', 'date', 'source']]

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    html.H1("Preprint Dashboard"),
    
    dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i, "type": "text", "presentation": "markdown"} for i in df.columns],
        data=df.to_dict('records'),
        style_table={'overflowX': 'auto'}, # Horizontal scroll
        page_size=15,  # Pagination

        # Enable filtering
        filter_action='native',
    ),
])

# Callback to truncate displayed text in cells
@app.callback(
    Output('table', 'style_data_conditional'),
    [Input('table', 'data')]
)
def truncate_display_text(rows):
    styles = []
    for i in range(len(rows)):
        row = rows[i]
        for col in row:
            value = row[col]
            if isinstance(value, str) and len(value) > 1:
                # Truncate display text and add ellipsis
                styles.append({
                    'if': {'row_index': i, 'column_id': col},
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'lineHeight': '15px',
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis'
                })
    return styles


# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)