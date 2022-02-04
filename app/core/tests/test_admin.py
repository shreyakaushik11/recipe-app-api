from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@github.com',
            password='password123'
        )
        """using the Client helper function to log a user with the Django
        authentication, it makes our tests a lot easier to write because
        it means we don't have to manually log the user in"""
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test@github.com',
            password='password123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        """in reverse. first we pass in the app name then after
        colon the URL that you want. The URLs are actually defined
        in the Django admin documentation"""
        url = reverse('admin:core_user_changelist')
        """This will use our test Client to perform a HTTP GET on the
        URL that we have found above"""
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        # /admin/core/user/1
        # it will create url like this, here 1 is the id of the user
        res = self.client.get(url)
        # we're going to test that our page renders ok
        self.assertEqual(res.status_code, 200)
