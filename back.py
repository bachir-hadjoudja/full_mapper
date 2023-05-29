from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import shutil
import json
import logging



logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)



app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

@app.route('/', methods=['POST'])
def receive_data():
    data = request.get_json(force=True)  # force=True will make sure it gets the data even if a client does not specify the mimetype

    # write columnChange data into a file
    with open('/home/bachir/Bureau/S8/HAI823I TER/scripts/dictionnaire.txt', 'w') as f:
        f.write(json.dumps(data['columnChange']))

    # write fileName into a file
    with open('/home/bachir/Bureau/S8/HAI823I TER/scripts/file_name.txt', 'w') as f:
        f.write(data['fileName'])

    # write fileType into a file
    with open('/home/bachir/Bureau/S8/HAI823I TER/scripts/file_type.txt', 'w') as f:
        f.write(data['fileType'])


if __name__ == '__main__':
    app.run(port=5010, debug=True)
