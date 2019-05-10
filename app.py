from project import create_app
from flask import send_from_directory
import os

app = create_app()

@app.route('/tmp/<path:path>')
def send_file(path):
    print(os.path.dirname('tmp'))
    return send_from_directory(os.path.dirname('C:\\projects\\shelter_files\\tmp\\'), os.path.basename(path))

app.run(debug=True, port=5001)
