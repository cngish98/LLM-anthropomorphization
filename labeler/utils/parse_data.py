import copy
import logging

from nltk import tokenize


class TextSplitter:
    def __init__(self, full_dict):
        self.full_dict = full_dict

    def split_into_sentences(self):
        text = tokenize.sent_tokenize(self.full_dict["resolved_text"])

        split_documents = []

        logging.info("Splitting sentences into dictionaries")

        for i, sentence in enumerate(text):
            new_dict = copy.deepcopy(self.full_dict)
            new_dict["id"] = f"news-{self.full_dict['id']}-s{i}"
            new_dict["sentence"] = sentence
            del new_dict["main_text"]
            del new_dict["resolved_text"]
            split_documents.append(new_dict)

        logging.info(f"Number of sentences: {len(split_documents)}")

        return split_documents
