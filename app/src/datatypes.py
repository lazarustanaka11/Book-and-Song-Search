from dataclasses import dataclass
from operator import itemgetter


@dataclass
class result:
    items: list
    status: int
    time_lapse: float

    @property
    def sorted_items(self):
        """
        sort the items by title in alphabetical order
        """
        return sorted(self.items, key=itemgetter("title"))


@dataclass
class itunes_results:
    audio: result


@dataclass
class books_results:
    books: result
