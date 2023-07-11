file_path = "C:/Users/katie/PycharmProjects/FoundationHomework/file.sql"

# Open the SQL file in write mode
sql_file = open(file_path, "w")

# Write SQL statements to the file
sql_file.write("CREATE TABLE movie_info (Movie_ID INT, Movie_Name VARCHAR(50), Movie_Length TIME, Age_Rating VARCHAR(5));\n")
sql_file.write("CREATE TABLE screens (Screen_ID INT, Four_K BOOLEAN);\n")
sql_file.write("CREATE TABLE showings (Showing_ID INT, Movie_ID INT, Screen_ID INT, Start_Time TIME, Available_Seats INT);\n")


file_path = "C:/Users/katie/PycharmProjects/FoundationHomework/file.sql"

# Open the SQL file in append mode (to preserve existing content)
with open(file_path, "a") as sql_file:
    sql_file.write("\n")
    sql_file.write("CREATE TABLE movie_info (\n")
    sql_file.write("    Movie_ID INT,\n")
    sql_file.write("    Movie_Name VARCHAR(50),\n")
    sql_file.write("    Movie_Length TIME,\n")
    sql_file.write("    Age_Rating VARCHAR(5)\n")
    sql_file.write(");\n\n")

    sql_file.write("CREATE TABLE screens (\n")
    sql_file.write("    Screen_ID INT,\n")
    sql_file.write("    Four_K BOOLEAN\n")
    sql_file.write(");\n\n")

    sql_file.write("CREATE TABLE showings (\n")
    sql_file.write("    Showing_ID INT,\n")
    sql_file.write("    Movie_ID INT,\n")
    sql_file.write("    Screen_ID INT,\n")
    sql_file.write("    Start_Time TIME,\n")
    sql_file.write("    Available_Seats INT\n")
    sql_file.write(");\n\n")

    sql_file.write("INSERT INTO movie_info (Movie_ID, Movie_Name, Movie_Length, Age_Rating)\n")
    sql_file.write("VALUES (1, 'The Movie', '01:35:00', '12A');\n\n")

    sql_file.write("INSERT INTO screens (Screen_ID, Four_K)\n")
    sql_file.write("VALUES (1, False);\n\n")

    sql_file.write("INSERT INTO showings (Showing_ID, Movie_ID, Screen_ID, Start_Time, Available_Seats)\n")
    sql_file.write("VALUES (1, 1, 1, '12:00:00', 23);\n")
