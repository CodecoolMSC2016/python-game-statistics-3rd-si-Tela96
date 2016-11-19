import csv
import math

# Report functions


def get_most_played(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    most_played_num = 0
    most_played = ""
    for row in read_stats:
        float(row[1])
        if float(row[1]) > most_played_num:
            most_played_num = float(row[1])
            most_played = row[0]
    return(most_played)


def sum_sold(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    sold_sum = 0
    sold_sum = float(sold_sum)
    for row in read_stats:
        sold_sum += float(row[1])
    return sold_sum


def get_selling_avg(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    selling = []
    for row in read_stats:
        row[1] = float(row[1])
        selling.append(row[1])
    selling_sum = sum(selling)
    all_selling = len(selling)
    avg_selling = selling_sum / all_selling
    return avg_selling


def count_longest_title(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    titles = []
    for row in read_stats:
        titles.append(row[0])
    max_length = max(titles, key=len)
    return len(max_length)


def get_date_avg(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    rls_list = []
    for row in read_stats:
        rls_list.append(int(row[2]))
    rls_sum = sum(rls_list)
    num_titles = len(rls_list)
    avg_date = rls_sum / num_titles
    avg_date = math.ceil(avg_date)
    return avg_date


def get_game(file_name, title):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    game = []
    for row in read_stats:
        if title == row[0]:
            row[1] = float(row[1])
            row[2] = int(row[2])
            return row


def count_grouped_by_genre(file_name):
    stats = open(file_name, 'r')
    read_stats = csv.reader(stats, delimiter='\t')
    genre_dict = {}
    for row in read_stats:
        if row[3] not in genre_dict:
            genre_dict.update({row[3]: 1})
        elif row[3] in genre_dict:
            genre_dict[row[3]] += 1
    return genre_dict
