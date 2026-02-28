import logging
from docx import Document
from docx.shared import Inches

logger = logging.getLogger(__name__)

class DocImporter(object):

    def __init__(self, doc_path):
        self.doc_path = doc_path

    def import_doc(self):
        try:
            with open(self.doc_path, 'r', encoding='utf-8') as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print(f"Error: The file '{self.doc_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


def import_doc():
    return None