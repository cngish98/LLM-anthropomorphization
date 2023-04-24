import argparse
import logging

from labeler.utils.read_data import XMLFormatter
from labeler.utils.coref_resolution import CorefResolution
from labeler.utils.parse_data import TextSplitter
from labeler.utils.passivity_check import PassiveChecker


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Anthropomorphization")
    parser.add_argument("-d", "--data", required=True, help="directory to scraped data")
    parser.add_argument(
        "-p",
        "--process",
        required=True,
        choices=["baseline", "model"],
        help="process to run",
    )

    args = parser.parse_args()
    data_dir = args.data
    process = args.process

    logging.info(f"arg - data directory: {data_dir}")

    logging.info("Reading in data...")
    data = XMLFormatter(data_dir).read_xmls()
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
    for document in data:
        doc_list = TextSplitter(document).split_into_sentences()
        data_split.extend(doc_list)
    logging.info(f"Collection length after splitting: {len(data_split)}")

    logging.info("Beginning passive check...")
    for index, document in enumerate(data_split):
        data_split[index] = PassiveChecker(document).check_for_passives()
    logging.info("Passive check complete")
    print(data_split)

    if process == "baseline":
        logging.info("Running baseline predictions...")
        # lemmatiziation
        # semantic role labeling
        # baseline evaluation
        pass
    elif process == "model":
        logging.info("Running model predictions...")
        # preprocess
        # train/test split
        # model - scores
        # evaluation
        pass
