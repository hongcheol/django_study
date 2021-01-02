from django.db import models
from django.urls import reverse_lazy #make url pattern
from taggit.managers import TaggableManager

# Create your models here.

class Post(models.Model):
    title = models.CharField(verbose_name = 'TITLE', max_length = 50)
    slug = models.SlugField('SLUG',unique=True,allow_unicode=True,help_text = 'one word for title alias.')#별칭
    description = models.CharField('DESCRIPTION',max_length = 100,blank=True,help_text='simple discription text')
    content = models.TextField('CONTENT')
    create_dt = models.DateTimeField('CREATE DATE',auto_now_add = True)
    modify_dt = models.DateTimeField('MODIFY DATE',auto_now=True)
    tags = TaggableManager(blank = True)

    class Meta: # 필드 속성외에 필요한 파라미터 있으면 여기에 선언하기
        verbose_name = 'post'#table name
        verbose_name_plural = 'posts'#table 복수 별칭
        db_table = 'blog_posts'
        ordering = ('-modify_dt',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('blog:post_detail',args=(self.slug,))

    def get_previous(self):
        return self.get_previous_by_modify_dt()

    def get_next(self):
        return self.get_next_by_modify_dt()

