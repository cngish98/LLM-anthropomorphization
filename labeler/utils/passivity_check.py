from PassivePySrc import PassivePy

# library documentation: https://pypi.org/project/PassivePy/


class PassiveChecker:
    def __init__(self, dict):
        self.dict = dict

    def check_for_passives(self):
        passivepy = PassivePy.PassivePyAnalyzer(spacy_model="en_core_web_sm")

        df = passivepy.match_text(
            self.dict["sentence"], full_passive=True, truncated_passive=True
        )
        self.dict["passive"] = df["binary"].item()

        return self.dict
