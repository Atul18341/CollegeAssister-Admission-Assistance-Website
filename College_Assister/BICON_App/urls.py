from django.urls import path,include
from BICON_App import views

urlpatterns=[

     path('',views.index,name="index"),
     path('About',views.about,name="about"),
      path('College/<int:pk>/',views.college_detail,name='college'),
     path('CollegeList',views.collegeList,name="collegeList"),
     path('Contact',views.contact,name="contact"),
     path('filters',views.cutoffview,name="filters"),
     path('querypage',views.queryPageview,name="querypage"),
     path('query-form',views.queryForm,name="queryform"),
##### College List Filter Urls
    path('CollegeList/establishment_year',views.establishment_year,name="establishment"),
    path('College/<int:no>/<str:Branch>/',views.cutoffTable,name="cutoffTable")

]