from logging.config import dictConfig
import os
import sys

from flask import Flask, render_template

app = Flask(__name__)

current_directory = app.root_path  # /Users/AAnsari/src/Aijaz/bab
log_file = os.path.join(current_directory, "flask.log")  # /Users/AAnsari/src/Aijaz/bab/flask.log
dictConfig(
    {
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
            },
            'simpleformatter': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            }
        },
        'handlers':
            {
                'custom_handler': {
                    'class': 'logging.FileHandler',
                    'formatter': 'simpleformatter',
                    'filename': log_file,
                    'level': 'DEBUG'
                },
                'stdout_handler': {
                    'class': 'logging.StreamHandler',
                    'formatter': 'default',
                    'stream': sys.stdout,
                    'level': 'DEBUG'
                }
            },
        'root': {
            'level': 'DEBUG',
            'handlers': ['custom_handler', 'stdout_handler']
        }})


@app.route("/")
def hello_world():
    app.logger.info("About to return Hello world")
    app.logger.debug("This is a debug statement")
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
