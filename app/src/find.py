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
        self.query = query
        x, x_status, x_time_lapse = self.google_books.book_search(self.query)
        y, y_status, y_time_lapse = self.itunes.song_search(self.query)
        items = x + y
        # record some search metrics, response time and status code
        result = {
            "items": [],
            "Status": {
                "Book_search ": {
                    "status_code": x_status,
                    "response_time": x_time_lapse,
                },
                "Song_search": {"status_code": y_status, "response_time": y_time_lapse},
            },
        }

        # sort the search results alphabetically by title
        result["items"] = sorted(items, key=lambda x: x["title"])

        return result
