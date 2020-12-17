from flask import Flask, request, render_template, render_template_string, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    if request.content_type == 'application/json':
        # If JSON is expected, this is a Javascript request
        mydata = [
            {'label': 'week 46', 'value': 12, 'color': '#ffa600'},
            {'label': 'week 47', 'value': 49, 'color': '#003f5c'},
            {'label': 'week 48', 'value': 50, 'color': '#2f4b7c'},
            {'label': 'week 49', 'value': 20, 'color': '#665191'},
            {'label': 'week 50', 'value': 10, 'color': '#d45087'},
            {'label': 'week 51', 'value': 50, 'color': '#f95d6a'},
            {'label': 'week 52', 'value': 34, 'color': '#ff7c43'}
        ]
        return jsonify(mydata)

    # If JSON was not expected, simply return the index.html file
    with open("index.html") as f:
        return f.read()

