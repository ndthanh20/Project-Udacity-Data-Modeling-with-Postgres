# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id SERIAL PRIMARY KEY,
                                start_time timestamp NOT NULL,
                                user_id int NOT NULL,
                                level varchar(10),
                                song_id varchar(100),
                                artist_id varchar(100),
                                session_id int,
                                location text,
                                user_agent text);
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS users(
                        user_id int PRIMARY KEY,
                        first_name varchar(100) NOT NULL,
                        last_name varchar(100) NOT NULL,
                        gender char(2),
                        level varchar(10));
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS songs (
                        song_id varchar(1000) PRIMARY KEY NOT NULL,
                        title varchar(1000) NOT NULL,
                        artist_id varchar(100), 
                        year int,
                        duration float8 NOT NULL);
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS artists (
                        artist_id varchar(1000) PRIMARY KEY,
                        name varchar(100) NOT NULL,
                        location varchar(100),
                        latitude float8,
                        longitude float8);
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS time (
                        start_time timestamp NOT NULL, 
                        hour char(2),
                        day char(2),
                        week char(2),
                        month char(2),
                        year int, 
                        weekday char(10));
    
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays (song_id, artist_id)
VALUES (%s, %s) ON CONFLICT (song_id, artist_id) DO NOTHING;
""")

user_table_insert = (""" INSERT INTO users (user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;
""")

song_table_insert = (""" INSERT INTO songs (song_id, title, artist_id, year, duration)
VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = (""" INSERT INTO artists (artist_id, name, location, latitude, longitude)
VALUES(%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = (""" INSERT INTO time (start_time, hour, day, week, month, year, weekday)
VALUES(%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = (""" SELECT song_id, artists.artist_id FROM songs 
                    JOIN artists 
                    ON songs.artist_id = artists.artist_id
                    WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]