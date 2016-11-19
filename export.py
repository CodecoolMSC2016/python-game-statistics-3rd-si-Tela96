
# Export functions
import reports


def main():
    filename = 'game_stat.txt'
    genres = []
    ordered_titles = []
    ordered_titles = reports.sort_abc(filename)
    genres = reports.get_genres(filename)

    exportfile = open('answers.txt', 'w')
    exportfile.write(str('How many games are in the file?'))
    exportfile.write('\n')
    exportfile.write(str(reports.count_games(filename)))
    exportfile.write('\n')
    exportfile.write(str('Is there a game from 2000?'))
    exportfile.write('\n')
    exportfile.write(str(reports.decide(filename, 2000)))
    exportfile.write('\n')
    exportfile.write(str('Which was the latest game?'))
    exportfile.write('\n')
    exportfile.write(str(reports.get_latest(filename)))
    exportfile.write('\n')
    exportfile.write(str('How many games do we have by the RPG genre?'))
    exportfile.write('\n')
    exportfile.write(str(reports.count_by_genre(filename, 'RPG')))
    exportfile.write('\n')
    exportfile.write(str('What is the line number of StarCraft?'))
    exportfile.write('\n')
    exportfile.write(
        str(reports.get_line_number_by_title(filename, 'StarCraft')))
    exportfile.write('\n')
    exportfile.write('\n')
    exportfile.write(
        str('What is the alphabetical ordered list of the titles?'))
    exportfile.write('\n')
    exportfile.write('\n')
    for game in ordered_titles:
        exportfile.write(game)
        exportfile.write('\n')
    exportfile.write('\n')
    exportfile.write(str('What are the genres?'))
    exportfile.write('\n')
    exportfile.write('\n')
    for genre in genres:
        exportfile.write(genre)
        exportfile.write('\n')
    exportfile.write('\n')
    exportfile.write(
        str('What is the release date of the top sold "First-person shooter" game?'))
    exportfile.write('\n')
    exportfile.write(str(reports.when_was_top_sold_fps(filename)))


main()
