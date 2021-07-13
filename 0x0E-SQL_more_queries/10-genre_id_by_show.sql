-- first dump it the file from the given site to your database
-- then use this to tv_shows.title - tv_sho_genres.genre_id

SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_shows INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
