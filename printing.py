
# Printing functions
import reports


def main():

    filename = 'game_stat.txt'

    print(reports.count_games(filename))
    print(reports.decide(filename, 2003))
    print(reports.count_by_genre(filename, 'RPG'))
    print(reports.get_latest(filename))
    print(reports.get_line_number_by_title(filename, 'StarCraft'))
    print(reports.sort_abc(filename))
    print(reports.get_genres(filename))
    print(reports.when_was_top_sold_fps(filename))


main()
