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
    def __init__(self, df):
        self.df = df

    def evaluate_text(self):
        logging.info("Beginning rule-based evaluation...")
        nlp = spacy.load("en_core_web_sm")
        logging.info("Lemmatizing sentences...")
        self.df["parsed_sentences"] = self.df["sentences"].apply(
            lambda x: [y.lemma_ for y in nlp(x.lower())]
        )
        logging.info("Applying filters...")
        self.df["baseline_label"] = self.df.apply(filters, axis=1)
        return self.df
