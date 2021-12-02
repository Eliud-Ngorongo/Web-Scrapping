from bs4 import BeautifulSoup
import requests

# with open('8-index.html', 'r') as index:
#     content = index.read()
#
#     soup = BeautifulSoup(content, 'html.parser')
#     locations = soup.find_all('div', class_='locations')
#     for location in locations:
#         print(location.h3.text)


def search_engine(text):
    html_text = requests.get('https://ke.ncbagroup.com/accounts/savings-accounts').text  # respose 200
    soup = BeautifulSoup(html_text, 'html.parser')
    savings = soup.find_all('h5', class_='mb-0 collapsed')
    print("NCBA has the following savings accounts: ")
    i = 1
    for saving in savings:
        print(i, saving.text.replace(" ", ''))  # show types of savings accounts offered by NCBA
        i += 1



# """This part retrives all links in the NCBA website"""
# html_text = requests.get('https://ke.ncbagroup.com/accounts/savings-accounts').text # respose 200
# soup = BeautifulSoup(html_text, 'html.parser')
# for link in soup.find_all("a", href=True):
#      if 'acc' in link:
#         print(link['href'])


