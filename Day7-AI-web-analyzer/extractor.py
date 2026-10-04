from bs4 import BeautifulSoup
from fetcher import fetch_page



MAX_CHARS = 8000

def extract_title(html):
    if html is None:
        return None
    soup = BeautifulSoup(html, "html.parser")
    if soup.title is None:
        return None
    return(soup.title.text)





def extract_headings(html):
    if html is None:
        return []
    soup = BeautifulSoup(html,"html.parser")
    headings = soup.find_all(['h1','h2'])
    headings_list = []
    for tags in headings:
        headings_list.append(tags.text.strip())
    return headings_list




def extract_text(html):
    if html is None:
        return ""
    soup = BeautifulSoup(html,"html.parser")
    content = soup.find_all(["p"])
    content_list = []
    for tags in content:
        data = tags.get_text(separator=" ",strip=True)
        if data:
            content_list.append(data)

    full_text = "\n\n".join(content_list)
    return full_text





def trim_text(text,max_chars):
    return text[:max_chars]



if __name__=="__main__":
    var = fetch_page("https://en.wikipedia.org/wiki/Artificial_intelligence")
    title = extract_title(var)
    # print(title)


    headings = extract_headings(var)
    # print(len(headings))
    # print(headings[:10])
    # print(len(extract_headings(None)))

    # print(extract_title("<p>hello</p>"))
    # print(extract_title(None))
    page_text = extract_text((var))
    # print (page_text[:500])



    short_text = trim_text(page_text,MAX_CHARS)
    print(short_text)