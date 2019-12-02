#used to test the static version of the pages
from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse
from .import views

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


#testing the database aspects of the code for each administrator role
from django.test import TestCase
from .models import Link

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


#testing custom models and views
from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from .models import Link

class LinkTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email= 'testemail@test.com',
            password= 'secret'
        )

        self.link = Link.objects.create(
        role = "ADMIN",
        label= 'Label Management',
        url = 'https://engineeringmanagement.com',
        )

    def test_role_label(self):
        link = Link.objects.get(id=1)
        field_label = link._meta.get_field('role').verbose_name
        self.assertEquals(field_label,'role')

    def test_url_label(self):
        link = Link.objects.get(id=1)
        field_label = link._meta.get_field('url').verbose_name
        self.assertEquals(field_label,'url')

    def test_role_max_length(self):
        link = Link.objects.get(id=1)
        max_length = link._meta.get_field('role').max_length
        self.assertEquals(max_length,15)

    def test_url_max_length(self):
        link = Link.objects.get(id=1)
        max_length = link._meta.get_field('url').max_length
        self.assertEquals(max_length,200)

    def test_objectname_is_role_and_label(self):
        link = Link.objects.get(id=1)
        expected_object_name = "(" + self.link.role +")" + " -- " + self.link.label
        self.assertEquals(expected_object_name, str(self.link))


    #testing that the contents of the link is stored correctly
    def test_link_content(self):
        self.assertEqual(f'{self.link.role}', 'ADMIN')
        self.assertEqual(f'{self.link.label}', 'Label Management')


    #confirms homepage uses correct template, and returns correct status code
    def test_link_list_view(self):
        response = self.client.get(reverse('blog-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/home.html')

    #test details of page works along with an incorrect error messages when page does not work
    def test_link_detal_view(self):
        response = self.client.get('')
        no_response= self.client.get('/100000/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)


#testing home, signup, login, login (testing pages and views)
class singupPageTests(TestCase):
    username= 'newuser'
    email= 'eng1@company.com'

    def test_signup_page_status_code(self): #err
        response = self.client.get('/accounts/signup/')
        self.assertEqual(response.status_code, 200)

    def test_login_view_by_name(self):
        response = self.client.get(reverse('account_login'))
        self.assertEqual(response.status_code, 200)

    def test_logout_view_by_name(self): #err
        response = self.client.get(reverse('account_logout'))
        self.assertEqual(response.status_code, 302)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template_test_1(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'account/signup.html')

    def test_view_uses_correct_template_test_2(self):
        response = self.client.get(reverse('account_signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')

    def test_signup_form(self):
        new_user = get_user_model().objects.create_user(
            self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(),1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
