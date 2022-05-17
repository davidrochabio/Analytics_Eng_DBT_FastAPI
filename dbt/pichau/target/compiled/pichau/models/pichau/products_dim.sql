with source_products as(
    SELECT
	    id_product,
        name,
        category
    FROM "pichau"."public"."products"
),

final as(
    SELECT * FROM source_products
)

SELECT * FROM final