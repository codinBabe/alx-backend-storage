-- A script that ranks country origins of bands, 
-- ordered by the number of (non-unique) fans

WITH fans AS (
    SELECT band_id, COUNT(*) AS nb_fans
    FROM fans
    GROUP BY band_id
)