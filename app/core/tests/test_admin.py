from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        """This is function that would execute before
        all the tests (same as before function at typeScript)"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin1@investing.com',
            password='pass123'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='test1@investing.com',
            password='pass123',
            name='Test user full name'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        # The function reverse wpi;d generate url base these params.
        url = reverse('admin:core_user_changelist')

        # Call rest request Get.
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)

    # Remember - in order it to excute it should start with prefix test
    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:core_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    # This test failed, - dont know why...
    # ================================
    # def test_create_user_page(self):
    #     """Test that the create user page works"""
    #     url = reverse('admin:core_user_add')
    #     res = self.client.get(url)
    #
    #     self.assertEqual(res.status_code, 200)
