

import requests

import re


# --- Etape 1: Affectation de l'URL du site à scrapper
principal_url = "http://books.toscrape.com/"

# ---Etape 2: acceder au contenu HTML du site web

def get_url_page(url_site):
    url_request = requests.get(url_site)
    data = BeautifulSoup(url_request.content, 'html.parser')
    return data



class Scraper:
    def __init__(self):
        self.list_categories = []

    # --- Etape 3: récupération de tous les liens de toutes les catégories
    def get_all_categories(self):
        data = get_url_page(principal_page)
        get_first_ul = data.find('ul', {"class": "nav-list"})
        get_ul = get_first_ul.find('ul')
        list_books_category = get_ul.find_all('li')
        for li in list_books_category:
            category_name_in_link = li.find('a')['href'].split('/')[3]
            category = Category(category_name_in_link)
            self.list_categories.append(category)

    # --- Etape 4: récupération de tous les liens produit par catégorie
    def get_all_books(self):
        for url in self.list_categories:
            category_url = urljoin(url_site, url)
            print("Catégorie url: ", category_url)

    # --- Etape 5: récupération des données par livre
    def parser_site(self, url_book):
            data = get_url_page(url_book)
            # ajout d'une boucle while pour la pagination
            while True:
                my_data = get_url_page(self.category_url)

                url_list = []
                for lk in my_data.find_all("li",class_="col-xs-6 col-sm-4 col-md-3 col-lg-3"):  # récuperer tous les liens produits de chaque catégorie
                    for i in lk.find("div", {"class": "image_container"}).find_all("a"):
                        url_list.append(i["href"])

                for url2 in url_list:
                    product_url = urljoin(category_url, url2)
                    print("Url Produit: ", product_url)

                    my_data2 = get_url_page(self.product_url)

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
                    urllib.request.urlretrieve(image_url, str(image_name) + ".jpg")  # Sauvegarde des images de chaque catégorie de livre
                    # ---------------------------------------------------

    book_data = Book(title_book, category_book, product_description, universal_product_code,
                    price_including_tax, price_excluding_tax, number_available, review_rating, url_page, image_url)

    return book_data