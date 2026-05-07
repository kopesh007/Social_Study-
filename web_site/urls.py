from django.urls import path
from . import views


app_name='web_site'

urlpatterns=[
    path("",views.index,name="home"),
    path("important_QA/",views.pdf,name="pdf"),
    path("model_QA/",views.model_Q,name="model_QA")

]