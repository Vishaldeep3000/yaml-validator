# app.py

from flask import Flask, render_template, request
import yaml

app = Flask(__name__)

def validate_yaml_indentation(yaml_text):
    try:
        # Attempt to load YAML
        parsed_yaml = yaml.safe_load(yaml_text)
        # If loading succeeds, return "Looks good"
        return "Looks good"
    except yaml.YAMLError as e:
        # If loading fails, return the error message
        return f"YAML Error: {e}"

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    yaml_text = ""
    if request.method == 'POST':
        yaml_text = request.form['yaml_text'].strip()
        if yaml_text:
            result = validate_yaml_indentation(yaml_text)
    return render_template('index.html', yaml_text=yaml_text, result=result)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
