from django.urls import include, path

from .views import users, professors, administratives, students

urlpatterns = [
    path('', users.home, name='home'),
    path('students/', include(([
        path('', students.HomeView, name='home'),
        path('signup/', students.SignUpView.as_view(), name='signup'),
    ], 'users'), namespace='students')),

    path('professors/', include(([
        path('', professors.HomeView, name='home'),
        path('signup/', professors.SignUpView.as_view(), name='signup'),
    ], 'users'), namespace='professors')),

    path('administratives/', include(([
        path('', administratives.HomeView, name='home'),
        path('add/', administratives.SignUpView.as_view(), name='administratives_add'),
    ], 'users'), namespace='administratives')),
]
