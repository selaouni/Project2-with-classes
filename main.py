# import les packages
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin #conversion en https://
from requests.packages.urllib3.exceptions import InsecureRequestWarning # disable warning
import os.path # pour l'ecriture dans les fichiers csv
import urllib.request #pour le téléchargement des images
import re

requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # disable warning


class Scraper:
    def __init__(self,url_site):
        self.url_site = url_site
    def soup(self):
        get_url_page = requests.get(self.url_site)  # Attribution du lien du site avec requests
        page_content = get_url_page.content
        self.data1 = BeautifulSoup(page_content, 'html.parser')  # récupérataion du contenu de la page à scraper
        return self.data1

from soup import Scraper

class site:
    def __init__(self, url_site):
        self.url_site = url_site
        self.category_list = []

    def list_categories_urls(self):
        soup = Scraper(self.url_site).soup()

        for lk in soup.find_all("ul", class_= "nav nav-list"):  #récupération de tous les liens de toutes les catégories
            for i in lk.find("ul").find_all("a"):
                self.category_list.append(i["href"])
            return self.category_list





class Categories:
    def __init__(self, cat_list_urls):
        self.cat_list_urls = cat_list_urls
        self.url_list = []

    def list_urls_books(self):
        for url in self.cat_list_urls:
            category_soup = Scraper(url).soup()
            for lk in category_soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):  # récuperer tous les liens produits de chaque catégorie
                for i in lk.find("div", {"class": "image_container"}).find_all("a"):
                    url_list.append(i["href"])
                return self.url_list

import site

class Extraction:

    def __init__(self,url_page, universal_product_code,title,price_including_tax, price_excluding_tax,number_available,product_description,category,review_rating,image_url):
        self.url_page = url_page
        self.universal_product_code = universal_product_code
        self.title = title
        self.price_including_tax=price_including_tax
        self.price_excluding_tax = price_excluding_tax
        self.number_available = number_available
        self.product_description = product_description
        self.category = category
        self.review_rating = review_rating
        self.image_url = image_url

    def parse (self):
        for url in site.list_categories_urls():
            category_url = urljoin(url_site, url)  # ajout du https:// pour un lien de catégorie valide
            print("Catégorie url: ", category_url)

            while True:  # ajout d'une boucle while pour la pagination
                my_data = Scraper(self.category_url.soup()

                url_list = []
                for lk in my_data.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):  # récuperer tous les liens produits de chaque catégorie
                    for i in lk.find("div", {"class": "image_container"}).find_all("a"):
                        url_list.append(i["href"])

                for url2 in url_list:
                    product_url = urljoin(category_url, url2)  # ajout du https:// pour un lien de livre valide
                    print("Url Produit: ", product_url)

                    my_data2 = Scraper(self.product_url.soup() # url produit récuperé comme instance

                    # -------------url page-----------------------------
                    url_page = product_url
                    print("url page: ", url_page)
                    # ------------code produit-----------------------------
                    universal_product_code_data = my_data2.find("td")
                    universal_product_code = universal_product_code_data.string
                    print("code produit: ", universal_product_code)
                    # ------------titre-------------------------------
                    title_data = my_data2.find("title")
                    title = title_data.string
                    print("titre: ", title)
                    # ------------Prix taxe incluse-----------------------------
                    price_including_tax_Table = my_data2.find("table", {"class": "table table-striped"})
                    price_including_tax_data = price_including_tax_Table.find_all("tr")

                    for td in price_including_tax_data[2].find("td"):
                        price_incl_tax = td.text
                        price_including_tax = price_incl_tax.replace('Â', '')
                        print("Prix taxe incluse: ", price_including_tax)
                    # ------------Prix hors taxes-----------------------
                    price_excluding_tax_Table = my_data2.find("table", {"class": "table table-striped"})
                    price_excluding_tax_data = price_excluding_tax_Table.find_all("tr")

                    for td in price_excluding_tax_data[3].find("td"):
                        price_excl_tax = td.text
                        price_excluding_tax = price_excl_tax.replace('Â', '')
                        print("Prix hors taxes:", price_excluding_tax)
                    # -------------Disponibilité en stock-------------------------
                    number_available_table = my_data2.find("table", {"class": "table table-striped"})
                    number_available_data = number_available_table.find_all("tr")

                    for td in number_available_data[5].find("td"):
                        number_available0 = td
                        number_available = re.findall('\d+', number_available0)[0]
                        print("Disponibilité en stock: ", number_available)

                    # --------------Description du produit------------------------
                    product_description = my_data2.find("meta", {"name": "description"})['content']
                    print("Description du produit:", product_description)
                    # -----------------Catégorie--------------------------------
                    category_table = my_data2.find("ul", {"class": "breadcrumb"})
                    category_data = category_table.find_all("li")

                    for td in category_data[2].find("a"):
                        category = td.text
                        print("Catégorie: ", category)
                    # -------------Review rating-------------------------------

                    review_rating_table = my_data2.find("article", {"product_page"})
                    for i in review_rating_table.find("div", {"class": "col-sm-6 product_main"}).find_all("p"):
                        review_rating_result = i.get('class')

                    if review_rating_result[1] == 'One':
                        review_rating = 1
                    elif review_rating_result[1] == 'Two':
                        review_rating = 2
                    elif review_rating_result[1] == 'Three':
                        review_rating = 3
                    elif review_rating_result[1] == 'Four':
                        review_rating = 4
                    elif review_rating_result[1] == 'Five':
                        review_rating = 5
                    else:
                        review_rating = 0
                    print("Review rating: ", review_rating)

                    # -------------image_url-----------------------------
                    image = my_data2.find("div", {"class": "item active"})
                    for i in image.find_all("img"):
                        url_brut = i.get('src')
                        image_url = urljoin(product_url, url_brut)
                        print("URL image: ", image_url)
                        image_name, ext = (image_url.split('/')[-1].split('.'))
                    urllib.request.urlretrieve(image_url,
                                               str(image_name) + ".jpg")  # Sauvegarde des images de chaque catégorie de livre
                    # ---------------------------------------------------

                    # enregister l'ensemble dans un fichier CSV / catégorie

                    en_tete = ["url_page",
                               "universal_product_code",
                               "title",
                               "price_including_tax",
                               "price_excluding_tax",
                               "number_available",
                               "product_description",
                               "category",
                               "review_rating",
                               "image_url"]

                    filename = str(category) + ".csv"
                    file_exists = os.path.isfile(filename)

                    with open(filename, 'a', encoding="utf-8-sig") as fichier_csv:
                        writer = csv.writer(fichier_csv, delimiter=';', lineterminator='\n')
                        if not file_exists:
                            writer.writerow(en_tete)

                        ligne = [url_page,
                                 universal_product_code,
                                 title,
                                 price_including_tax,
                                 price_excluding_tax,
                                 number_available,
                                 product_description,
                                 category,
                                 review_rating,
                                 image_url]

                        writer.writerow(ligne)

                # passer à la page suivante à parser si vrai

                next_page_element = my_data.select_one('li.next > a')
                if next_page_element:
                    next_page_url = next_page_element.get('href')
                    print("next_page_url", next_page_url)
                    category_url = urljoin(category_url, next_page_url)
                else:
                    break









