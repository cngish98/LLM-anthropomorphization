from fastcoref import FCoref, spacy_component
# from fastcoref import LingMessCoref, spacy_component
# LingMessCoref is a more accurate coreference resolution implementation, but it takes much longer to run
# spacy_component is required with both libraries even though it is not directly called anywhere
import spacy

# library documentation: https://github.com/shon-otmazgin/fastcoref


class CorefResolution:
    def __init__(self, text):
        self.text = text

    def resolve_coreferences(self):
        model = FCoref(device="mps")

        nlp = spacy.load("en_core_web_sm")
        nlp.add_pipe("fastcoref")

        doc = nlp(self.text)

        doc = nlp(  # for multiple texts use nlp.pipe
            self.text, component_cfg={"fastcoref": {"resolve_text": True}}
        )

        return doc._.resolved_text
