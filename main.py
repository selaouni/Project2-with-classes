
import Scraper

if __name__ == '__main__':
    scraper = Scraper()
    scraper.get_all_categories()
    scraper.get_all_books()
    scraper.create_csv_books()



















"""

                # passer à la page suivante à parser si vrai

                next_page_element = my_data.select_one('li.next > a')
                if next_page_element:
                    next_page_url = next_page_element.get('href')
                    print("next_page_url", next_page_url)
                    category_url = urljoin(category_url, next_page_url)
                else:
                    break

"""







