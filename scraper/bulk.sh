#$/bin/sh

for i in \
"https://hbr.org/2023/02/how-ai-will-transform-project-management","news-cl-206" \
; do IFS=","; set -- $i; python data_scraper.py --file "news/$2" --url "$1" --type "news" --source "Harvard Business Review"; done
