-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>

SELECT
    tv_genres.genre AS genre,
    COUNT(*) AS number_of_shows
FROM
    tv_genres
JOIN
    tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY
    tv_genres.genre
ORDER BY
    number_of_shows DESC;
