"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("ServeTimesDB.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    server, seconds_before_next_point, day, opponent, game_score, sets, game
):
    """create example query"""
    conn = sqlite3.connect("ServeTimesDB.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO ServeTimesDB 
        (server, seconds_before_next_point, day, opponent, game_score, sets, game) 
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (server, seconds_before_next_point, day, opponent, game_score, sets, game),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO ServeTimesDB VALUES (
            {server}, 
            {seconds_before_next_point}, 
            {day}, 
            {opponent}, 
            {game_score}, 
            {sets}, 
            {game});"""
    )


def update_record(
    record_id, server, seconds_before_next_point, day, opponent, game_score, sets, game
):
    """update example query"""
    conn = sqlite3.connect("ServeTimesDB.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE ServeTimesDB 
        SET server=?, 
        seconds_before_next_point=?, 
        day=?, opponent=?, 
        game_score=?, 
        sets=?, 
        game=?
        WHERE id=?
        """,
        (
            server,
            seconds_before_next_point,
            day,
            opponent,
            game_score,
            sets,
            game,
            record_id,
        ),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE ServeTimesDB SET 
        server={server}, 
        seconds_before_next_point=
        {seconds_before_next_point},
        day={day}, opponent={opponent}, 
        game_score={game_score}, 
        sets={sets}, 
        game={game} 
        WHERE id={record_id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("ServeTimesDB.db")
    c = conn.cursor()
    c.execute("DELETE FROM ServeTimesDB WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM ServeTimesDB WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("ServeTimesDB.db")
    c = conn.cursor()
    c.execute("SELECT * FROM ServeTimesDB")
    data = c.fetchall()
    log_query("SELECT * FROM ServeTimesDB;")
    return data
