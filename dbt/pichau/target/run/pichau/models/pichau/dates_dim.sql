
  create view "pichau"."public"."dates_dim__dbt_tmp" as (
    with source_dates as(
    SELECT
	    *
    FROM "pichau"."public"."dates"
),

final as(
    SELECT * FROM source_dates
)

SELECT * FROM final
  );
