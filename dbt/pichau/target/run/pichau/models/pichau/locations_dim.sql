
  create view "pichau"."public"."locations_dim__dbt_tmp" as (
    with source_locations as(
    SELECT
	    *
    FROM "pichau"."public"."locations"
),

final as(
    SELECT * FROM source_locations
)

SELECT * FROM final
  );
