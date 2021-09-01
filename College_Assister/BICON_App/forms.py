from django import forms
from .models import cutoff
Branches = (
    ("Select Branch","Select Branch"),
    ("CSE","Computer Science"),("EEE","Electrical & Electronics"),
    ("ECE","Electronics & Communication"),("EE","Electrical"),
     ("ME","Mechanical"),("CE","Civil"))
Category = (("#","Select your Category"),("UR","UR"),("ST","ST"),("SC","SC"),("BC","BC"),("EWS","EWS"))
Round = (("#","Select Round"),("1","Round 1"),("2","Round 2"),("3","Round 3"))

class CutoffForm(forms.Form):
    branch = forms.ChoiceField(choices=Branches,label="")
    category = forms.ChoiceField(choices=Category,label="")
    round = forms.ChoiceField(choices=Round,label="")
