from django.db import models


# Path Table Sigle

class Teacher(models.Model):
    name = models.CharField(max_length = 150)
    first_name = models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)

    def __str__(self):
        return '%s %s %s' % (self.name, self.first_name, self.last_name)


class Branch(models.Model):
    name = models.CharField(max_length = 150)
    def __str__(self):
        return self.name





# path ForeignKey

class Paper(models.Model):
    title_th = models.CharField(max_length = 255) # หัวข้อวิจัย ภาษาไทย
    title_eg = models.CharField(max_length = 255, null=True, blank=True) # หัวข้อวิจัย ภาษาอังกฤษ 
    researcher = models.CharField(max_length = 150) # ผู้วิจัย
    abstract_thai = models.TextField(blank=True)# บทนำ ภาษาไทย
    abstract_eng = models.TextField(blank=True)# บทนำ ภาษาอังกฤษ
    link_paper = models.URLField(max_length = 200, blank=True)# link paper
    keyword = models.CharField(max_length = 150, blank=True) # คำสำคัญ
    upload_files = models.FileField(upload_to='file', null=True, blank=True) # uppload file paper
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE) # อาจารย์ที่ปรึกษา
    branchs = models.ForeignKey(Branch, on_delete=models.CASCADE) # สาขาวิชา
    date_paper = models.DateField() # วันเดือนปี เอกสาร
    approve = models.BooleanField(default=False) # อนุมัติ Paper

    def __str__(self):
        return self.title_th


    