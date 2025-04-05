from functions.func import strip_all_markup




class NewsHandler():
    def __init__(self):
        pass


    def getNews(self, newsFeed):
        #{'id': 3147, 'published': 35866486, 'type': 0, 'tagIds': [], 'message': "<i=3>ALERT</i>\n\nThe <i=1>Meridian Singularity</i> has come within critical range of <i=1>Ivis.</i> Final evacuation orders have been issued. The planet's destruction is imminent."}
        message = []
        for i in newsFeed[-10:]:
            message.append(strip_all_markup(i['message']))

        return list(reversed(message))
    