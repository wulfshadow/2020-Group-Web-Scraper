# Will be edited later to find specfic information
# def get_text():
#     page_response = requests.get(page_link, timeout = 5)
#     page_content = BeautifulSoup(page_response.content, "html.parser")
#     text = str(page_content)
#     raw_text = html2text.html2text(text)
#     return(raw_text)

# current_text = get_text()

# For my use later:
# <span class="YVvGBb asQXV">vizceral posted a new assignment: test</span>

from HTMLParser import HTMLParser

# create a subclass and override the handler methods
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Encountered a start tag:", tag

    def handle_endtag(self, tag):
        print "Encountered an end tag :", tag

    def handle_data(self, data):
        print "Encountered some data  :", data

# instantiate the parser and fed it some HTML
parser = MyHTMLParser()
parser.feed('<span class="YVvGBb asQXV">vizceral posted a new assignment: test</span>'
