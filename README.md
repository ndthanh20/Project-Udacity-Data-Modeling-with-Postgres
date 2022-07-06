#                      PROJECT 1: DATA MODELING WITH POSTGRES

## Discuss the purpose of this database in the context of the startup, Sparkify, and their analytical goals.

A Postgres database designed with Star Schema would help the startup access the database and query data easily. And analytics team would understand the data and database easily and would allow the Startup can tuning performance and gain the best revenue. So that their analytical goals can be gained without difficulty.

## How to run the Python scripts

There are two ways to run Python scripts as I know:
- Firstly, we can run Python scripts by running the python file in the terminal with `python` command.
- Secondly, we can run Python scripts through Jupyter Notebook.

## An explanation of the files in the repository:

- sql_queires.py: contains all your sql queries, and is imported into the last three files above.

- etl.py: read and procces files from 'song_data' and 'log_data' and loads them into your tables. You can fill this out based on your work in the ETL notebook.

- test.ipynb: displays the first few rows of each table to let you check your database.

- create_tables.py: drops and creates your tables. Run this file to reset your tables before each time you run your ETL scripts.

- etl.ipynb: reads and processes a single file from 'song_data' and 'log_data' and loads the data into your tables. This notebook contains detailed instructions on the ETL process for each of the tables.

## State and justify your database schema design and ETL pipeline.

### Fact Table
    1. songplays - records in log data associated with song plays i.e. records with page NextSong
         songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
### Dimension Tables
    2. users - users in the app
         user_id, first_name, last_name, gender, level
    3. songs - songs in music database
        song_id, title, artist_id, year, duration
    4. artists - artists in music database
        artist_id, name, location, latitude, longitude
    5. time - timestamps of records in songplays broken down into specific units
        start_time, hour, day, week, month, year, weekday