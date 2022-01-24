import climmob.plugins.utilities as u
from climmob.processes import getActiveProject


class MyPublicView(u.publicView):
    def process_view(self):

        return {}


class MyPrivateView(u.privateView):
    def __init__(self, request):
        u.privateView.__init__(self, request)
        self.checkCrossPost = False

    def processView(self):

        activeProject = getActiveProject(self.user.login, self.request)

        return {
            "activeUser": self.user,
            "activeProject": activeProject,
            "message": "Hello word",
        }
