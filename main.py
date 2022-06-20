from util import *
from TravellingMan import TravellingMan
from Waterstones import Waterstones
from BookDepository import BookDepository

def main():
    book_name = get_book_name()
    matches = []
    tm = TravellingMan()
    ws = Waterstones()
    bd = BookDepository()
    matches.extend(tm.get_matches(book_name))
    matches.extend(ws.get_matches(book_name))
    matches.extend(bd.get_matches(book_name))
    append_to_csv(matches)

if __name__ == "__main__":
    main()

