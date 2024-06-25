from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest


class CategoryOfExpertsMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/register/" and request.method == "POST":
            age = int(request.POST.get("age"))
            if age < 5:
                return HttpResponseBadRequest(
                    "Для присвоения экспертной категории необходим стаж более 5 лет"
                )
            elif age >= 5 and age <= 10:
                request.club = "Ваша экспертная категория - Первая категория"
            elif age >= 11 and age <= 15:
                request.club = "Ваша экспертная категория - Вторая категория"
            elif age >= 16 and age <= 25:
                request.club = "Ваша экспертная категория - Высшая категория"
            else:
                return HttpResponseBadRequest("Вам необходимо пройти сертификацию")
        elif request.path == "/register/" and request.method == "GET":
            setattr(request, "club", "Категория не определена")
