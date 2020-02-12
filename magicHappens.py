# Will be edited later to find specfic information
def get_text():
    page_response = requests.get(page_link, timeout=5)
    page_content = BeautifulSoup(page_response.content, "html.parser")
    text = str(page_content)
    raw_text = html2text.html2text(text)
    return(raw_text)

current_text = get_text()

# For my use later:
# <span class="YVvGBb asQXV">vizceral posted a new assignment: test</span>
