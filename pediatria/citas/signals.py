from .models import Paciente, Pediatra, Cita
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import ugettext as _
from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Cita)
def on_create_cita(sender, instance, created, **kwargs):
    if created:
        subject = _('Prueba YEMA: correo de notificación de cita.')
        message = _('Tu cita ha sido agendada en la fecha ') + str(instance.fecha) + _(' a las ') + str(instance.hora) + _(' con el Dr. ') + instance.pediatra.nombre + '\n' + instance.comentario
        email_from = settings.EMAIL_HOST_USER
        recipient_list = settings.EMAIL_TO_LIST
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list, fail_silently=False )