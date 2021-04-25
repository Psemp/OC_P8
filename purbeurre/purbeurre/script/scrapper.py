import requests
from research.models import Product, Category, Store

product_list = []
category_list = []

page_api = 1

category_url = 'https://fr-fr.openfoodfacts.org/categories.json'
r = requests.get(category_url)
category_page = r.json()


def FiltersOnId(catid):
    """filters double categories (x AND y)"""
    if '-and-' in catid:
        return True
    else:
        return False


def FiltersOnProductCnt(number):
    """defines the relevance of a category by the number of products in it"""
    if number > 200 and number < 5500:
        return True
    else:
        return False


def FilterOnTranslation(catname):
    """returns true if a category has been translated, non translated categories"""
    """ look like -> en:catname """
    if catname[2] == ":":
        return False
    else:
        return True


def BarcodeTest(barcode):
    """returns true if a barcodes is 13 numbers long, ie a valid barcode"""
    if len(barcode) == 13:
        return True
    elif len(barcode) < 13:
        return False
    else:
        return False


def SectionsInProduct(prod):
    """returns true if relevant sections are in the product description"""
    if 'product_name' in prod and 'categories_hierarchy' in prod and 'brands' in prod and 'nutriscore_grade' in prod and 'stores' in prod:
        return True
    else:
        return False


for web_category in category_page['tags']:

    if FiltersOnProductCnt(web_category['products']) and FiltersOnId(web_category['id']) and FilterOnTranslation(web_category['name']):
        category_list.append(Category(web_category['id'], web_category['name'], web_category['url'], web_category['products']))

idgen = 1

for category in category_list:
    category.id = idgen
    idgen += 1

product_place_in_list = 0
barcode_dict = {}

for category in reversed(category_list):

    page_api = 1

    while page_api < 2:  # (category.amount/20):
        formatted_url = category.link + f'/{page_api}.json'
        r = requests.get(formatted_url)
        productlist_page = r.json()
        print(formatted_url)

        for web_product in productlist_page['products']:

            if SectionsInProduct(web_product) and BarcodeTest:

                if web_product['_id'] not in barcode_dict:

                    barcode_dict[web_product['_id']] = product_place_in_list
                    if 'url' in web_product:
                        product_list.append(Product(web_product['_id'], web_product['product_name'], web_product['brands'], web_product['nutriscore_grade'], web_product['url'], web_product['stores']))
                        product_list[product_place_in_list].category_id.append(category.id)
                    else:
                        product_list.append(Product(web_product['_id'], web_product['product_name'], web_product['brands'], web_product['nutriscore_grade'], 'https://seashepherd.org', web_product['stores']))
                        product_list[product_place_in_list].category_id.append(category.id)
                    product_place_in_list += 1

                else:

                    pass

        page_api += 1
