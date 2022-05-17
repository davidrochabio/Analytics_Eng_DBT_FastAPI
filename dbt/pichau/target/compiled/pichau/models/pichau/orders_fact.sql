with source_orders as(
    SELECT
	    od.index,
	    o.id_order,
	    o.date,
	    o.location_code,
	    p.id_product,
	    od.quantity,
	    p.price AS unit_price,
	    (od.quantity * p.price) AS prod_final_price
    FROM "pichau"."public"."orders_details" AS od
    LEFT JOIN "pichau"."public"."orders" AS o
    ON od.id_order = o.id_order
    LEFT JOIN "pichau"."public"."products" AS p
    ON od.id_product = p.id_product
),

final as(
    SELECT * FROM source_orders
)

SELECT * FROM final