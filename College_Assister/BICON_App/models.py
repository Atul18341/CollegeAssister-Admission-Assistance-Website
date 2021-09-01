from django.db import models
from .validators import validate_file_size
# Create your models here.
class colleges(models.Model):
    college_logo = models.ImageField(upload_to="logo", verbose_name="", validators=[validate_file_size])
    college_name = models.TextField()
    address = models.TextField()
    building_image = models.ImageField(upload_to="building", verbose_name="", validators=[validate_file_size])
    establishment_year = models.IntegerField()
    campus_area = models.IntegerField(default=0)
    branches = models.TextField(default="Not Available")

    def __str__(self):
        return self.college_name
class Years(models.Model):
    Year_id = models.IntegerField(primary_key=True)
    Year = models.IntegerField(default=0)

class Rounds(models.Model):
    Round_id = models.IntegerField(primary_key=True)
    Round = models.CharField(max_length=10,default="")


class Categories(models.Model):
    Category_id = models.IntegerField(primary_key=True)
    Category = models.CharField(max_length=10, default="-")

class cutoff(models.Model):
    college= models.ForeignKey(colleges, on_delete=models.CASCADE)
    Year = models.ForeignKey(Years, on_delete=models.CASCADE,default=0)
    Round = models.ForeignKey(Rounds, on_delete=models.CASCADE,default=0)
    Category = models.ForeignKey(Categories, on_delete=models.CASCADE,default=0)
    CSE1 = models.CharField(max_length=15, default="-")
    CSE2 = models.CharField(max_length=15, default="-")
    CSE3 = models.CharField(max_length=15, default="-")
    CSE4 = models.CharField(max_length=15, default="-")
    EEE1 = models.CharField(max_length=15, default="-")
    EEE2 = models.CharField(max_length=15, default="-")
    EEE3 = models.CharField(max_length=15, default="-")
    EEE4 = models.CharField(max_length=15, default="-")
    ECE1 = models.CharField(max_length=15, default="-")
    ECE2 = models.CharField(max_length=15, default="-")
    ECE3 = models.CharField(max_length=15, default="-")
    ECE4 = models.CharField(max_length=15, default="-")
    EE1 = models.CharField(max_length=15, default="-")
    EE2 = models.CharField(max_length=15, default="-")
    EE3 = models.CharField(max_length=15, default="-")
    EE4 = models.CharField(max_length=15, default="-")
    ME1 = models.CharField(max_length=15, default="-")
    ME2 = models.CharField(max_length=15, default="-")
    ME3 = models.CharField(max_length=15, default="-")
    ME4 = models.CharField(max_length=15, default="-")
    CE1 = models.CharField(max_length=15, default="-")
    CE2 = models.CharField(max_length=15, default="-")
    CE3 = models.CharField(max_length=15, default="-")
    CE4 = models.CharField(max_length=15, default="-")

    class Meta:
        db_table = "BICON_App_cutoff"


class branches(models.Model):
    college_id = models.ForeignKey(colleges, on_delete=models.CASCADE, related_name="collegeId",
                                   related_query_name="collegeId")
    branch = models.CharField(max_length=5)

class data_contributors(models.Model):
    profile_pic=models.ImageField(upload_to="data_contributors", verbose_name="", validators=[validate_file_size])
    name=models.CharField(max_length=30)
    branch=models.CharField(max_length=5)
    year=models.IntegerField(default=0)
    college=models.CharField(max_length=30)

class user(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=30)

class discussion(models.Model):
    query=models.TextField()
    response=models.CharField(max_length=500,default="")