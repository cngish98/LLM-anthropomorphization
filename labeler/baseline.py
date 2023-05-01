import logging

import spacy

from .consts import ANTHROPOMORPHIC_WORDS, MODEL_LEXICON


def filters(df):
    if df["binary"] == 0:
        if any(word in df["parsed_sentences"] for word in ANTHROPOMORPHIC_WORDS):
            if any(word in df["parsed_sentences"] for word in MODEL_LEXICON):
                return 1
    return 0


class AnthropomorphizationAnalyzer:
    def __init__(self, data):
        self.data = data

    def evaluate_text(self):
        logging.info("Beginning rule-based evaluation...")
        nlp = spacy.load("en_core_web_sm")
        logging.info("Lemmatizing sentences...")
        self.data["parsed_sentences"] = self.data["sentences"].apply(
            lambda x: [y.lemma_ for y in nlp(x.lower())]
        )
        logging.info("Applying filters...")
        self.data["label"] = self.data.apply(filters, axis=1)
        return self.data
