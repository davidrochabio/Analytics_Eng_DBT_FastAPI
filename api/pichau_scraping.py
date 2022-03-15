# %%
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from random import randint
import itertools as it

# %%
r = requests.get('https://www.pichau.com.br/hardware/ssd')

print(r.status_code)

# %%
html = r.text
soup = bs(html)

# %%
with open("html_txt.html", "w", encoding="utf-8") as f:
    f.write(r.text)

# %%
products = soup.find_all('h2')
products_list = []
for i in products:
    txt = i.get_text()
    products_list.append(txt)

print(products_list[0:5])

# %%
prices = soup.find_all('div', class_='jss69')
prices_list = []
for p in prices:
    value = p.get_text()
    prices_list.append(value)

print(prices_list[0:5])

# %%
prices = soup.find_all('div', class_='jss64')
prices_list = []
for p in prices:
    value = p.get_text()
    prices_list.append(value)

print(prices_list)

# %%
urls = ['https://www.pichau.com.br/hardware/processadores/amd', 
        'https://www.pichau.com.br/hardware/processadores/intel',
        'https://www.pichau.com.br/hardware/placa-m-e',
        'https://www.pichau.com.br/hardware/memorias',
        'https://www.pichau.com.br/hardware/placa-de-video',
        'https://www.pichau.com.br/hardware/hard-disk-e-ssd',
        'https://www.pichau.com.br/hardware/ssd',
        'https://www.pichau.com.br/hardware/gabinete',
        'https://www.pichau.com.br/hardware/fonte',
        'https://www.pichau.com.br/perifericos/teclado',
        'https://www.pichau.com.br/perifericos/fone-de-ouvido',
        'https://www.pichau.com.br/perifericos/mouse',
        'https://www.pichau.com.br/monitores']

pichau_products_list = []

for page in urls:
    category = page.split('/')[-1]

    r = requests.get(page)
    print(r.status_code)
    html = r.text

    soup = bs(html)

    products = soup.find_all('h2')
    products_list = []
    for i in products:
        txt = i.get_text()
        products_list.append(txt)
    
    localiz = 'R$' in soup.find_all('div', class_='jss69')[0]

    if localiz:
        prices = soup.find_all('div', class_='jss69')
        prices_list = ['X'] * len(products_list)
        for idx, p in enumerate(prices):
            value = p.get_text()
            prices_list[idx] = value
    else:
        prices = soup.find_all('div', class_='jss64')
        prices_list = ['X'] * len(products_list)
        for idx, p in enumerate(prices):
            value = p.get_text()
            prices_list[idx] = value
    
    category_list = [category] * len(products_list)

    p = {'name': products_list, 'category': category_list, 'price': prices_list}

    df = pd.DataFrame(data=p)

    pichau_products_list.append(df)

products = pd.concat(pichau_products_list).reset_index(drop=True)

# %%
products['price'].replace(to_replace=r"\.", value='', inplace=True, regex=True)
products['price'].replace(to_replace=r",", value='.', inplace=True, regex=True)
products['price'].replace(to_replace=r'R\$', value='', inplace=True, regex=True)

# %%
products = products.loc[products['price'] != 'X', :]

# %%
products['price'] = products['price'].astype('float32')

# %%
products.reset_index(drop=True, inplace=True)
products = products.reset_index().rename(columns={'index': 'id_product'})
products['price'] = products['price'].round(decimals=2)
print(products.shape)

# %%
len_products = len(products) - 1
print(len_products)

# %%
mun = pd.read_excel('cities_brazil.xlsx')

# %%
mun['prob'] = mun['População 2010'] / mun['População 2010'].sum()

# %%
import random
from random import randint
random.seed(123)
np.random.seed(123)

orders_dfs = []
orders_products_dfs = []

for i in it.chain(range(0, 2027), range(2027, 2900), range(2900, 4870), range(4870, 7026), range(7026, 8390), range(8390, 10039)):
    
    # generate data for orders table
    order_id = i
    
    # month
    if i <= 2026:
        month = '1-January'
    elif i <= 2899:
        month = '2-February'
    elif i <= 4868:
        month = '3-March'
    elif i <= 7025:
        month = '4-April'
    elif i <= 8389:
        month = '5-May'
    else:
        month = '6-June'
    
    local_df = mun.sample(1, weights=mun['prob'], axis=0)
    city = local_df['Município'].values[0]
    state = local_df['UF'].values[0]
    region = local_df['Região'].values[0]
    
    # quantity of products of order
    qt_products = randint(1, 10)
    
    # generate variable time_to_separate from normal distributions
    if qt_products <= 2:
        time_to_separate = np.random.normal(loc=4, scale=1, size=1)[0]
    elif qt_products <= 4:
        time_to_separate = np.random.normal(loc=8, scale=1, size=1)[0]
    elif qt_products <= 7:
        time_to_separate = np.random.normal(loc=14, scale=1, size=1)[0]
    else:
        time_to_separate = np.random.normal(loc=20, scale=1, size=1)[0]
        
    o = {'id_order': order_id, 'month': month, 'city': city, 'state': state, 'region': region, 'time_separate': time_to_separate}
    order_df = pd.DataFrame(data=o, index=[i])
    orders_dfs.append(order_df)
        
    # orders_products table data
    order_id_list = [i] * qt_products
    order_products_list = np.random.randint(0, high=len_products, size=qt_products)
    num_prod = [1, 2, 3, 4, 5]
    products_qt = np.random.choice(num_prod, qt_products, p=[0.8, 0.1, 0.05, 0.025, 0.025])

    op = {'id_order': order_id_list, 'id_product': order_products_list, 'quantity': products_qt}
    order_product_df = pd.DataFrame(data=op)
    orders_products_dfs.append(order_product_df)

orders = pd.concat(orders_dfs).reset_index(drop=True)
orders_products = pd.concat(orders_products_dfs).reset_index(drop=True)

# %%
print("Products: ", products.shape)
print("Orders: ", orders.shape)
print("Orders Products: ", orders_products.shape)

# %%
products.to_excel('pichau_products.xlsx', index=False)
orders.to_excel('pichau_orders.xlsx', index=False)
orders_products.to_excel('pichau_orders_products.xlsx', index=False)

# %%
from sqlalchemy import create_engine

postgres_engine = create_engine('postgresql://postgres:postgres@postgres:5432/pichau', echo=True)

i = 50
while i > 0:
    try:
        conn = postgres_engine.connect()
        conn.close()
        break
    except:
        print(i)
        i -= 1
     

# %%

with postgres_engine.connect() as connection:
    result = connection.execute("select * from products limit 5")
    for row in result:
        print(row)

# %%
products.to_sql('products', con=postgres_engine, if_exists='replace')

# %%
orders.to_sql('orders', con=postgres_engine, if_exists='replace')

# %%
orders_products.to_sql('orders_products', con=postgres_engine, if_exists='replace')

# %%
postgres_engine.dispose()

# %% [markdown]
# # --------------------------------


