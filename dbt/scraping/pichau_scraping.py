# %%
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup as bs
from random import randint
import itertools as it

import time
time.sleep(15)

# %%
r = requests.get('https://www.pichau.com.br/hardware/ssd')

print(r.status_code)

# %%
html = r.text
soup = bs(html, features='html5lib')

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

    soup = bs(html, features='html5lib')

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
products.insert(0, 'id_product', [i for i in range(1, len(products)+ 1)])
products['price'] = products['price'].round(decimals=2)
print(products.shape)

# %%
len_products = len(products)
print(len_products)

# %%
locations = pd.read_excel('cities_brazil.xlsx')

# %%
locations['prob'] = locations['population'] / locations['population'].sum()

# %%
import datetime

min_date = datetime.datetime(2021, 7, 1)
max_date = datetime.datetime(2021, 12, 31)

# %%
date_range = pd.date_range(start=min_date, end=max_date, periods=7000)

# %%
np.random.choice(date_range)

# %%
date_range_df = pd.DataFrame({'date': date_range})
date_range_df['year'] = date_range_df['date'].dt.year
date_range_df['quarter'] = date_range_df['date'].dt.quarter
date_range_df['month'] = date_range_df['date'].dt.month
date_range_df['day'] = date_range_df['date'].dt.day
date_range_df['day_of_week'] = date_range_df['date'].dt.dayofweek
date_range_df['hour'] = date_range_df['date'].dt.hour

# %%
import random
from random import randint
import string
random.seed(123)
np.random.seed(123)

orders_dfs = []
orders_details_dfs = []

S = 10

for i in it.chain(range(0, 2027), range(2027, 2900), range(2900, 4870), range(4870, 7026), range(7026, 8390), range(8390, 10039)):
    
    # generate data for orders table
    id_order = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))
    
    date = np.random.choice(date_range)
    
    local_df = locations.sample(1, weights=locations['prob'], axis=0)
    location_code = local_df['location_code'].values[0]
    
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
        
    o = {'id_order': id_order, 'date': date, 'location_code': location_code, 'time_separate': time_to_separate}
    order_df = pd.DataFrame(data=o, index=[i])
    orders_dfs.append(order_df)
        
    # orders_products table data
    order_id_list = [id_order] * qt_products
    order_details_list = np.random.randint(1, high=len_products, size=qt_products)
    num_prod = [1, 2, 3, 4, 5]
    products_qt = np.random.choice(num_prod, qt_products, p=[0.8, 0.1, 0.05, 0.025, 0.025])

    od = {'id_order': order_id_list, 'id_product': order_details_list, 'quantity': products_qt}
    order_details_df = pd.DataFrame(data=od)
    orders_details_dfs.append(order_details_df)

orders = pd.concat(orders_dfs).reset_index(drop=True)
orders = orders.sort_values('date').reset_index(drop=True)
orders_details = pd.concat(orders_details_dfs).reset_index(drop=True)

# %%
print("Products: ", products.shape)
print("Orders: ", orders.shape)
print("Orders details: ", orders_details.shape)

# %%
orders.id_order.nunique()

# %%
products.to_excel('pichau_products.xlsx', index=False)
orders.to_excel('pichau_orders.xlsx', index=False)
orders_details.to_excel('pichau_orders_details.xlsx', index=False)

# %%
from sqlalchemy import create_engine

postgres_engine = create_engine('postgresql://postgres:postgres@postgres:5432/pichau', echo=True) 

# %%
with postgres_engine.connect() as connection:
    result = connection.execute("select * from products limit 5")
    for row in result:
        print(row)

# %%
locations.to_sql('locations', con=postgres_engine, if_exists='replace')

# %%
date_range_df.to_sql('dates', con=postgres_engine, if_exists='replace')

# %%
products.to_sql('products', con=postgres_engine, if_exists='replace')

# %%
orders.to_sql('orders', con=postgres_engine, if_exists='replace')

# %%
orders_details.to_sql('orders_details', con=postgres_engine, if_exists='replace')

# %%
postgres_engine.dispose()

# %% [markdown]
# # --------------------------------


