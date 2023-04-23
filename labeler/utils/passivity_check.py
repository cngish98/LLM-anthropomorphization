from PassivePySrc import PassivePy

# library documentation: https://pypi.org/project/PassivePy/


class PassiveChecker:
    def __init__(self, text):
        self.text = text

    def check_for_passives(self):
        passivepy = PassivePy.PassivePyAnalyzer(spacy_model="en_core_web_lg")
