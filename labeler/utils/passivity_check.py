"""Check sentence passivity.

library documentation: https://pypi.org/project/PassivePy/

"""

from PassivePySrc import PassivePy


class PassiveChecker:
    def __init__(self, df):
        """
        :param df: pandas dataframe with (?)
        """
        self.df = df

    def check_for_passives_df(self):
        """Use PassivePy model to differentiate active versus passive sentences

        :return: dataframe with only text and label columns (?)
        """
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
