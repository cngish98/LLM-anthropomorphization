# Data Sources

Data was collected via manual copy and paste as well as automated scraping from sources such as NPR, The New York Times,
The Atlantic, the Washington Post, Fox News, Wired, Slate, etc.

For copyright reasons, the exact data is not provided but the code to implement scraping on your own is included.

The XML template is also included here as `template_schema.rnc`. We have a `tags` element but there wasn't enough data
for us to use it. 

## To Use Scraper

make sure to install the packages that you need

run with

```python data_scraper.py --url <url> --file <filename> --type <type of data> --source <name of source>```

## Bulk Scraping

To feed in multiple articles and have it scrape consecutively, make updates to `bash.sh` with the url and the file
name/location. It will break if there are issues (ie. missing string), so best to use it after confirming articles are
pulling in as expected.

## Known Issues

Newspaper has a known issue where for many news sites, it seems to only pick up the first paragraph/section of the
article:
https://github.com/codelucas/newspaper/issues/645

We weren't able to get a quick solution & the forked repo changes didn't seem to work for us, so the workaround is to
copy & paste the full body of the article, drop it in a txt document, and overwrite the `main_text` that way.

run with

```python data_scraper.py --text <txt_file_name> --file <filename> --loc <field to replace> --type <podcast, news, etc>```

## Scraper Behavior With Various Sites

### Works Well

- NPR
- The Atlantic
- New York Post
- CNBC
- TechCrunch
- Tom's Guide
- Financial Review
- Business Insider
- Eater

### Works with Bugs

- Daily Mail - misses random chunks of main text
- Fox News - does not grab date
- Medium - does not grab description (subheading/subtitle)
- Futurism - doesn't seem to grab authors or date
- Gizmodo - missing author
- Yahoo! - missing date
- Politico - struggles with author
- Reuters - missing author
- Harvard Business Review - missing author
- Washington Post - missing description
- CBS News - missing date

### Requires Manual Text Substitution

- NYT - will only grab a section of the text & will need to do the workaround to get the full text; does not pick up
  summaries either
  To get all body text in browser, go to Console in browser and enter:
  ```javascript
  $$("article section p").map(node => node.innerText).join('\n')
  ```
- Bloomberg - pulls title, author, etc. but no text body
- MIT Technology Review - does not pull full text

### Crashes & Burns

- CNN - cannot find anything
- Wired - cannot find anything
- Slate - cannot find anything
- Mark Tech Post - cannot find anything
- Wall Street Journal - 403
- Forbes - 403
- Inc. - 403

