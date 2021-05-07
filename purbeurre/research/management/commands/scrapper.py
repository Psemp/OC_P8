import requests
from research.models import Product, Category


# FILTERS #


def filters_id(catid):
    """filters double categories (x AND y)"""
    if '-and-' in catid:
        return True
    else:
        return False


def filters_cnt(number):
    """defines the relevance of a category by the number of products in it"""
    if number > 200 and number < 5500:
        return True
    else:
        return False


def filter_translate(catname):
    """returns true if a category has been translated, non translated categories"""
    """ look like -> en:catname """
    if catname[2] == ":":
        return False
    else:
        return True


def sections_in_prod(prod):
    """returns true if relevant sections are in the product description"""
    if 'product_name' in prod and 'categories_hierarchy' in prod and 'brands' in prod and 'nutriscore_grade' in prod and 'stores' in prod:
        return True
    else:
        return False

# /FILTERS #


def get_categories():
    """Scans and saves categories in DB from URL"""
    category_url = 'https://fr-fr.openfoodfacts.org/categories.json'
    r = requests.get(category_url)
    category_page = r.json()

    for category in category_page['tags']:

        if filters_cnt(category['products']) and filters_id(category['id']) and filter_translate(category['name']):
            c = Category(name=category['id'], translated_name=category['name'],
                         url=category['url'], amount=category['products'])
            c.save()


def get_products():
    """Scans and saves relevant products per categories in DB"""
    barcode_list = []
    cat_obj_list = Category.objects.all()

    for category in cat_obj_list:
        page_api = 1

        while page_api < (category.amount/20):  # +/- 20 products per page
            formatted_url = category.url + f'/{page_api}.json'
            r = requests.get(formatted_url)
            products_page = r.json()
            print(formatted_url)

            for product in products_page:
                if product['_id'] in barcode_list:
                    p = Product.object.get(barcode=product['_id'])
                    p.product_categories.add(category.pk)
                    p.save()
                elif product['_id'] not in barcode_list:
                    p = Product(barcode=product['_id'], name=product['product_name'], url=product['url'],
                                brand=product['brands'], picture_url=product['image_front_url'])
                    p.product_categories.add(category.pk)
                    barcode_list.append(product['_id'])
                    p.save()


# for category in reversed(category_list):

#     page_api = 1

#     while page_api < 2:  # (category.amount/20):
#         formatted_url = category.link + f'/{page_api}.json'
#         r = requests.get(formatted_url)
#         productlist_page = r.json()
#         print(formatted_url)

#         for web_product in productlist_page['products']:

#             if SectionsInProduct(web_product) and BarcodeTest:

#                 if web_product['_id'] not in barcode_dict:

#                     barcode_dict[web_product['_id']] = product_place_in_list
#                     if 'url' in web_product:
#                         product_list.append(Product(web_product['_id'], web_product['product_name'], web_product['brands'], web_product['nutriscore_grade'], web_product['url'], web_product['stores']))
#                         product_list[product_place_in_list].category_id.append(category.id)
#                     else:
#                         product_list.append(Product(web_product['_id'], web_product['product_name'], web_product['brands'], web_product['nutriscore_grade'], 'https://seashepherd.org', web_product['stores']))
#                         product_list[product_place_in_list].category_id.append(category.id)
#                     product_place_in_list += 1

#                 else:

#                     pass

#         page_api += 1


##############
# 1. Get Categories
# 2. Get Product per categories and save barcodes
# 3.1. If Barcode not saved, save product and assign category
# 3.2. If Barcode saved, add category to product(defined by barcode)
##############
