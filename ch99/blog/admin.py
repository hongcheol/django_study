from django.contrib import admin
from blog.models import Post

# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):#admin page에서 보여줄 항목 설정
    list_display = ('id','title','modify_dt') #Post 객체 보여줄 때, () 안의 내용 보여주기
    list_filter = ('modify_dt',) #()안의 컬럼을 사용하는 필터 사이드바를 보여주라는 뜻
    search_fields = ('title','content') # 검색박스를 표시해서 입력된 단어는 title과 content 칼럼에서 검색하라는 의미
    prepoulated_fields = {'slug' : ('title',)} # title 필드를 이용해서 미리 채워지도록한다.


