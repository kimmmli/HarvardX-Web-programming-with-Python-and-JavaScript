from django.urls import path
from . import views

# 在urls.py 我们定义了app_name 之后refer url name都要加: 如：
# <li><a href="{% url 'flights:flight' flight.id %}">Flight {{ flight.id }}</a>: {{ flight.origin }} to {{ flight.destination }}</li>
app_name="user"
urlpatterns=[
    path('', views.index, name="index"),
    path('login',views.login_view,name="login"),
    path('logout',views.logout_view,name="logout")
]