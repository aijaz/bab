from flask import Flask
from logging.config import dictConfig
import os

current_directory = "/Users/AAnsari/src/Aijaz/bab"  # /Users/AAnsari/src/Aijaz/bab
log_file = os.path.join(current_directory, "flask.log")  # /Users/AAnsari/src/Aijaz/bab/flask.log
# log_file = f"{current_directory}/flask.log"
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
                    'level': 'WARN'
                }
            },
        'root': {
            'level': 'DEBUG',
            'handlers': ['custom_handler']
        }})

app = Flask(__name__)


@app.route("/")
def hello_world():
    app.logger.info("About to return Hello world")
    app.logger.debug("This is a debug statement")
    return "<p>Hello, World Four!</p>"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
