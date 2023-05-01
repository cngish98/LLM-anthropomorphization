import argparse
import glob
import logging
import os

import pandas as pd

from sklearn.model_selection import train_test_split

from labeler.baseline import AnthropomorphizationAnalyzer
from labeler.utils.export_csv import ExportCSV
from labeler.utils.get_metrics import Metrics
from labeler.utils.passivity_check import PassiveChecker

logging.getLogger().setLevel(logging.INFO)

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
    parser.add_argument(
        "-e",
        "--export",
        required=False,
        help="export baseline labeled data to csv",
        action="store_true",
    )

    args = parser.parse_args()
    data_dir = args.data
    process = args.process
    export = args.export

    logging.info(f"arg - data directory: {data_dir}")

    logging.info("Reading in data from csv...")
    all_files = glob.glob(os.path.join(data_dir, "*.csv"))

    all_sentences = pd.concat((pd.read_csv(f) for f in all_files), ignore_index=True)
    logging.info(f"Number of sentences: {len(all_sentences)}")

    logging.info("Beginning passive check...")
    all_sentences_df = PassiveChecker(all_sentences).check_for_passives_df()
    # columns: 'sentences', 'all_passives', 'all_passives_count', 'binary', 'full_passive_matches',
    # 'raw_full_passive_count', 'binary_full_passive', 'truncated_passive_matches', 'raw_truncated_passive_count',
    # 'binary_truncated_passive', 'id', 'url', 'source', 'source_type', 'authors', 'title', 'date', 'gold_label'
    logging.info("Passive check complete")

    logging.info("Running baseline predictions...")
    all_sentences_df = AnthropomorphizationAnalyzer(all_sentences_df).evaluate_text()
    # columns: 'sentences', 'all_passives', 'all_passives_count', 'binary', 'full_passive_matches',
    # 'raw_full_passive_count', 'binary_full_passive', 'truncated_passive_matches', 'raw_truncated_passive_count',
    # 'binary_truncated_passive', 'id', 'url', 'source', 'source_type', 'authors', 'title', 'date', 'gold_label',
    # 'baseline_label'
    logging.info("Baseline predictions complete and added to column 'label'")

    if process == "baseline":
        logging.info("Baseline evaluation complete")

        baseline_labeled = all_sentences_df[["sentences", "gold_label", "label"]]
        baseline_labeled = baseline_labeled.dropna()
        baseline_labeled = baseline_labeled.rename(columns={"sentences": "text"})
        logging.info(f"Baseline labeled sentences: {len(baseline_labeled)}")

        accuracy, f1, conf_matrix = Metrics(
            baseline_labeled["gold_label"], baseline_labeled["label"]
        ).get_metrics()

        logging.info(f"baseline accuracy: {accuracy}")
        logging.info(f"baseline f1_score: {f1}")
        logging.info(f"baseline conf_matrix: {conf_matrix}")

        anthrop_sentences = baseline_labeled[baseline_labeled["label"] == 1]
        logging.info(
            f"Baseline identified {len(anthrop_sentences)} anthropomorphic sentences"
        )

        if export:
            logging.export("Exporting baseline labeled sentences only to csv")
            baseline_labeled = [
                sent for sent in all_sentences if not sent["gold_label"]
            ]

            for item in baseline_labeled:
                del item["id"]
                del item["url"]
                del item["source"]
                del item["source_type"]
                del item["authors"]
                del item["title"]
                del item["date"]
                del item["passive"]
                del item["lemmas"]

            ExportCSV(baseline_labeled).write_df_to_csv(
                "baseline_labeled_excl_gold_labels"
            )

            anthrop_sentences = [
                sent for sent in baseline_labeled if sent["label"] == 1
            ]
            logging.info(
                f"Baseline identified {len(anthrop_sentences)} anthropomorphic sentences"
            )

            ExportCSV(anthrop_sentences).write_df_to_csv("anthrop_sentences")

        logging.info("No export required, process complete")

    elif process == "model":
        logging.info("Running model predictions...")
        train, test = train_test_split(all_sentences_df, test_size=0.2)

        all_sentences = all_sentences[["sentence", "gold_label"]]
        all_sentences = all_sentences.dropna()
        all_sentences = all_sentences.rename(
            columns={"sentence": "text", "gold_label": "label"}
        )
        len_all = len(all_sentences)
        logging.info(f"Number of sentences: {len_all}")

        len_1s = len(all_sentences[all_sentences["label"] == 1])
        len_0s = len(all_sentences[all_sentences["label"] == 0])
        logging.info(f"1s in All: {len_1s}")
        logging.info(f"0s in All: {len_0s}")
        logging.info(f"1s in Train: {len(train[train['label'] == 1])}")
        logging.info(f"0s in Train: {len(train[train['label'] == 0])}")

        train.to_csv("gold_train.csv", index=False)
        logging.info(f"Number of train sentences: {len(train)}")

        test.to_csv("gold_test.csv", index=False)
        logging.info(f"Number of test sentences: {len(test)}")

        weight_for_0 = (1 / len_0s) * (len_all / 2.0)
        weight_for_1 = (1 / len_1s) * (len_all / 2.0)

        class_weight = {0: weight_for_0, 1: weight_for_1}

        # model - scores
        # evaluation
        pass
