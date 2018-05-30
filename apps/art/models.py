from django.db import models
from django.utils import timezone


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
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True)

    def __str__(self):
        return self.t_name

    class Meta:
        db_table = "t_tag"
        verbose_name = "tag"


# 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255, verbose_name="标题")
    a_info = models.CharField(max_length=300, verbose_name="简介")
    a_content = models.TextField(verbose_name="内容")
    a_img = models.ImageField(null=True, blank=True, upload_to="uploads")
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True)
    a_updatetime = models.DateTimeField(default=timezone.now)
    a_tag = models.ForeignKey(Tag)

    def __str__(self):
        return self.a_title

    class Meta:
        db_table = "t_art"
        ordering = ['-a_addtime']
