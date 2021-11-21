from django.contrib.auth.models import User

def run():
    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    user.save()

