from django.views.generic import TemplateView

#제네릭 뷰 상속받아 이용하기 때문에 template_name 클래스 변수를 오버라이딩 해줘야함.
class HomeView(TemplateView):
    template_name = 'home.html'
