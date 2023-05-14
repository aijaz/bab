from logging.config import dictConfig
import os
import sys


def setup_logging(app):
    current_directory = app.root_path
    log_file = os.path.join(current_directory, "flask.log")
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
