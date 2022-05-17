with source_locations as(
    SELECT
	    *
    FROM {{ source('pichau', 'locations') }}
),

final as(
    SELECT * FROM source_locations
)

SELECT * FROM final