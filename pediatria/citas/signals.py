from .models import Paciente, Pediatra, Cita
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail
from django.conf import settings

@receiver(post_save, sender=Cita)
def on_create_cita(sender, instance, created, **kwargs):
    if created:
        print('sending mail to santiago.gm1191@gmail.com')
        subject = 'Prueba YEMA: correo de notificación de cita.'
        message = 'Tu cita ha sido agendada en la fecha ' + str(instance.fecha) + ' a las ' + str(instance.hora) + ' con el Dr. ' + instance.pediatra.nombre + '\n' + instance.comentario
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['santiago.gm1191@gmail.com',]
        send_mail(subject=subject, message=message, from_email=email_from, recipient_list=recipient_list, fail_silently=False )