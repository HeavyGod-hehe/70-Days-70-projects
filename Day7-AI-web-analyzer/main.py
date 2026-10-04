from fetcher import fetch_page
from extractor import extract_headings,extract_text,extract_title,trim_text
from AI_service import Analyze


MAX_CHARS = 8000




while True:
    url = input("Type Your URL here  or Type EXIT to Quit : ").strip()
    
    
    if url.lower() == "exit":
        break
    if not url : continue

    html = fetch_page(url)
    if html is None : continue
    headings  = extract_headings(html)
    title = extract_title(html)
    text = extract_text(html)
    if not text:continue
    trimmed_text = trim_text(text=text,max_chars=MAX_CHARS)
    Summary = Analyze(headings=headings,title=title,text=trimmed_text)
    if Summary is None:
        print("There Was a Error ")
        continue
    print(Summary)