'Imported'
from django.shortcuts import render


def userprofile(request):
    """ A view to return the userprofile page """

    return render(request, 'userprofile/userprofile.html')
