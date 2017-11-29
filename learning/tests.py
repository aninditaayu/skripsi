import datetime

from django.utils import timezone
from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from .models import Materi, Bab, Soal, Jawaban

class LearningViewTests(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Selamat Datang")
        self.assertQuerysetEqual(response.context['progress'], '')

    def setUp(self):
    	self.user = User.objects.create_user(username='testuser', password='12345')
    	self.user.save()
    	login = self.client.login(username='testuser', password='12345')

    def test_bab_view(self):
    	response = self.client.get(reverse('bab'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BAB YANG DIPELAJARI")
        self.assertQuerysetEqual(response.context['bab'], '')      

    def test_bab_view_2(self):
    	Bab.objects.create(nama='bab 1')
    	response = self.client.get(reverse('bab'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "BAB YANG DIPELAJARI")
        self.assertQuerysetEqual(response.context['bab'], ['<Bab: bab 1>']) 

    def test_materi_view(self):
    	bab=Bab.objects.create(nama='bab 1')
    	Materi.objects.create(bab=bab, judul_materi='Pengenalan Python' )
        response = self.client.get(reverse('materi', kwargs={'bab_slug': 'bab-1'}))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['materi'], ['<Materi: Pengenalan Python-bab 1>'])

    def test_materi_view_404(self):
    	response = self.client.get(reverse('materi', kwargs={'bab_slug': 'bab-300'}))
    	self.assertEqual(response.status_code, 404)

    def test_soal_view(self):
    	bab=Bab.objects.create(nama='bab 1')
    	materi = Materi.objects.create(bab=bab, judul_materi='Print')
    	soal=Soal.objects.create(materi=materi, judul_soal='Soal Print', deskripsi_soal='ini adalah deskripsi soal',
   			instruksi='Print 3+3', kunci_jawaban='6', hint='ini hint')
    	response = self.client.get(reverse('soal', kwargs={'bab_slug': 'bab-1', 'materi_slug': 'print', 'soal_id': soal.id}))
    	self.assertEqual(response.status_code, 200)
    	self.assertEqual(response.context['soal'], soal)

    def test_about_view(self):
    	response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Be-Py")
        
    def test_user_dashboard_view(self):
    	response = self.client.get(reverse('dashboard'))
    	self.assertEqual(response.status_code, 200)
    	self.assertContains(response, "Profil")
        self.assertQuerysetEqual(response.context['progress'], '')