import init_request
import time

class Google(object):
    def __init__(self):
        self.init_calls = init_request.initiate_calls()

    def book_search(self,query):
        self.query = query
        self.book_base_url = "https://www.googleapis.com/books/v1/volumes?"
        self.book_payload = {"filter":"full","maxResults":"5","q":self.query}
        
        items = [] #empty list to which the results will be appended
        results , book_result_status,book_time_lapse = self.init_calls.init_request(self.book_base_url,
                                                                                   self.book_payload)
        #filter the desired items from the books API call results
        if book_result_status == 200:
            if "items" in results and len(results["items"]) > 0:
                results = results["items"]
            else:
                results = []
        else :
            #incase of failure, just return an empty list
            results = []
        """
            - If there is something in results list, look for kind and author and add to list.
            - If there is nothing, use the defualt,empty items list initialized above
        """
        if len(results) > 0:
            for x in range(len(results)):
                with open("examine.json","w") as js:
                    js.write(str(results))
                each_item = results[x]
                each_item_kind = each_item["kind"]
                volume_info = each_item["volumeInfo"]
                #some books have either no title or no author, therefore ...
                author = volume_info["authors"] if "authors" in volume_info.keys() else [] #if no author return empty list
                title = volume_info["title"] if "title" in volume_info.keys() else [] #no title return empty list
                items.append({"type" : each_item_kind, "author": author, "title" : title})
        #return the results list, status code of call and the time lapse 
        return items, book_result_status, book_time_lapse


