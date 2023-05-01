from PassivePySrc import PassivePy

# library documentation: https://pypi.org/project/PassivePy/


class PassiveChecker:
    def __init__(self, df):
        self.df = df

    def check_for_passives_df(self):
        passivepy = PassivePy.PassivePyAnalyzer(spacy_model="en_core_web_sm")

        df = passivepy.match_sentence_level(
            self.df,
            column_name="sentence",
            batch_size=1000,
            full_passive=True,
            truncated_passive=True,
        )
        df = df.drop(columns=["sentenceId", "docId"])

        return df
