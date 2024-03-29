from __future__ import annotations

import typing
from argparse import FileType
from ast import Bytes
from ctypes.wintypes import BOOL, INT
from datetime import date
from email.charset import BASE64
from hashlib import md5
from pathlib import Path
from typing import *

from sqlalchemy import DATE
from typing_extensions import *

from ...extension_globals.database import db


class FileTracker(db.Model):
    """_summary_ = "FileTracker"

    Args:
        db (_type_): _description_

    Returns:
        _type_: _description_

    Raises:
        _type_: _description_

    """

    __tablename__ = "file_tracker"
    id: int = db.Column(db.Integer, primary_key=True)
    file_name: str = db.Column(db.String(255), nullable=False)
    file_cid: str = db.Column(db.String(255), nullable=False)
    file_hash: str = db.Column(db.String(255), nullable=False)
    file_size: int = db.Column(db.Integer, nullable=False)
    file_type: str = db.Column(db.String(255), nullable=False)
    file_date: date = db.Column(db.Date, nullable=False)

    def check_if_valid_hash(self, hash_: str) -> bool:
        """_summary_ = "Check if the hash is valid"

        Args:
            hash_ (_type_): _description_
        """
        return self.file_hash == hash_

    def check_if_valid_cid(self, cid: str) -> bool:
        """_summary_ = "Check if the CID is valid"

        Args:
            cid (_type_): _description_
        """
        return self.file_cid == cid

    def __init__(
        self,
        file_name: str,
        file_cid: str,
        file_hash: str,
        file_size: int,
        file_type: str,
        file_date: date,
    ):
        """_summary_ = "Initialize the FileTracker"
        Args:

            file_name: (str) The name of the file.
            file_cid: (str) The CID of the file.
            file_hash: (str) The hash of the file.
            file_size: (int) The size of the file.
            file_type: (str) The type of the file.
            file_date: (date) The date of the file.
        """
        self.file_name = file_name
        self.file_cid = file_cid
        self.file_hash = file_hash
        self.file_size = file_size
        self.file_type = file_type
        self.file_date = file_date
