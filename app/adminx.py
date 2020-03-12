import xadmin
from xadmin import views
from .models import Blog
# Register your models here.


class GlobalSettings(object):
    site_title = "别来无恙"
    site_footer = "小脚丫"


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class BlogAdmin:
    list_display = ['title','content']
    list_editable = ['title','content']


xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(Blog,BlogAdmin)