from fastcoref import LingMessCoref, spacy_component
import spacy

model = LingMessCoref(device='mps')
text = 'Alice goes down the rabbit hole. Where she would discover a new reality beyond her expectations.'

nlp = spacy.load("en_core_web_sm")
nlp.add_pipe("fastcoref")

doc = nlp(text)

doc = nlp(      # for multiple texts use nlp.pipe
   text,
   component_cfg={"fastcoref": {'resolve_text': True}}
)

text = doc._.resolved_text
print(text)
