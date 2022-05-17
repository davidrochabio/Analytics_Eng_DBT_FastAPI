with source_dates as(
    SELECT
	    *
    FROM {{ source('pichau', 'dates') }}
),

final as(
    SELECT * FROM source_dates
)

SELECT * FROM final