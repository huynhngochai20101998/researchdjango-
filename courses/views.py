from django.http import HttpResponse
from django.views import View


class WelcomeView(View):
    @staticmethod
    def get(request):
        return HttpResponse('Hello')
