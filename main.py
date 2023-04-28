from bs4 import BeautifulSoup
import requests

def med_info():
    salt = input()
    html_text = requests.get("https://www.apollopharmacy.in/salt/"+salt).text
    soup = BeautifulSoup(html_text,'lxml')
    info = soup.find_all("div", class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[0].h2.text
    print(h2_1)
    print()
    h2_data_1 = info[0].p.text
    print(h2_data_1)
    print()
    print()

    info = soup.find_all("div",class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[1].h2.text
    print(h2_1)
    print()
    h2_data_1 = info[1].p.text
    print(h2_data_1)
    print()
    print()

    info = soup.find_all("div", class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[2].h2.text
    print(h2_1)
    print()
    h2_data_1 = info[2].p.text
    print(h2_data_1)
    print()
    print()

    info = soup.find_all("div", class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[3].h2.text
    print(h2_1)
    print()
    h2_data_1 = info[3].div.text
    print(h2_data_1)
    print()
    print()

    info = soup.find_all("div", class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[4].h2.text
    print(h2_1)
    print()
    h2_data_1 = info[4].div.text
    print(h2_data_1)
    print()
    print()

    info = soup.find_all("div", class_="ProductDetailsGeneric_descListing__w3wG3")
    h2_1 = info[5].h2.text
    print(h2_1)
    h2_data_1 = info[5].div.text
    print(h2_data_1)

    print("List of medicines : ")
    print()

    med_cards = soup.find_all("div",class_="SaltMedicines_saltLink__7cBrq")
    for med in med_cards:
        name = med.p.text
        price = med.find("span",class_="SaltMedicines_mrpBx__mwrKA").text
        print("Name of medicine : " + name)
        print("Price of medicine : " + price)

med_info()

