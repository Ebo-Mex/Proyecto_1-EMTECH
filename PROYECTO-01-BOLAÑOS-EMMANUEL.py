"""
This is the LifeStore-SalesList data:

lifestore-searches = [id_search, id product]
lifestore-sales = [id_sale, id_product, score (from 1 to 5), date, refund]
lifestore-products = [id_product, name, price, category, stock]
"""

# CAMBIAR LOS LAMBDA!
# FINISH 1.2.2

# importa las listas con los datos
from lifestore_file import lifestore_products as ls_products
from lifestore_file import lifestore_sales as ls_sales
from lifestore_file import lifestore_searches as ls_searches


# Función que cuenta las veces que un elemento se repite
# List ingresada debe estar en orden
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
        # menos uno, sal del bucle
        if counter == len(sorted_list) - 1:
            break
        # Si el elemento actual es igual al siguiente
        # aumenta el numero de repeticiones
        elif element == sorted_list[counter + 1]:
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
# Regresa solo la columna ordenada
# Opcional: agrega otra columna con keep_col
# ordena en de mayor a menor con rev = True
def sort_by_n_element(unsorted_list, n, keep_col=10, rev=False):
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
    # Ordena la lista de menor a mayor a menos de que rev sea verdadero
    if not rev:
        clean_list.sort()
    else:
        clean_list.sort(reverse=True)
    return clean_list


# Función para guardar outputs en formato csv
def save_to_csv(file_name, list_to_save):
    with open("outputs/" + file_name + ".csv", "w") as f:
        for sublist in list_to_save:
            for item in sublist:
                f.write(str(item) + ",")
            f.write("\n")


# Función para regresar ids que no han sido comprados o buscados
def didnt_appear(a, x, b, y):
    """

    :param a: list with all the ids
    :param x: column of ids in a
    :param b: list with some ids
    :param y: column of ids in b
    :return: list with sublists of the form [0, id]
    """
    new_list = []
    for sblst in a:
        c = 0
        for sblst_2 in b:
            if sblst[x] == sblst_2[y]:
                c = c + 1
        if c == 0:
            new_list.append([0, sblst[0]])
    return new_list


# Función para regresar solo el nombre del producto
def prod_name(names):
    product_name_0 = names.find(",")
    if product_name_0 == -1:
        return product_name_0
    return names[:product_name_0]


# 1.1)
# Los 50 + vendidos
# Crea una nueva lista con ids de los productos vendidos
# ordenados de menor a mayor
productos_vendidos = sort_by_n_element(ls_sales, 1)
# Lista que muestra cuanto se vendió cada producto
cantidad_vendidos = quantify_list(productos_vendidos)
# Ordena la lista de mayor a menor
total_vendidos_y_ids = sort_by_n_element(cantidad_vendidos, 1, 0, rev=True)
# Lista con productos que no se vendieron
producto_no_vendido = didnt_appear(ls_products, 0, ls_sales, 1)
# Agregar productos no vendidos al final de la lista
total_vendidos_y_ids = total_vendidos_y_ids + producto_no_vendido
# Cambiar ids a nombres para hacer amigable a la lectura
for id_lst in total_vendidos_y_ids:
    for prd_lst in ls_products:
        if id_lst[1] == prd_lst[0]:
            id_lst[1] = prod_name(prd_lst[1])
# Crea la lista final con solo 50 valores
if len(total_vendidos_y_ids) <= 49:
    print("\nNo se cuenta con 50 productos o más, mostrando", len(total_vendidos_y_ids), "productos\n")
    final_total_vendidos_y_ids = total_vendidos_y_ids
else:
    final_total_vendidos_y_ids = total_vendidos_y_ids[0:50]
"""
# Quitar comentarios para mostrar resultados
print("\n\nLista de productos vendidos (mayor a menor)\n")
for out_vendidos_ids in final_total_vendidos_y_ids:
    if out_vendidos_ids[0] >= 2:
        print(out_vendidos_ids[1], "se ha vendido", out_vendidos_ids[0], "veces" "\n")
    elif out_vendidos_ids[0] == 1:
        print(out_vendidos_ids[1], "se ha vendido", out_vendidos_ids[0], "vez" "\n")
    else:
        print(out_vendidos_ids[1], "no se ha vendido" "\n")
# Guarda resultado en outputs/test_0.csv
final_total_vendidos_y_ids = [["Ventas", "Nombre del producto"]] + final_total_vendidos_y_ids
save_to_csv("test_0", final_total_vendidos_y_ids)
"""

# 100 + buscados
# Lista con ids de productos buscados en orden
productos_buscados = sort_by_n_element(ls_searches, 1)
# Cantidad de búsquedas por producto
cantidad_busquedas = quantify_list(productos_buscados)
# Ordena la lista de mayor a menor
total_busqueda_y_ids = sort_by_n_element(cantidad_busquedas, 1, 0, rev=True)
# Lista de producto no buscado
producto_no_buscado = didnt_appear(ls_products, 0, ls_searches, 1)
total_busqueda_y_ids = total_busqueda_y_ids + producto_no_buscado
# Cambiar ids a nombres para hacer amigable a la lectura
for id_lst in total_busqueda_y_ids:
    for prd_lst in ls_products:
        if id_lst[1] == prd_lst[0]:
            id_lst[1] = prod_name(prd_lst[1])
# Crea la lista final con solo 100 valores
if len(total_busqueda_y_ids) <= 99:
    print("\nNo se cuenta con 100 productos o más, mostrando", len(total_busqueda_y_ids), "productos\n")
    final_total_buscados_y_ids = total_busqueda_y_ids
else:
    final_total_buscados_y_ids = total_busqueda_y_ids[0:100]
"""
# Quitar comentarios para mostrar resultados
print("\n\nLista de productos buscados (mayor a menor)\n")
for out_buscados_ids in final_total_buscados_y_ids:
    if out_buscados_ids[0] >= 2:
        print(out_buscados_ids[1], "se ha buscado", out_buscados_ids[0], "veces" "\n")
    elif out_buscados_ids[0] == 1:
        print(out_buscados_ids[1], "se ha buscado", out_buscados_ids[0], "vez" "\n")
    else:
        print(out_buscados_ids[1], "no se ha buscado" "\n")
# Guarda resultado en outputs/test_0.csv
final_total_buscados_y_ids = [["Búsquedas", "Nombre del producto"]] + final_total_buscados_y_ids
save_to_csv("test_1", final_total_buscados_y_ids)
"""

# 1.2) Por categoría
# Obtén la lista de categorías
list_of_categories_shuffled = sort_by_n_element(ls_products, 3)
list_of_categories = []
for cat in list_of_categories_shuffled:
    if cat not in list_of_categories:
        list_of_categories.append(cat)
list_of_categories.sort()
# Lista para almacenar categoria y sus ids
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

# Categorías con menos ventas
sale_per_cat = []
# Recorrer sublistas de ids de categorías
for ids in cat_and_id:
    tmp = 0
    # Recorre lista de ventas
    for sell in ls_sales:
        # Si id se encuentra en lista de ventas
        # aumentar contador
        if sell[1] in ids[1]:
            tmp = tmp + 1
    # Agregar categoría y cuenta de ventas a la lista
    # reiniciar contador
    sale_per_cat.append([ids[0], tmp])
    tmp = 0
# Ordenar de categorías con ventas de menor a mayor
sale_per_cat = sort_by_n_element(sale_per_cat, 1, 0)
"""
# Quitar comentarios para mostrar resultados
print("\nLista de ventas por categoría (menor a mayor) \n")
for ventas_x_cat in sale_per_cat:
    if ventas_x_cat[0] >= 2:
        print("La categoría de", ventas_x_cat[1], "se ha vendido", ventas_x_cat[0], "veces \n")
    elif ventas_x_cat[0] == 1:
        print("La categoría de", ventas_x_cat[1], "se ha vendido", ventas_x_cat[0], "vez \n")
    else:
        print("La categoría de", ventas_x_cat[1], "no se ha vendido \n")
# Guarda resultados en csv
sale_per_cat = [["Ventas", "Categoría"]] + sale_per_cat
save_to_csv("cat_con_menos_ventas", sale_per_cat)
"""

# Categorías con menos búsquedas
search_per_cat = []
# Recorrer sublistas de ids y categorías
for ids in cat_and_id:
    tmp = 0
    # Recorre lista de ventas
    for search in ls_searches:
        # Si id se encuentra en lista de ventas
        # aumentar contador
        if search[1] in ids[1]:
            tmp = tmp + 1
    # Agregar categoría y cuenta de búsquedas a la lista
    # reiniciar contador
    search_per_cat.append([ids[0], tmp])
    tmp = 0
search_per_cat = sort_by_n_element(search_per_cat, 1, 0)
"""
# Quitar comentarios para mostrar resultados
print("\nLista de búsquedas por categoría (menor a mayor) \n")
for busq_x_cat in search_per_cat:
    if busq_x_cat[0] >= 2:
        print("La categoría de", busq_x_cat[1], "se ha buscado", busq_x_cat[0], "veces \n")
    elif busq_x_cat[0] == 1:
        print("La categoría de", busq_x_cat[1], "se ha buscado", busq_x_cat[0], "vez \n")
    else:
        print("La categoría de", busq_x_cat[1], "no se ha buscado \n")
# Guarda resultados en csv
search_per_cat = [["Búsqueda", "Categoría"]] + search_per_cat
save_to_csv("cat_con_menos_búsquedas", search_per_cat)
"""

# 2)
# 20 mejores/peores reseñas
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
# Calificación promedio para cada producto
ids_avg_revs = []
for c, review_pack in enumerate(ids_packed_reviews):
    if len(review_pack[1]) != 0:
        avg = sum(review_pack[1])/len(review_pack[1])
        ids_avg_revs.append([review_pack[0], avg])
# Ordenar calificación de productos de menor a mayor
ids_avg_revs = sort_by_n_element(ids_avg_revs, 1, 0)
# Cambiar ids a nombres
for id_lst in ids_avg_revs:
    for prd_lst in ls_products:
        if id_lst[1] == prd_lst[0]:
            id_lst[1] = prod_name(prd_lst[1])
# Ordenar ids para cada output
worst_revs = ids_avg_revs[0:20]
best_revs = ids_avg_revs[-1:-21:-1]
"""
# Quitar comentarios para mostrar resultados
print("\nLista de mejores calificaciones \n")
for rev_1 in best_revs:
    print(rev_1[1], "tiene una calificación de", rev_1[0], "\n")
print("\nLista de peores calificaciones \n")
for rev_2 in worst_revs:
    print(rev_2[1], "tiene una calificación de", rev_2[0], "\n")
best_revs = [["Producto", "Calificación"]] + best_revs
worst_revs = [["Producto", "Calificación"]] + worst_revs
# Guarda resultado en outputs/
save_to_csv("mejor_calificación", best_revs)
save_to_csv("peor_calificación", worst_revs)
"""

# 3)
# Total ingresos y ventas promedio mensuales,
# total anual y meses con más ventas al año
# ans1 = ingresos, ventas prom x mes
# ans2 = total anual <- anual_income, total_sells
# ans3, highlight meses con mas ventas

# Lista de ids, con mes y año de venta
ids_and_dates = []
for sublist_3 in ls_sales:
    ids_and_dates.append([sublist_3[1], int(sublist_3[3][3:5]), int(sublist_3[3][6:10])])
# Lista de los años con ventas
list_of_years_shuffled = sort_by_n_element(ids_and_dates, 2)
list_of_years = []
for yr in list_of_years_shuffled:
    if yr not in list_of_years:
        list_of_years.append(yr)
# Lista de ventas para cada año
ids_2002 = []
ids_2019 = []
ids_2020 = []
for year in ids_and_dates:
    if year[2] == list_of_years[0]:
        ids_2002.append(year)
    elif year[2] == list_of_years[1]:
        ids_2019.append(year)
    else:
        ids_2020.append(year)
# Lista de meses con ventas
list_of_months_shuffled = sort_by_n_element(ids_2020, 1)
list_of_months = []
for mt in list_of_months_shuffled:
    if mt not in list_of_months:
        list_of_months.append(mt)
# Lista con ids contabilizados y ordenados por mes
org_ids_2020 = []
for n in list_of_months:
    counter = 0
    ids_temp = []
    for i in ids_2020:
        if i[1] == n:
            counter = counter + 1
            ids_temp.append(i[0])
    org_ids_2020.append([ids_temp, counter, n])
# Lista de ids con precios
ids_prices = sort_by_n_element(ls_products, 0, 2)
# Obtenemos los ingresos por mes, los ingresos anuales
# y el total de ventas
income_per_month = []
anual_income = 0
total_sells = 0
for month in org_ids_2020:
    income = 0
    for i_id_price in ids_prices:
        for n_id in range(len(month[0])):
            if month[0][n_id] == i_id_price[0]:
                income = income + int(i_id_price[1])
                anual_income = anual_income + int(i_id_price[1])
                total_sells = total_sells + 1
    income_per_month.append([income, month[1], month[2]])
# Promedio mensual
prom_mensual = int(total_sells/len(list_of_months))
# Obtener lista de meses con mejores ventas (arriba del promedio)
highlight_month = []
for list_i in income_per_month:
    if list_i[1] > prom_mensual:
        highlight_month.append(list_i)

print("\nIngreso anual:", anual_income, "\nVentas totales:",  total_sells)

print("\nPromedio mensual de ventas:", prom_mensual)

print("\nIngresos y ventas por mes\n", income_per_month)

print("\nMejores meses\n", highlight_month)
