import google_books
import itunes


class perfom_search:
    """
    - class to perfom the search by calling the methods on the parent class on which this child
        class is baed on, the initiate_calls class
    """

    def __init__(self):
        super().__init__()
        self.google_books = google_books.Google()
        self.itunes = itunes.Itunes()

    def search(self, query):
        """
        - method to perfom the search and return the result in alphabetical order
        """
        self.query = query
        google_books = self.google_books.book_search(self.query)
        itunes = self.itunes.song_search(self.query)
        result = {
            "individual_results": {
                "Book_search_results ": google_books.books.sorted_items,
                "Song_search_results": itunes.audio.sorted_items,
            },
        }
        
        return result
