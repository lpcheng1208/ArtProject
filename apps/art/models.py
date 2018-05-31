from django.db import models
from django.utils import timezone
from DjangoUeditor.models import UEditorField


# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=50)


class Student(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    cls_id = models.ForeignKey(Class)

    def __str__(self):
        return self.name


# 文章标签类
class Tag(models.Model):
    t_name = models.CharField(max_length=255, verbose_name="标签名")
    t_info = models.CharField(max_length=300, verbose_name="标签描述")
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")

    def __str__(self):
        return self.t_name

    class Meta:
        ordering = ['t_createtime']
        db_table = "t_tag"
        # verbose_name = "标签"
        verbose_name_plural = "标签"


# 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255, verbose_name="标题")
    a_info = models.CharField(max_length=300, verbose_name="简介")
    a_content = UEditorField(verbose_name="文章内容", width=1000, height=600,
                             imagePath="arts_ups/ueditor/", filePath="arts_ups/ueditor/",
                             blank=True, toolbars="full", default='')
    a_img = models.ImageField(null=True, blank=True, upload_to="arts_ups/%Y-%m-%d/")
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True, verbose_name="创建时间")
    a_updatetime = models.DateTimeField(default=timezone.now, verbose_name="更改时间")
    a_tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.a_title

    class Meta:
        db_table = "t_art"
        ordering = ['a_addtime']
        # verbose_name = "文章"
        verbose_name_plural = "文章"
