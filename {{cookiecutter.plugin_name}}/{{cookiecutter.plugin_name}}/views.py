from climmob.views.classes import privateView, publicView

class MyPublicView(publicView):
    def process_view(self):
        return {"status":200,"message":"ok"}


class MyPrivateView(privateView):
    def process_view(self):

    	return {"status":200,"message":"ok"}
