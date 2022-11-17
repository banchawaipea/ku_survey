from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length = 150)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)

    def __str__(self):
        return '%s %s %s' % (self.name, self.first_name, self.last_name)

class Branch(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.name




class Paper(models.Model):
    title = models.CharField(max_length = 255)
    abstract_thai = models.TextField()
    abstract_eng = models.TextField()
    link_paper = models.CharField(max_length = 255)
    keyword = models.CharField(max_length = 150)
    upload_files = models.FileField(upload_to='file', null=True, blank=True)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    branchs = models.ForeignKey(Branch, on_delete=models.CASCADE)
    date_paper = models.DateField()
    approve = models.BooleanField(default=False)

    
    def __str__(self):
        return self.title


    