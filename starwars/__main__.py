from app.create_starships import create_starships
from app.fill_starships import fill_starships
from app.final_printing_bit import print_starships


if __name__ == '__main__':
    # The variables are needed because the functions return values
    pointless_value = create_starships()  # This runs the create starships function
    pointless_value_2 = fill_starships()  # This runs the fill starships function. This is the main function because it
    #                                       contains make_starship_dicts too
    print_starships()  # This is there to print out everything to show it's there.
