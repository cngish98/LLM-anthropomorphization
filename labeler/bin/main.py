import argparse
import glob
import logging
import os

import pandas as pd

from labeler.baseline import AnthropomorphizationAnalyzer
from labeler.utils.read_data import XMLFormatter
from labeler.utils.coref_resolution import CorefResolution
from labeler.utils.parse_data import TextSplitter
from labeler.utils.passivity_check import PassiveChecker

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="LLM Anthropomorphization")
    parser.add_argument("-d", "--data", required=True, help="directory to labeled csvs")
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

    logging.info("Reading in data from csv...")
    all_files = glob.glob(os.path.join(data_dir, "*.csv"))
    all_sentences_df = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    logging.info(f"Number of sentences: {len(all_sentences_df)}")
    # columns: 'id', 'url', 'source', 'source_type', 'authors', 'title', 'date', 'sentence', 'gold_label'
    print(all_sentences_df.head())

    logging.info("Beginning passive check...")
    all_sentences_df = PassiveChecker(all_sentences_df).check_for_passives()
    # columns: 'sentences', 'all_passives', 'all_passives_count', 'binary', 'full_passive_matches',
    # 'raw_full_passive_count', 'binary_full_passive', 'truncated_passive_matches', 'raw_truncated_passive_count',
    # 'binary_truncated_passive', 'id', 'url', 'source', 'source_type', 'authors', 'title', 'date', 'gold_label'
    print(all_sentences_df.head())
    logging.info("Passive check complete")

    logging.info("Running baseline predictions...")
    anthrop_sentences, all_sentences_df = AnthropomorphizationAnalyzer(
        all_sentences_df
    ).evaluate_text()
    print(all_sentences_df.head())
    logging.info("Baseline predictions complete and added to column 'baseline_label'")
    # columns: 'sentences', 'all_passives', 'all_passives_count', 'binary', 'full_passive_matches',
    # 'raw_full_passive_count', 'binary_full_passive', 'truncated_passive_matches', 'raw_truncated_passive_count',
    # 'binary_truncated_passive', 'id', 'url', 'source', 'source_type', 'authors', 'title', 'date', 'gold_label',
    # 'baseline_label'

    if process == "baseline":
        logging.info("Baseline evaluation complete")
        for index, flagged_sentence in enumerate(anthrop_sentences):
            print(index, flagged_sentence["id"], flagged_sentence["sentence"])
        logging.info(
            f"Baseline identified {len(anthrop_sentences)} anthropomorphic sentences"
        )
    elif process == "model":
        logging.info("Running model predictions...")
        # preprocess
        # train/test split
        # model - scores
        # evaluation
        pass
