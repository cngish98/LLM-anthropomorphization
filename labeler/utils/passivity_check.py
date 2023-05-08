"""Check sentence passivity.

library documentation: https://pypi.org/project/PassivePy/

"""

from PassivePySrc import PassivePy


class PassiveChecker:
    def __init__(self, df):
        """
        :param df: pandas dataframe with sentence, url, source, source_type, authors,
        title, date, & gold_label

        """
        self.df = df

    def check_for_passives_df(self):
        """Use PassivePy model to differentiate active versus passive sentences

        :return: dataframe with added passive-data columns ('raw_full_passive_count', 'binary_full_passive',
        'truncated_passive_matches', 'raw_truncated_passive_count', 'binary_truncated_passive')
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
