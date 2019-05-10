import os
import uuid
import pathlib

class FilesService:

    def upload(self, file_storage):
        tmp_file_path = self.__save_tmp(file_storage)
        return tmp_file_path

    def __save_tmp(self, file_storage):
        filename = str(uuid.uuid4())
        ext = pathlib.Path(file_storage.filename).suffix
        result_path = os.path.join('tmp', filename+ext)
        file_storage.save(result_path)
        file_storage.close()
        return result_path