from series_parser import SeriesMediaParser


def main():
    parser = SeriesMediaParser()
    result = parser.get_rename_path("helloworld")
    print(result)


main()
