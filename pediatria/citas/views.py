from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cita, Pediatra, Paciente

class citas(APIView):
    def post(self, request):
        try:
            fecha = request.data['fecha']
            hora = request.data['hora']
            comentario = request.data['comentario']
            pediatra_nom = request.data['pediatra_nombre']
            pediatra_apa = request.data['pediatra_apellido_paterno']
            paciente_nom = request.data['paciente_nombre']
            paciente_apa = request.data['paciente_apellido_paterno']
            
            paciente = Paciente.objects.get(nombre=paciente_nom, apellido_paterno=paciente_apa)
            pediatra = Pediatra.objects.get(nombre=pediatra_nom, apellido_paterno=pediatra_apa)

            cita = Cita()
            cita.fecha = fecha
            cita.hora = hora
            cita.comentario = comentario
            cita.paciente = paciente
            cita.pediatra = pediatra

            cita.save()

            return Response({
                'message': 'cita creada',
                'id_cita': cita.id
            }, status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'status':'internal error',
                'message':str(e)
            }, status.HTTP_500_INTERNAL_SERVER_ERROR)
