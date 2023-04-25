import logging
import numpy as np

from .consts import ANTHROPOMORPHIC_VERBS, MODEL_LEXICON


class AnthropomorphizationAnalyzer:
    def __init__(self, df):
        self.df = df

    def evaluate_text(self):
        logging.info("Beginning rule-based evaluation...")

        self.df["baseline_label"] = np.where(
            (
                (self.df["binary"] == 0)
                & self.df["sentences"].str.contains("|".join(ANTHROPOMORPHIC_VERBS))
                & self.df["sentences"].str.contains("|".join(MODEL_LEXICON))
            ),
            1,
            0,
        )

        return self.df
