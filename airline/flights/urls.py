from django.urls import path
from . import views

# 在urls.py 我们定义了app_name 之后refer url name都要加: 如：
# <li><a href="{% url 'flights:flight' flight.id %}">Flight {{ flight.id }}</a>: {{ flight.origin }} to {{ flight.destination }}</li>
app_name="flights"
urlpatterns=[
    path('', views.index, name="index"),
    path('<int:flight_id>',views.flight,name="flight"),
    path('<int:flight_id>/book',views.book,name="book")
]