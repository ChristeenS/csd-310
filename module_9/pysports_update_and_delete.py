import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "pysports_user",
    "password": "seasprite",
    "host": "127.0.0.1",
    "database": "pysports",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)
    print("\nDatabase user {} connected to MySQL on host {} with database {}".format(config["user"],config["host"],config["database"]))

    cursor = db.cursor()
    playerTeamSearch = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"
    cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('smeagol', 'Shire Folk', 1)")
    cursor.execute(playerTeamSearch)
    Players = cursor.fetchall()

    print("-- DISPLAYING PLAYER AFTER INSERT --")
    for Player in Players:
        print("Player ID: {}".format(Player[0]))
        print("First Name: {}".format(Player[1]))
        print("Last Name: {}".format(Player[2]))
        print("Team Name: {}\n".format(Player[3]))

    cursor.execute("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    cursor.execute(playerTeamSearch)
    Players = cursor.fetchall()

    print("-- DISPLAYING PLAYER AFTER UPDATE --")
    for Player in Players:
        print("Player ID: {}".format(Player[0]))
        print("First Name: {}".format(Player[1]))
        print("Last Name: {}".format(Player[2]))
        print("Team Name: {}\n".format(Player[3]))

    cursor.execute("DELETE FROM player WHERE first_name = 'Gollum'")
    cursor.execute(playerTeamSearch)
    Players = cursor.fetchall()

    print("-- DISPLAYING PLAYER AFTER DELETE --")
    for Player in Players:
        print("Player ID: {}".format(Player[0]))
        print("First Name: {}".format(Player[1]))
        print("Last Name: {}".format(Player[2]))
        print("Team Name: {}\n".format(Player[3]))

    input("\n\nPress any key to continue...")
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password are invalid")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")
    else:
        print(err)

finally:
    db.close()