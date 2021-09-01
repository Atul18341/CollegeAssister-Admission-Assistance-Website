from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, get_object_or_404,HttpResponseRedirect
from .models import colleges, Years, Rounds, Categories, branches, cutoff, data_contributors,discussion
from .forms import CutoffForm


# Create your views here.
def index(request):
    Data_contributors=data_contributors.objects.all();
    print(Data_contributors)
    return render(request, "index.html",{'data_contributors':Data_contributors})


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def collegeList(request):

    college = colleges.objects.values("id","college_name")
    return render(request, "collegeList.html", {'college': college,'form': CutoffForm()})

def college_detail(request, pk):
    college = get_object_or_404(colleges, pk=pk)
    Branches = branches.objects.filter(college_id=pk);

    return render(request, "colleges.html",
                  {"college": college,"branches": Branches})


##### College List Filters
def establishment_year(request):
    college = colleges.objects.filter().order_by("establishment_year")
    return render(request, "collegeList.html", {"college": college})


def cutoffTable(request, no, Branch):

    years = Years.objects.filter().order_by("-Year_id")
    round=Rounds.objects.all()
    cutoffs = cutoff.objects.values("Round_id__Round","Category_id__Category", Branch + '1', Branch + '2', Branch + '3', Branch + '4').filter(
        college_id=no)
    sql=cutoff.objects.values("college_id__college_name").filter(CE1__lte=2000).filter(Year_id__Year=2020).filter(Round_id__Round=2)
    print(sql)
    return render(request, "CutoffTable.html",
                  {"cutoffs": cutoffs, "branch": Branch, "years": years,"Rounds":round})



def cutoffview(request):
    if request.method == "POST":
        rform = CutoffForm(request.POST)
        if rform.is_valid():
            branch = rform.cleaned_data['branch']
            category = rform.cleaned_data['category']
            round = rform.cleaned_data['round']
            print(branch,category,round)
            val = branch
            cutoffs = cutoff.objects.values("college_id__college_name",branch + '1', branch + '2', branch + '3', branch + '4').filter(Category_id__Category=category).filter(Round_id=round)
            print(cutoffs)
            return render(request,"filters.html",{"category":category,"cutoffs":cutoffs,"branch":branch})

def queryPageview(request):
    Query=discussion.objects.all()
    return render(request,"querypage.html",{'queries':Query})