from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
'''
学生信息： 学号int 姓名char 性别char 年龄int 入学年份data 所在专业char 班级char 导员姓名char
考试成绩：考试科目 考试成绩
课程信息：课程名 课程老师 上课教室
'''


# 学生信息
class StdentInformation(models.Model):
    student_id = models.IntegerField(verbose_name='学号')
    student_age = models.IntegerField(verbose_name='年龄')
    student_name = models.CharField(max_length=100, verbose_name='姓名')
    student_sex = models.CharField(max_length=5, verbose_name='性别')
    start_year = models.CharField(max_length=10, verbose_name='入学年份')
    specialty = models.CharField(max_length=20, verbose_name='所在专业')
    student_class = models.CharField(max_length=10, verbose_name='班级')
    teacher_name = models.CharField(max_length=20, verbose_name='导员姓名')

    def __str__(self):
        return self.student_name


# 考试成绩
class StudentScore(models.Model):
    sub_ject = models.CharField(max_length=10, verbose_name='科目')
    score = models.CharField(max_length=10, verbose_name='成绩')


# 课程信息
class StudentCourse(models.Model):
    sub_name = models.CharField(max_length=10, verbose_name='课程名')
    sub_tcacher = models.CharField(max_length=10, verbose_name='课程老师')
    sub_class = models.CharField(max_length=10, verbose_name='上课教师')
