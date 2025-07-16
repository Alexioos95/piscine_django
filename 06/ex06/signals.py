from django.db.models.signals import pre_save, post_save, post_delete
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission
from django.dispatch import receiver
from .models import Vote, Tip
from ex04.models import MyUser

@receiver(pre_save, sender=Vote)
def update_reputation(sender, instance, **kwargs):
	user = instance.tip.author
	if instance.pk:
		prev = Vote.objects.get(pk=instance.pk)
		if prev.type != instance.type:
			if prev.type == "up":
				user.reputation -= 5
			elif prev.type == "down":
				user.reputation += 2
			if instance.type == "up":
				user.reputation += 5
			elif instance.type == "down":
				user.reputation -= 2
	else:
		if instance.type == "up":
			user.reputation += 5
		elif instance.type == "down":
			user.reputation -= 2
	user.save()

@receiver(post_delete, sender=Vote)
def remove_reputation(sender, instance, **kwargs):
	user = instance.tip.author

	if instance.type == "up":
		user.reputation -= 5
	elif instance.type == "down":
		user.reputation += 2
	user.save()

@receiver(post_save, sender=MyUser)
def update_perms(sender, instance, **kwargs):
	content_type = ContentType.objects.get(app_label="ex06", model="tip")
	downvote_perm = Permission.objects.get(codename="downvote_tip", content_type=content_type)
	delete_perm = Permission.objects.get(codename="delete_tip", content_type=content_type)

	if instance.reputation >= 15:
		instance.user_permissions.add(downvote_perm)
	else:
		instance.user_permissions.remove(downvote_perm)
	if instance.reputation >= 30:
		instance.user_permissions.add(delete_perm)
	else:
		instance.user_permissions.remove(delete_perm)
