#used to test the static version of the pages
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .import views

#used to test the database elements of the pages
from django.test import TestCase
from .models import Link


#used to test the creating of the home pages
class HomePageTests(SimpleTestCase):

    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code,200)

    def test_about_page_status_code(self):
        response= self.client.get('/about/')
        self.assertEquals(response.status_code,200)

    def test_views_url_by_name(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code,200)

    def test_view_uses_corrrect_template(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response, 'blog/home.html')

    #def test_home_page_contains_correct_html(self):
    #    response = self.client.get(reverse('blog-home'))
    #    self.assertContains(response.content.decode(), '<h2>')

#testing the database aspects of the code for each administrator role
class AdminLinkModelTest(TestCase):
    def setUp(self):
        Link.objects.create(role = "ADMIN")

    def test_text_content(self):
        link = Link.objects.get(id=1)
        expected_object_name= f'{link.role}'
        self.assertEquals(expected_object_name, "ADMIN")

class FinanceAdminLinkModelTest(TestCase):
    def setUp(self):
        Link.objects.create(role = "FINANCE_ADMIN")

    def test_text_content(self):
        link = Link.objects.get(id=1)
        expected_object_name= f'{link.role}'
        self.assertEquals(expected_object_name, "FINANCE_ADMIN")

class HRAdminLinkModelTest(TestCase):
    def setUp(self):
        Link.objects.create(role = "HR_ADMIN")

    def test_text_content(self):
        link = Link.objects.get(id=1)
        expected_object_name= f'{link.role}'
        self.assertEquals(expected_object_name, "HR_ADMIN")

class SALESAdminLinkModelTest(TestCase):
    def setUp(self):
        Link.objects.create(role = "SALES_ADMIN")

    def test_text_content(self):
        link = Link.objects.get(id=1)
        expected_object_name= f'{link.role}'
        self.assertEquals(expected_object_name, "SALES_ADMIN")

class ENGGAdminLinkModelTest(TestCase):
    def setUp(self):
        Link.objects.create(role = "ENGG_ADMIN")

    def test_text_content(self):
        link = Link.objects.get(id=1)
        expected_object_name= f'{link.role}'
        self.assertEquals(expected_object_name, "ENGG_ADMIN")


class HomePageViewTest(TestCase):
    def setUp(self):
        Link.objects.create(role= "this is another role")

    def test_view_url_exist_at_proper_location(self):
        resp= self.client.get('/')
        self.assertEquals(resp.status_code,200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('blog-home'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'blog/home.html')
