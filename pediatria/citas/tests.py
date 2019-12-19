from django.test import TestCase
from .models import Pediatra, Paciente

class PediatraTestCase(TestCase):

    def setUp(self):
        self.ped1 = Pediatra.objects.create(nombre='Jorge', 
        apellido_paterno='Clooney', 
        apellido_materno='Perez')

        self.ped2 = Pediatra.objects.create(nombre='Scarlette', 
        apellido_paterno='Herrera', 
        apellido_materno='Gomez')

    def test_pediatra_creado(self):
        ped3 = Pediatra.objects.create(nombre='Francis', 
        apellido_paterno='Montoya', 
        apellido_materno='Farías')
        
        tst_pediatra = Pediatra.objects.get(pk=ped3.id)

        self.assertIsInstance(tst_pediatra, Pediatra)
        self.assertEqual(tst_pediatra.nombre, 'Francis')
        self.assertEqual(tst_pediatra.apellido_paterno, 'Montoya')

    def test_get_lista_pediatras(self):
        tst_pediatras = Pediatra.objects.filter(id__in =[self.ped1.id, self.ped2.id]  )
        nombres = [ped.nombre for ped in tst_pediatras]
        
        self.assertEqual(tst_pediatras.count(), 2)
        self.assertIn('Jorge', nombres)
        self.assertIn('Scarlette', nombres)

    def test_get_pediatra_by_id(self):
        tst_ped1 = Pediatra.objects.get(pk=self.ped1.id)
        tst_ped2 = Pediatra.objects.get(pk=self.ped2.id)

        self.assertIsInstance(tst_ped1, Pediatra)
        self.assertIsInstance(tst_ped2, Pediatra)
        self.assertEqual(tst_ped1.id, self.ped1.id)
        self.assertEqual(tst_ped2.id, self.ped2.id)

    def test_delete_pediatra(self):
        Pediatra.objects.get(pk = self.ped1.id).delete()
        qs_ped = Pediatra.objects.filter(id=self.ped1.id)

        self.assertEqual(qs_ped.count(), 0)

    def test_update_pediatra(self):
        Pediatra.objects.filter(pk = self.ped1.id).update(nombre='Juan')
        tst_pediatra = Pediatra.objects.get(pk = self.ped1.id)

        self.assertIsInstance(tst_pediatra, Pediatra)
        self.assertEqual(tst_pediatra.nombre, 'Juan')
  
class PacienteTestCase(TestCase):
    def setUp(self):
        self.pac1 = Paciente.objects.create(nombre='Manuel', 
        apellido_paterno='Pinkman', 
        apellido_materno='Rosas',
        fecha_nacimiento='2010-12-11')

        self.pac2 = Paciente.objects.create(nombre='Sofía', 
        apellido_paterno='White', 
        apellido_materno='Blanco',
        fecha_nacimiento='2011-09-01')

    def test_paciente_creado(self):
        pac3 = Paciente.objects.create(nombre='Marshal', 
        apellido_paterno='Stinson', 
        apellido_materno='Mosby',
        fecha_nacimiento='2014-03-14')
        
        tst_paciente = Paciente.objects.get(pk=pac3.id)

        self.assertIsInstance(tst_paciente, Paciente)
        self.assertEqual(tst_paciente.nombre, 'Marshal')
        self.assertEqual(tst_paciente.apellido_paterno, 'Stinson')

    def test_get_lista_pacientes(self):
        tst_pacientes = Paciente.objects.filter(id__in =[self.pac1.id, self.pac2.id]  )
        nombres = [pac.nombre for pac in tst_pacientes]
        
        self.assertEqual(tst_pacientes.count(), 2)
        self.assertIn('Manuel', nombres)
        self.assertIn('Sofía', nombres)

    def test_get_paciente_by_id(self):
        tst_pac1 = Paciente.objects.get(pk=self.pac1.id)
        tst_pac2 = Paciente.objects.get(pk=self.pac2.id)

        self.assertIsInstance(tst_pac1, Paciente)
        self.assertIsInstance(tst_pac2, Paciente)
        self.assertEqual(tst_pac1.id, self.pac1.id)
        self.assertEqual(tst_pac2.id, self.pac2.id)

    def test_delete_paciente(self):
        Paciente.objects.get(pk = self.pac1.id).delete()
        qs_pac = Paciente.objects.filter(id=self.pac1.id)

        self.assertEqual(qs_pac.count(), 0)

    def test_update_paciente(self):
        Paciente.objects.filter(pk = self.pac1.id).update(nombre='Ernesto')
        tst_paciente = Paciente.objects.get(pk = self.pac1.id)

        self.assertIsInstance(tst_paciente, Paciente)
        self.assertEqual(tst_paciente.nombre, 'Ernesto')