import logging

from .consts import ANTHROPOMORPHIC_VERBS, MODEL_LEXICON


class AnthropomorphizationAnalyzer:
    def __init__(self, doc_list):
        self.doc_list = doc_list

    def evaluate_text(self):
        anthropomorphic_sentences = []

        logging.info("Beginning rule-based evaluation...")

        for index, doc_dict in enumerate(self.doc_list):
            self.doc_list[index]["anthrop_label"] = 0
            if doc_dict["passive"] == 0:
                logging.info("Sentence is active, continuing check...")
                if any(word in doc_dict["sentence"] for word in ANTHROPOMORPHIC_VERBS):
                    logging.info(
                        "Sentence contains anthropomorphic verbs, continuing check..."
                    )
                    if any(word in doc_dict["sentence"] for word in MODEL_LEXICON):
                        logging.info("Sentence contains model lexicon, adding to list")
                        anthropomorphic_sentences.append(doc_dict)
                        self.doc_list[index]["anthrop_label"] = 1

        return anthropomorphic_sentences, self.doc_list
