"""Coreference resolution to assist hand-labeling data as individual sentences.

LingMessCoref is a more accurate coreference resolution implementation,
but it takes much longer to run.

fastcoref library documentation: https://github.com/shon-otmazgin/fastcoref

spacy_component is required with both libraries even though it is not directly
called anywhere.
"""

from fastcoref import FCoref, spacy_component
import spacy


class CorefResolution:
    """Finds and replaces similar entities in text."""

    def __init__(self, text):
        """
        :param text: pulled text data from XML file
        """

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
