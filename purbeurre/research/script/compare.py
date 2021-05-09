from research.models import Product


def compare_products(user_product, product_list):
    """returns a list of objects products with better nutriscore than original"""
    healthier_products = []

    def get_nutriscore(product):
        return product.nutriscore

    for product in product_list:
        if product.nutriscore < user_product.nutriscore:
            healthier_products.append(product)

    return healthier_products.sort(key=get_nutriscore)


def get_similar_prod(cat_set):
    """returns list of barcodes of products w/ same categories as original prod"""
    product_list = []
    for category in cat_set:
        query = Product.objects.filter(product_categories__id=category.id)
        for product in query:
            if product not in product_list:
                product_list.append(product)

    return product_list


def get_product_categories(product):
    """returns list of categories of a product"""
    cat_set = product.product_categories.all()

    return cat_set
