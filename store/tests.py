from django.test import TestCase
from django.urls import reverse

from .models import Album, Booking, Contact, Artist
# Create your tests here.


class IndexPageTestCase(TestCase):

    def test_index_page(self):
        response = self.client.get(reverse('index', ))
        self.assertEqual(response.status_code, 200)
        

class DetailPageTestCase(TestCase):
    
    def setUp(self):
        impossible = Album.objects.create(title="Transmission impossible")
        self.album = Album.objects.get(title="Transmission impossible")
    
    
    def test_detail_page_return_200(self):
        album_id = self.album.id
        
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 200)
        
    def test_detail_page_return_404(self):
        album_id = self.album.id + 1
        
        response = self.client.get(reverse('store:detail', args=(album_id,)))
        self.assertEqual(response.status_code, 404)
        
        
class BookingTestCase(TestCase):
    
    def setUp(self):
        Contact.objects.create(name="Freddie", email="freddy@queen.forever")
        impossible = Album.objects.create(title="Transmission impossible")
        journey = Artist.objects.create(name="Journey")
        impossible.artists.add(journey)
        
        self.contact = Contact.objects.get(name="Freddie")
        self.album = Album.objects.get(title="Transmission impossible")
        
    def test_new_booking_is_registered(self):
        old_bookings = Booking.objects.count()
        album_id = self.album.id
        name = self.contact.name
        email = self.contact.email
        
        response = self.client.post(reverse('store:detail', 
                                           args=(album_id,)),
                                           {'name':name, 'email':email})
        new_bookings = Booking.objects.count()
        self.assertEqual(new_bookings, old_bookings+1)