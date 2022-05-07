#  Copyright (c) 2022. luz5020
#  Approved for use in Open Source Projects
#  GNU General Public License v3.0
#  https://www.gnu.org/licenses/gpl-3.0.en.html

from flask import Flask, render_template

app = Flask(__name__)


# Render-group
@app.route('/')
def home():
    return render_template('index.html')


# Run
if __name__ == '__main__':
    app.run(debug=True)
