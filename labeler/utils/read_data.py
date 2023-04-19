from datetime import datetime
import re

from lxml import etree


xml_path = "/Users/ctung/Library/CloudStorage/Dropbox/My Files/georgetown/2023 - 01 to 05/ling 472 | advanced python/llm-data/news/news-cl-87.xml"
tree = etree.parse(xml_path)
root = tree.getroot()
url = root[0].text
source = root[1].text
source_type = root[1].get("type")
authors = root[2]
title = root[3].text
date = root[4].text
description = root[5].text
main_text = root[6].text
tags = root[7]

text = {
    "url": url,
    "source": source,
    "source_type": source_type,
    "authors": [author.text for author in authors],
    "title": title,
    "date": datetime.strptime(date, "%Y-%m-%d").date(),
    "description": description,
    "main_text": re.sub(r"\s{2,}", "", main_text.replace("\n", "")),
    "tags": [tag.text for tag in tags],
}

print(text)

# TODO this needs to be set up as a real class and whatnot, also there probably needs to be an extra for loop over everything once we combine all the xmls together
