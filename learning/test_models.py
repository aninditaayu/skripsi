from django.test import TestCase

from .models import Bab, Materi, Soal, Jawaban, User


class BabModelTest(TestCase):

    def test_string_representation(self):
        bab = Bab.objects.create(nama='Bab 1')
        self.assertEqual(bab.__unicode__(), 'Bab 1')
        self.assertEqual(bab.__unicode__(), bab.nama)


class MateriModelTest(TestCase):

	def test_string_representation(self):
		bab = Bab.objects.create(nama='Bab 1')
		materi = Materi.objects.create(bab = bab, judul_materi = 'Pengenalan Python')
		self.assertEqual(materi.__unicode__(), 'Pengenalan Python-Bab 1')
		self.assertEqual(materi.__unicode__(), '{}-{}'.format(materi.judul_materi, materi.bab.nama))



class SoalModelTest(TestCase):

 	def test_string_representation(self):
 		bab = Bab.objects.create(nama= 'Bab 2')
 		materi = Materi.objects.create(bab = bab, judul_materi = 'Print')
 		soal = Soal.objects.create(judul_soal = 'Print (1)', materi = materi)
 		self.assertEqual(soal.__unicode__(), 'Print (1)-Print-Bab 2')
 		self.assertEqual(soal.__unicode__(), '{}-{}-{}'.format(soal.judul_soal, soal.materi.judul_materi, soal.materi.bab))


class JawabanModelTest(TestCase):

	def test_string_representation(self):
		bab = Bab.objects.create(nama= 'Bab 2')
 		materi = Materi.objects.create(bab = bab, judul_materi = 'Print')
 		soal = Soal.objects.create(judul_soal = 'Print (1)', materi = materi)
 		user = User.objects.create_user(username='testuser', password='12345')
 		jawaban = Jawaban.objects.create(soal=soal, kali_jawab=1, user=user)
 		self.assertEqual(jawaban.__unicode__(), 'Soal Print (1)-Print-Bab 2 - testuser - 1')

