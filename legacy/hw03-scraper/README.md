# tomato-scraper

## Install Dependencies

Once you have choco/brew, python, and poetry installed...

    brew install chromedriver (macos terminal)
>
    choco install chromedriver (windows powershell [as admin])
>
    poetry config virtualenvs.in-project true
>
    poetry install

## Run

    poetry run python tomato-scraper.py

## Sqlite Notes

    -- pip install sqlite-web

    -- sqlite3 cache.db
    -- sqlite_web cache.db

    -- .tables
    SELECT key FROM scraper;
    SELECT COUNT(*) FROM scraper;
    PRAGMA table_info(scraper);
    SELECT * FROM scraper WHERE key LIKE '%thor%';
    -- .quit


    -- sqlite3 tomatoes.db
    -- sqlite_web tomatoes.db

    -- .tables

    SELECT name FROM movies;

    SELECT name FROM movies WHERE release >= date('now','start of month','-24 months');

    SELECT movies.name, genres.name FROM movies LEFT JOIN map_movie_genre ON map_movie_genre.movie_id = movies.id INNER JOIN genres ON genres.id = map_movie_genre.genre_id;

    SELECT movies.name, genres.name FROM movies LEFT JOIN map_movie_genre ON map_movie_genre.movie_id = movies.id INNER JOIN genres ON genres.id = map_movie_genre.genre_id WHERE genres.id = 'action';
    
    SELECT movies.name, celebs.name FROM movies LEFT JOIN map_movie_celeb ON map_movie_celeb.movie_id = movies.id INNER JOIN celebs ON celebs.id = map_movie_celeb.celeb_id WHERE celebs.name LIKE '%John%';

    SELECT meter+score, name FROM movies ORDER BY meter+score DESC;
    
    -- .quit
