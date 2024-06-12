from django.contrib.auth.models import User

def project_contex(request):
    contex = {
        'me': User.objects.first(),
    }
    return contex