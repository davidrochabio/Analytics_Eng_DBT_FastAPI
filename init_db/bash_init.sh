#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE TABLE IF NOT EXISTS public.products (
        index INT NOT NULL,
        id_product INT NOT NULL,
        name VARCHAR(500) NOT NULL,
        category VARCHAR(250) NOT NULL,
        price NUMERIC NOT NULL,
        PRIMARY KEY (index)
    );

    CREATE TABLE IF NOT EXISTS public.orders (
        index INT NOT NULL,
        id_order VARCHAR(10) NOT NULL,
        date TIMESTAMP NOT NULL,
        location_code INT NOT NULL,
        time_separate NUMERIC NOT NULL,
        PRIMARY KEY (index)
    );
    
    CREATE TABLE IF NOT EXISTS public.orders_details (
        index INT NOT NULL,
        id_order VARCHAR(10) NOT NULL,
        id_product INT NOT NULL,
        quantity INT NOT NULL,
        PRIMARY KEY (index)
    );
EOSQL