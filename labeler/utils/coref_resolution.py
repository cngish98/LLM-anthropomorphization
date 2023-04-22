from fastcoref import LingMessCoref, spacy_component
import spacy


class CorefResolution:
    def __init__(self, text):
        self.text = text

    def resolve_coreferences(self):
        model = LingMessCoref(device="mps")

        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("fastcoref")

        doc = nlp(self.text)

        doc = nlp(  # for multiple texts use nlp.pipe
            self.text, component_cfg={"fastcoref": {"resolve_text": True}}
        )

        return doc._.resolved_text
