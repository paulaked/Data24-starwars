from app.create_starships import create_starships
from app.fill_starships import fill_starships
from app.final_printing_bit import print_starships


if __name__ == '__main__':
    pointless_value = create_starships()
    pointless_value_2 = fill_starships()
    print_starships()
