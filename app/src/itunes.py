import init_request
from datatypes import result, itunes_results


class Itunes(object):
    def __init__(self):
        super().__init__()
        self.initiate_calls = init_request.initiate_calls()
        # ttt

    def song_search(self, term):
        self.term = term
        self.song_base_url = "https://itunes.apple.com/search?"
        self.song_payload = {"term": self.term, "limit": 5}
        items = []  # empty list to which the results will be appended
        # time the function call below
        results, song_result_status, song_time_lapse = self.initiate_calls.init_request(
            self.song_base_url, self.song_payload
        )
        # filter the desired result from the itunes API call result
        if song_result_status == 200:
            if "resultCount" in results and results["resultCount"] > 0:
                results = results["results"]
            else:
                results = []
        else:
            # incase of failure, just return an empty list
            results = []
        """
            - If there is something in results list, look for kind and artist and add to list.
            - If there is nothing, use the defualt,empty items list initialized above
        """
        if len(results) > 0:

            for each_item in results:
                title = None
                each_item_kind = (
                    each_item["kind"]
                    if "kind" in each_item
                    else each_item["wrapperType"]
                )
                artist = each_item["artistName"]
                if "trackName" in each_item:
                    title = each_item["trackName"]
                else:
                    # IF THERE IS NO TITLE, APPEND A * AND EXPLAIN IN DOCUMENTATION
                    title = "*"
                    title += each_item["collectionName"]
                items.append({"type": each_item_kind, "artist": artist, "title": title})
        # return the results list, status code of call and the time lapse
        return itunes_results(result(items, song_result_status, song_time_lapse))
