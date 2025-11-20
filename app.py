from flask import Flask, render_template_string, send_from_directory
import os

app = Flask(__name__)

# Serve the main HTML page
@app.route('/')
def index():
    # Read the HTML file and serve it
    with open('ensem_marks_estimator_v1.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    return render_template_string(html_content)

'''# Optional: Serve favicon or other static files
@app.route('/favicon.ico')
def favicon():
    return '', 404    '''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)