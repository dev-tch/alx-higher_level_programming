-- lists all genres in the database
-- Results must be sorted in descending order by their rating
SELECT g.name AS genre,
       COUNT(*) AS number_of_shows
  FROM tv_genres AS g
       INNER JOIN tv_show_genres AS t
       ON g.id = t.genre_id
 GROUP BY g.name
 ORDER BY number_of_shows DESC;
