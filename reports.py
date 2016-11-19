import csv

# Report functions


def count_games(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    gamecount = 0
    for row in read_stats:
        gamecount += 1
    return gamecount


def decide(file_name, year):
    year = str(year)
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    for row in read_stats:
        if year in row[2]:
            return True
    return False


def get_latest(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    latest_year = 0
    for row in read_stats:
        if latest_year < int(row[2]):
            latest_year = int(row[2])
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    for row in read_stats:
        if str(latest_year) in row[2]:
            latest_game = row[0]
            return latest_game


def count_by_genre(file_name, genre):

    genre_counter = 0
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    for row in read_stats:
        if genre in row[3]:
            genre_counter += 1
    return(genre_counter)


def get_line_number_by_title(file_name, title):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    line_counter = 0
    for row in read_stats:
        line_counter += 1
        if title in row[0]:
            return line_counter
    return ValueError


def sort_abc(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    ordered_titles = []
    for row in read_stats:
        ordered_titles.append(row[0])
    ordered_titles = sorted(ordered_titles)
    return ordered_titles


def get_genres(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    genres = []
    for row in read_stats:
        if not row[3] in genres:
            genres.append(row[3])
    genres = sorted(genres, key=str.lower)
    return genres


def when_was_top_sold_fps(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    all_fps = []
    top_sell = 0
    for row in read_stats:
        if row[3] == 'First-person shooter':
            all_fps.append(row)
    for game in all_fps:
        if float(game[1]) > top_sell:
            top_sell = float(game[1])
    for game in all_fps:
        if str(top_sell) in game[1]:
            return int(game[2])
    return ValueError
