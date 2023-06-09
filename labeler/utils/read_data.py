"""Read in data from XML files."""

import logging
import re

from datetime import datetime
from pathlib import Path

from lxml import etree


class XMLFormatter:
    """Extract id, url, source, source type, authors, title,
    date, description, and main text from each XML file"""

    def __init__(self, data_dir):
        """

        :param data_dir: genre subdirectory
        """
        self.data_dir = data_dir

    def read_xmls(self):
        """Read XML data and store into list.

        :return: list of dictionaries of each document
        """
        logging.info(f"Beginning to read in data from {self.data_dir}...")
        text_collection = []
        doc_count = 0
        parser = etree.XMLParser(remove_comments=True)

        for file in Path(self.data_dir).glob("*.xml"):
            tree = etree.parse(file, parser)
            root = tree.getroot()
            url = root[0].text
            source = root[1].text
            source_type = root[1].get("type")
            authors = root[2]
            title = root[3].text
            date = root[4].text
            description = root[5].text
            main_text = root[6].text

            text = {
                "id": doc_count,
                "url": url,
                "source": source,
                "source_type": source_type,
                "authors": [author.text for author in authors],
                "title": title,
                "date": datetime.strptime(date, "%Y-%m-%d").date()
                if date is not None
                else None,
                "description": description,
                "main_text": re.sub(r"\s{2,}", " ", main_text.replace("\n\n", " ")),
            }

            text_collection.append(text)
            doc_count += 1

        return text_collection
