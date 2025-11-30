from django.test import TestCase, Client
from django.urls import reverse
from accounts.models import User
from products.models import Product
from orders.models import Order, OrderItem


class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com',
            role='farmer'
        )
        self.order = Order.objects.create(
            user=self.user,
            order_number='ORD123456',
            status='pending',
            shipping_address='Test Address',
            shipping_phone='1234567890',
            total_amount=100.00
        )

    def test_can_revert_status_pending(self):
        """Pending orders cannot be reverted (no previous status)."""
        self.order.status = 'pending'
        self.order.save()
        self.assertFalse(self.order.can_revert_status())

    def test_can_revert_status_packed(self):
        """Packed orders can be reverted to pending."""
        self.order.status = 'packed'
        self.order.save()
        self.assertTrue(self.order.can_revert_status())
        self.assertEqual(self.order.get_previous_status(), 'pending')

    def test_can_revert_status_shipped(self):
        """Shipped orders can be reverted to packed."""
        self.order.status = 'shipped'
        self.order.save()
        self.assertTrue(self.order.can_revert_status())
        self.assertEqual(self.order.get_previous_status(), 'packed')

    def test_can_revert_status_delivered(self):
        """Delivered orders can be reverted to shipped."""
        self.order.status = 'delivered'
        self.order.save()
        self.assertTrue(self.order.can_revert_status())
        self.assertEqual(self.order.get_previous_status(), 'shipped')

    def test_can_revert_status_cancelled(self):
        """Cancelled orders cannot be reverted."""
        self.order.status = 'cancelled'
        self.order.save()
        self.assertFalse(self.order.can_revert_status())

    def test_revert_status_success(self):
        """Test reverting status from shipped to packed."""
        self.order.status = 'shipped'
        self.order.save()
        result = self.order.revert_status()
        self.assertTrue(result)
        self.assertEqual(self.order.status, 'packed')

    def test_revert_status_failure(self):
        """Test reverting status when it cannot be reverted."""
        self.order.status = 'pending'
        self.order.save()
        result = self.order.revert_status()
        self.assertFalse(result)
        self.assertEqual(self.order.status, 'pending')


class RevertOrderStatusViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@example.com',
            role='farmer'
        )
        self.admin_user = User.objects.create_user(
            username='adminuser',
            password='adminpass123',
            email='admin@example.com',
            role='admin',
            is_staff=True
        )
        self.order = Order.objects.create(
            user=self.user,
            order_number='ORD123456',
            status='shipped',
            shipping_address='Test Address',
            shipping_phone='1234567890',
            total_amount=100.00
        )

    def test_revert_status_requires_login(self):
        """Anonymous users cannot revert order status."""
        url = reverse('orders:revert_order_status', args=[self.order.pk])
        response = self.client.post(url)
        self.assertEqual(response.status_code, 302)
        self.assertIn('/accounts/login/', response.url)

    def test_revert_status_requires_staff(self):
        """Non-staff users cannot revert order status."""
        self.client.login(username='testuser', password='testpass123')
        url = reverse('orders:revert_order_status', args=[self.order.pk])
        response = self.client.post(url, follow=True)
        self.assertContains(response, 'You do not have permission')
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'shipped')

    def test_revert_status_staff_can_revert(self):
        """Staff users can revert order status."""
        self.client.login(username='adminuser', password='adminpass123')
        url = reverse('orders:revert_order_status', args=[self.order.pk])
        response = self.client.post(url, follow=True)
        self.assertContains(response, 'reverted')
        self.order.refresh_from_db()
        self.assertEqual(self.order.status, 'packed')
