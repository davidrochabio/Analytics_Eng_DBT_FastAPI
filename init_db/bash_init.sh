#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS public.products (
        id INT NOT NULL,
        product_id INT NOT NULL,
        nome VARCHAR(500) NOT NULL,
        categoria VARCHAR(250) NOT NULL,
        preco_unit NUMERIC NOT NULL,
        PRIMARY KEY (id)
    );

    CREATE TABLE IF NOT EXISTS public.orders (
        id INT NOT NULL,
        order_id INT NOT NULL,
        mes VARCHAR(50) NOT NULL,
        cidade VARCHAR(250) NOT NULL,
        uf VARCHAR(3) NOT NULL,
        regiao VARCHAR(50) NOT NULL,
        tempo_separacao NUMERIC NOT NULL,
        PRIMARY KEY (id)
    );
    
    CREATE TABLE IF NOT EXISTS public.orders_products (
        id INT NOT NULL,
        order_id INT NOT NULL,
        product_id INT NOT NULL,
        quantidade INT NOT NULL,
        PRIMARY KEY (id)
    );
EOSQL