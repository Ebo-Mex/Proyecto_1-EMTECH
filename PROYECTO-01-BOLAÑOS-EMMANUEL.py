"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund]
lifestore-products = [id_product, name, price, category, stock]
"""

from lifestore_file import lifestore_products as ls_products
from lifestore_file import lifestore_sales as ls_sales
from lifestore_file import lifestore_searches as ls_searches


def quantify_list(sorted_list):
    reps = 1
    quantified_list = []
    for counter, element in enumerate(sorted_list):
        if counter == len(sorted_list) - 1:
            break
        if element == sorted_list[counter + 1]:
            reps = reps + 1
            continue
        quantified_list.append([element, reps])
        reps = 1
    quantified_list.append([element, reps])
    return quantified_list


def sort_by_n_element(unsorted_list, n, keep_col="a"):
    clean_list = []
    for sub_list in unsorted_list:
        for counter_2, category in enumerate(sub_list):
            if counter_2 == n:
                if isinstance(keep_col, int):
                    clean_list.append([category, sub_list[keep_col]])
                else:
                    clean_list.append(category)
    clean_list.sort()
    return clean_list


""" Save to CSV fun
with open("test_1.csv", "w") as f:
    for sublist in cantidad_vendidos:
        for item in sublist:
            f.write(str(item) + ",")
        f.write("\n")
"""

# 1)
# a) Los 50 + vendidos


productos_vendidos = sort_by_n_element(ls_sales, 1)
cantidad_vendidos = quantify_list(productos_vendidos)
cantidad_vendidos.sort(key=lambda x: x[1], reverse=True)

# b) 100 + buscados

productos_buscados = sort_by_n_element(ls_searches, 1)
cantidad_busquedas = quantify_list(productos_buscados)
cantidad_busquedas.sort(key=lambda x: x[1], reverse=True)

# 2) by category:
productos_categorizados = sort_by_n_element(ls_products, 3, 0)
list_of_categories = list(set(sort_by_n_element(ls_products, 3)))
list_of_categories.sort()

for category in list_of_categories:
    for par in productos_categorizados:
        if par[0] == category:
            print(par)
    print("---------------------------")


# a) list of 50 products with less sells
# b) list of 100 products with less searches

"""
list_of_ids = sort_by_n_element(ls_products, 0)
list_of_sells = list(set(productos_vendidos))

# print(list_of_sells)

didnt_sell = [i for i in list_of_ids if i not in list_of_sells]

print(didnt_sell)
"""
