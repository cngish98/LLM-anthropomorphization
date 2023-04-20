import argparse
import logging

from labeler.utils.read_data import XMLFormatter

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Anthropomorphization")
    parser.add_argument("-d", "--data", required=True, help="directory to scraped data")

    args = parser.parse_args()
    data_dir = args.data

    logging.info(f"arguments:")
    logging.info(f"data directory: {data_dir}")

    data = XMLFormatter(data_dir).read_xmls()
    print(len(data))
