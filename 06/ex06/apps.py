from django.apps import AppConfig


class Ex06Config(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'ex06'
		
	def ready(self):
		import ex06.signals
