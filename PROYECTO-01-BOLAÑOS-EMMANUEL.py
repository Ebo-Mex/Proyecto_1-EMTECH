"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund]
lifestore-products = [id_product, name, price, category, stock]
"""

# importa las listas con los datos
from lifestore_file import lifestore_products as ls_products
from lifestore_file import lifestore_sales as ls_sales
from lifestore_file import lifestore_searches as ls_searches


# Función que cuenta las veces que un elemento se repite
# Regresa el elemento y las repeticiones
def quantify_list(sorted_list):
    # Declara una variable para contar repeticiones
    # y una lista en blanco
    reps = 1
    quantified_list = []
    # Para cada elemento de la lista ingresada
    # asigna un contador y lee el elemento
    for counter, element in enumerate(sorted_list):
        # Si el contador es del tamaño de la lista
        # menos uno, sal del for
        if counter == len(sorted_list) - 1:
            break
        else:
            # Si el elemento actual es igual al siguiente
            # aumenta el numero de repeticiones
            if element == sorted_list[counter + 1]:
                reps = reps + 1
            # De lo contrario, agrega el elemento y
            # sus repeticiones a la lista y regresa
            # la variable que cuenta repeticiones a 1
            else:
                quantified_list.append([element, reps])
                reps = 1
    # Agrega el elemento final a la lista
    quantified_list.append([element, reps])
    return quantified_list


# Función para ordenar una lista de acuerdo a su columna n
# Regresa la columna ordenada
# Opcional: agrega otra columna con keep_col
def sort_by_n_element(unsorted_list, n, keep_col=10):
    # Declara una lista en blanco
    clean_list = []
    # Para cada sublista de la lista ingresada
    for sub_list in unsorted_list:
        # Para cada categoría dentro de la sublista
        # Se asigna un contador para cada categoría
        for counter_2, category in enumerate(sub_list):
            # Si el contador es igual a n,
            # estamos en la columna correcta
            if counter_2 == n:
                # Si el valor keep_col fue cambiado,
                # entonces agrega la columna a la lista
                # Sino, ordena la lista de forma normal
                if keep_col != 10:
                    clean_list.append([category, sub_list[keep_col]])
                else:
                    clean_list.append(category)
    # Ordena la lista de menor a mayor
    clean_list.sort()
    return clean_list


# Función para guardar outputs en formato csv
def save_to_csv(file_name, list_to_save):
    with open("outputs/" + file_name + ".csv", "w") as f:
        for sublist in list_to_save:
            for item in sublist:
                f.write(str(item) + ",")
            f.write("\n")

# 1)
# 1.1.1) Los 50 + vendidos
# Crea una nueva lista con ids de los productos vendidos ordenados
productos_vendidos = sort_by_n_element(ls_sales, 1)
# Lista que muestra cuanto se vendió cada producto
cantidad_vendidos = quantify_list(productos_vendidos)
# Ordena la lista de mayor a menor
cantidad_vendidos.sort(key=lambda x: x[1], reverse=True)
# Guarda resultado en outputs/
# save_to_csv("test_1", cantidad_vendidos)

# 1.1.2) 100 + buscados
# Lista con ids de productos buscados en orden
productos_buscados = sort_by_n_element(ls_searches, 1)
# Cantidad de búsquedas por producto
cantidad_busquedas = quantify_list(productos_buscados)
# Ordena la lista de mayor a menor
cantidad_busquedas.sort(key=lambda x: x[1], reverse=True)
# Guarda resultado en outputs/
# save_to_csv("test_2", cantidad_busquedas)

# 1.2) by category:
# Obtén la lista de categorías
list_of_categories = list(set(sort_by_n_element(ls_products, 3)))
list_of_categories.sort()

cat_and_id = []

# Recorrer la lista de categorías
for category in list_of_categories:
    # Lista temporal para almacenar los ids de cada categoría
    temp = []
    # Recorre sublistas en la lista de productos
    for sublist_2 in ls_products:
        # Si la categoría de la sublista es igual a la
        # categoría actual, almacena en lista temporal
        if sublist_2[3] == category:
            temp.append(sublist_2[0])
    # Agrega la categoría y sus ids a una nueva lista
    cat_and_id.append([category, temp])

# 1.2.1) list of 50 products with less sells
sale_per_cat = []
for ids in cat_and_id:
    tmp = 0
    for sell in productos_vendidos:
        if sell in ids[1]:
            tmp = tmp + 1
    sale_per_cat.append([ids[0], tmp])
    tmp = 0

# 1.2.2) list of 100 products with less searches
# Not yet teehee

"""
lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund]
lifestore-products = [id_product, name, price, category, stock]
"""

# 2)
# 20 best/worst reviews
# Obtén ids para cada producto
product_ids = sort_by_n_element(ls_products, 0)

ids_packed_reviews = []
# Para cada id en la lista de productos
for ids in product_ids:
    # Lista usada para almacenar datos temporalmente
    tmp = []
    # Recorre lista de ventas
    for sell in ls_sales:
        # Si el id de la venta es el mismo que
        # el id actual
        if sell[1] == ids:
            # Agrega la calificación de la venta a
            # la lista temporal
            tmp.append(sell[2])
    # Agrega el id y las calificaciones a una
    # sola sublista de ids_packed_reviews
    ids_packed_reviews.append([ids, tmp])

ids_avg_revs = []
for c, review_pack in enumerate(ids_packed_reviews):
    if len(review_pack[1]) == 0:
        continue
    else:
        avg = sum(review_pack[1])/len(review_pack[1])
        ids_avg_revs.append([review_pack[0], avg])

ids_avg_revs.sort(key=lambda x: x[1], reverse=True)

best_revs = [i for c, i in enumerate(ids_avg_revs) if c < 20]
worst_revs = [i for c, i in enumerate(reversed(ids_avg_revs)) if c < 20]
# Guarda resultado en outputs/
# save_to_csv("test_5", best_revs)
# save_to_csv("test_6", worst_revs)
