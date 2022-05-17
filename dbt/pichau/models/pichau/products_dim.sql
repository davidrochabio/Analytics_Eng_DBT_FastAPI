with source_products as(
    SELECT
        index,
	    id_product,
        name,
        category
    FROM {{ source('pichau', 'products') }}
),

final as(
    SELECT * FROM source_products
)

SELECT * FROM final