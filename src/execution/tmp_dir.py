import logging
import os
import shutil

from files.user_file_storage import UserFileStorage
from utils.file_utils import normalize_path

TMP_FOLDER = 'tmpFiles'

LOGGER = logging.getLogger('script_server.tmpdir')


class ScriptTmpDir:
    __instance = None

    def __new__(cls, user_file_storage: UserFileStorage, temp_folder):
        if ScriptTmpDir.__instance is None:
            ScriptTmpDir.__instance = object.__new__(cls)
        return ScriptTmpDir.__instance

    def __init__(self, user_file_storage: UserFileStorage, temp_folder) -> None:
        self.user_file_storage = user_file_storage
        self.folder = os.path.join(temp_folder, TMP_FOLDER)

    @classmethod
    def prepare_new_folder(cls, username) -> str:
        self = cls.__instance
        if self is None:
            raise Exception(cls + " wasn't inited")
        new_folder = self.user_file_storage.prepare_new_folder(username, self.folder)
        return normalize_path(new_folder)

    @classmethod
    def cleanup_folder(cls, path) -> None:
        self = cls.__instance
        if self is None:
            raise Execution(cls + " wasn't inited")
        LOGGER.debug('Cleaning script tmp folder: ' + path)
        shutil.rmtree(path)
