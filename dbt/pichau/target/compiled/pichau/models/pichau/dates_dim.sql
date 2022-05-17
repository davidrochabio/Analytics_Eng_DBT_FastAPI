with source_dates as(
    SELECT
	    *
    FROM "pichau"."public"."dates"
),

final as(
    SELECT * FROM source_dates
)

SELECT * FROM final