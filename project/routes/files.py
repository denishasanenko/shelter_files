from flask import Blueprint, jsonify, abort, request
from project.models.files import Files
from project.models import db_session
from project.services.files import FilesService
from sqlalchemy import literal_column


files_bp = Blueprint('files_bp', __name__, url_prefix='/files')


@files_bp.route('/', methods=['POST'])
def file_upload():
    file = request.files['file']
    mime = file.mimetype
    fs = FilesService()
    new_filename = fs.upload(file)
    file_record = Files.insert().values(dist='http://localhost:5001/'+new_filename.replace('\\', '/'), mimetype=mime).returning(literal_column('*'))
    result = db_session.execute(file_record)
    db_session.commit()
    return jsonify(dict(result.first()))


@files_bp.route('/<string:file_uuid>', methods=['GET'])
def file_record(file_uuid):
    try:
        query = Files.select().where(Files.c.file_uuid == file_uuid)
        file_record = db_session.execute(query).first()
    except Exception:
        return abort(404)
    return jsonify(dict(file_record))
