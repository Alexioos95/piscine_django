from .forms import NavLoginForm

def login_form_context(request):
	from django.contrib.auth.forms import AuthenticationForm
	return {
		"login_form": AuthenticationForm(request=request)
	}
