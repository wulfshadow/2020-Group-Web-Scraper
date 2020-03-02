#MAGIC HAPPENS
def get_count():
    page_response = requests.get(page_link, timeout=5)
    page_count = BeautifulSoup(page_response.content, "html.parser")
    count = len(page_count.find_all('p'))
    print count
    return(count)

current_count = get_count()

while True:
    page_count = get_count()
    if(current_count != page_count):
        print("Changed")
