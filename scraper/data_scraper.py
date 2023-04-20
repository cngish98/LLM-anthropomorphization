import argparse

import newspaper
from lxml import etree

parser = argparse.ArgumentParser(description="location of names.tsv file")
parser.add_argument("--file", required=False, help="filename")
parser.add_argument("--url", required=False, help="url to scrape")
parser.add_argument(
    "--text",
    required=False,
    help="filename for replacing text that wasn't pulled correctly",
)
parser.add_argument(
    "--loc",
    required=False,
    help="field to replace in xml, probably description or main_text",
)
parser.add_argument("--bulk", required=False, help="bulk scraping mode")
parser.add_argument("--type", required=False, help="source type")
parser.add_argument("--source", required=False, help="source name")

args = parser.parse_args()
url_string = args.url
file_name = args.file
replacement_text = args.text
location = args.loc
source_type = args.type
source_string = args.source

if url_string:
    print(f"gathering elements from url: {url_string}")

    # XML SETUP
    data = etree.Element("data")
    url = etree.SubElement(data, "url")
    source = etree.SubElement(data, "source")
    # UPDATE FOR DIFFERENT SOURCE TYPE
    # MUST BE: "news", "podcast", "academic", or "video"
    source.set("type", f"{source_type}")
    authors = etree.SubElement(data, "authors")
    title = etree.SubElement(data, "title")
    date = etree.SubElement(data, "date")
    description = etree.SubElement(data, "description")
    main_text = etree.SubElement(data, "main_text")
    tags = etree.SubElement(data, "tags")

    # ARTICLE RETRIEVAL
    article = newspaper.Article(url=url_string, language="en")
    article.download()
    article.parse()

    # POPULATE XML
    url.text = url_string
    print(url_string)
    title.text = article.title
    if article.publish_date is not None:
        date.text = (
            article.publish_date
            if isinstance(article.publish_date, str)
            else article.publish_date.strftime("%Y-%m-%d")
        )
    description.text = article.summary
    main_text.text = article.text
    source.text = source_string

    for i, _ in enumerate(article.authors):
        author = etree.SubElement(authors, "author")
        author.text = article.authors[i]

    if tags is not None:
        for i, _ in enumerate(article.keywords):
            tag = etree.SubElement(tags, "tag")

    relaxng = etree.RelaxNG(file="template_schema.rnc")
    relaxng.validate(data)
    xml_string = etree.tostring(data)

    print(len(article.text))
else:
    print("replace element from .txt")
    f = open(f"{replacement_text}.txt", "r")
    tree = etree.parse(f"{file_name}.xml")
    root = tree.getroot()
    element = root.find(location)
    replacement = f.read()
    print(replacement)
    element.text = replacement
    f.close()

    xml_string = etree.tostring(root)

f = open(f"{file_name}.xml", "wb")
f.write(xml_string)
f.close()

print(f"writing complete for {file_name}")
