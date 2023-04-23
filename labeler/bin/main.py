import argparse
import logging

from labeler.utils.read_data import XMLFormatter
from labeler.utils.coref_resolution import CorefResolution
from labeler.utils.parse_data import TextSplitter


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

    # access data by finding data[index]['resolved_text'], no splitting has been done yet
    # beware - this process takes a while. i'll look into optimizaiton/parallelization but for now, it took me
    # about 10 minutes to run the 18 podcast documents
    # definitely works better with short sentences & podcast format is probably a little extra weird

    logging.info("Splitting sentences...")
    logging.info(f"Collection length at start: {len(data)}")
    data_split = []
    for document in data:
        doc_list = TextSplitter(document).split_into_sentences()
        data_split.extend(doc_list)
    logging.info(f"Collection length after splitting: {len(data_split)}")
    logging.info(f"Orig length after splitting: {len(data)}")

    logging.info("Beginning passive check...")
    # to do - add passive details here
    logging.info("Passive check complete")

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
