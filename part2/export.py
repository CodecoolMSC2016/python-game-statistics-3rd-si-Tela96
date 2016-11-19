import reports

# Export functions


def main():
    file_name = 'game_stat.txt'
    title = 'StarCraft'
    genres_dict = reports.count_grouped_by_genre(file_name)
    exportfile = open('answers.txt', 'w')
    exportfile.write(str(reports.get_most_played(file_name)))
    exportfile.write('\n')
    exportfile.write(str(reports.sum_sold(file_name)))
    exportfile.write('\n')
    exportfile.write(str(reports.get_selling_avg(file_name)))
    exportfile.write('\n')
    exportfile.write(str(reports.count_longest_title(file_name)))
    exportfile.write('\n')
    exportfile.write(str(reports.get_date_avg(file_name)))
    exportfile.write('\n')
    exportfile.write(str(reports.get_game(file_name, title)))
    exportfile.write('\n')
    for genre, num in genres_dict.items():
        exportfile.write(str(genre))
        exportfile.write('\t')
        exportfile.write(str(num))
        exportfile.write('\n')
    exportfile.write('\n')

main()
