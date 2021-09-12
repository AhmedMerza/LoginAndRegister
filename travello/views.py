from travello.models import Project, User
from django.shortcuts import render

# Create your views here.


def home(request):

    user = User()
    user.user = 'i47med01'
    user.name = 'Ahmed Ali'
    user.email = 'i47med01x@gmail.com'
    user.insta = 'https://www.instagram.com/i47med01x/'
    user.github = 'https://github.com/i47med01'
    # user = User.objects.all()

    # project1 = Project()
    # project1.id = 1
    # project1.p = 'Project one is about making a calculator using java.\nThis calculator is a 3 in 1 calculator, the first one is the standard calculator the second one is the scientific calculator, and the last one is the programming calculator.'

    # project2 = Project()
    # project2.id = 2
    # project2.p = 'Project two is about making a game and it is Hangman using C#.\nThere are three difficulties easy, normal, and hard, the easy gives you 30s to guess the word, the normal givse you 20s, and the hard gives you 10s.'

    # project3 = Project()
    # project3.id = 3
    # project3.p = 'Project one is about making a calculator using java, this calculator is a 3 in 1 calculator, the first one is the standard calculator the second one is the scientific calculator, and the last one is the programming calculator.'

    # projects = [project1, project2, project3]

    projects = Project.objects.all()

    return render(request, 'home.html', {'User': user, 'projects': projects}, )
