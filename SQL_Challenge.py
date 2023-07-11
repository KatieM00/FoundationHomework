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


# Open the SQL file in append mode
with open(file_path, "a") as sql_file:
    sql_statements = """
USE foundation_assessment_ii;

INSERT INTO movie_info(movie_ID, movie_name, movie_length, age_rating)
VALUES 
    (1, 'The Movie', '2:19:00', '12A'),
    (2, 'The Other Movie', '1:30:00', '15'),
    (3, 'The 3D Amazing Movie',  '1:42:00', 'PG'),
    (4, 'La Allure', '1:09:00', '18'),
    (5, 'The Cartoon', '1:15:00', 'U'),
    (6, 'The Scary Cartoon', '1:23:00', 'PG'),
    (7, 'The Coming Of Age', '1:40:00', '12A'),
    (8, 'The War', '2:07:00', '15'),
    (9, 'The Murder Mystery', '1:47:00', '15');

INSERT INTO screens(screen_ID, four_k)
VALUES 
    (1, True),
    (2, False),
    (3, True),
    (4, True),
    (5, True),
    (6, True),
    (7, True),
    (8, False),
    (9, True),
    (10, True);

INSERT INTO showings(showing_ID, movie_ID, screen_ID, start_time, available_seats)
VALUES 
    (1, 1, 2, '12:00:00', 10), 
    (2, 1, 2, '17:00:00', 23), 
    (3, 2, 9, '10:30:00', 30), 
    (4, 3, 1, '07:00:00', 38), 
    (5, 3, 5, '10:00:00', 26), 
    (6, 3, 1, '17:00:00', 5), 
    (7, 3, 1, '19:00:00', 0), 
    (8, 3, 5, '14:00:00', 2), 
    (9, 4, 9, '20:00:00', 14), 
    (10, 4, 9, '23:00:00', 23), 
    (11, 5, 6, '09:30:00', 30), 
    (12, 5, 6, '12:30:00', 7), 
    (13, 5, 6, '14:30:00', 0), 
    (14, 5, 6, '15:20:00', 0), 
    (15, 6, 10, '10:00:00', 32), 
    (16, 6, 10, '13:30:00', 25), 
    (17, 6, 10, '17:00:00', 14), 
    (18, 7, 7, '12:00:00', 36), 
    (19, 8, 4, '15:00:00', 24), 
    
    """
