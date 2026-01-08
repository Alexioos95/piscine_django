import time
import random
from django.conf import settings

class NamesMiddleware:
	def __init__(self, get_response):
		self.get_response = get_response

	def __call__(self, request):
		# Ignore future exercises
		if request.path.startswith("/ex"):
			return self.get_response(request)
		# Get current data
		now = time.time()
		username = request.session.get("username")
		timestamp = request.session.get("timestamp")
		# If None or outdated, update
		if not username or not timestamp or now - timestamp > 42:
			username = random.choice(settings.NAMES)
			request.session["username"] = username
			request.session["timestamp"] = now
		request.username = request.session["username"]
		# Call view
		return self.get_response(request)
