
import csv
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning # disable warning
import os.path


requests.packages.urllib3.disable_warnings(InsecureRequestWarning) # disable warning


class Categories:
    def __init__(self, name):
        self.name = name
        self.books = []


        def create_csv(self):

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






"""

    def list_urls_books(self):
        for url in self.cat_list_urls:
            category_soup = Scraper(url).soup()
            for lk in category_soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):  # récuperer tous les liens produits de chaque catégorie
                for i in lk.find("div", {"class": "image_container"}).find_all("a"):
                    url_list.append(i["href"])
                return self.url_list


"""