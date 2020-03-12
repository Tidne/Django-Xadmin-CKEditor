from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=45, verbose_name='标题')
    # content = RichTextField(verbose_name="内容")
    content = RichTextUploadingField(verbose_name="内容")
    # content2 = RichTextUploadingField(verbose_name="对比")

    class Meta():
        db_table = 'blog'
        verbose_name = '博客'
        verbose_name_plural = verbose_name

