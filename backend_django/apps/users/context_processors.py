from .models import User


def test_user_context_processors(request):
    first_user = User.objects.first()
    return {"first_user": first_user}
