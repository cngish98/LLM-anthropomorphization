"""Pulls in XML data and creates csv containing each sentence.

Data was organized into 5 subdirectories by genre: academic, blog,
news, podcast, and video, all within a LLM-data directory.

For each subdirectory, create a csv file with each line being a resolved
coreference sentence.
"""

import csv
import logging

from labeler.utils.read_data import XMLFormatter
from labeler.utils.coref_resolution import CorefResolution
from labeler.utils.parse_data import TextSplitter

folders = ["academic", "blog", "news", "podcast", "video"]


for subfolder in folders:
    logging.info("Reading in data...")
    data = XMLFormatter(f"../../../LLM-data/{subfolder}").read_xmls()
    logging.info(f"Number of documents: {len(data)}")

    logging.info("Starting coreference resolution...")
    for document in data:
        document["resolved_text"] = CorefResolution(
            document["main_text"]
        ).resolve_coreferences()
    logging.info("Coreference resolution complete")

    logging.info("Splitting sentences...")
    logging.info(f"Collection length at start: {len(data)}")
    data_split = []
    file = open(f"{subfolder}.csv", "w")
    writer = csv.writer(file)
    writer.writerow(
        ["id", "url", "source", "source_type", "authors", "title", "date", "sentence"]
    )
    for i, document in enumerate(data):
        doc_list = TextSplitter(document).split_into_sentences()
        data_split.extend(doc_list)
    logging.info(f"Collection length after splitting: {len(data_split)}")

    for item in data_split:
        writer.writerow(item.values())
