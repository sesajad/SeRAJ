from django.urls import include, path

from .views import users, professors, administratives

urlpatterns = [
    path('', users.home, name='home'),

    path('professors/', include(([
        path('', professors.HomeView, name='professors_home'),
        path('add/', professors.ProfessorsSignUpView.as_view(), name='professors_add'),
    ], 'users'), namespace='professors')),

    path('administratives/', include(([
        path('', administratives.HomeView, name='administratives_home'),
        path('add/', administratives.AdministrativesSignUpView.as_view(), name='administratives_add'),
    ], 'users'), namespace='administratives')),
]
