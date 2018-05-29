from django.db import models


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


from django.db import models

# Create your models here.
from django.utils import timezone


# 文章标签类
class Tag(models.Model):
    t_name = models.CharField(max_length=255)
    t_info = models.CharField(max_length=300)
    t_createtime = models.DateTimeField(default=timezone.now, db_index=True)

    def __unicode__(self):
        return self.t_name


# 文章类
class Art(models.Model):
    a_title = models.CharField(max_length=255)
    a_info = models.CharField(max_length=300)
    a_content = models.TextField()
    a_img = models.ImageField(null=True, blank=True, upload_to="uploads")
    a_addtime = models.DateTimeField(default=timezone.now, db_index=True)
    a_updatetime = models.DateTimeField(default=timezone.now)
    a_tag = models.ForeignKey(Tag)

    def __unicode__(self):
        return self.a_title

    class Meta:
        ordering = ['-a_addtime']
