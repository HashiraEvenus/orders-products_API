import unittest
import json
import api

class APITestCase(unittest.TestCase):

    def setUp(self):
        self.app = api.app.test_client()

    def test_get_products(self):
        response = self.app.get('/products')
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.get_data(as_text=True))
        self.assertIsInstance(data, list)

    def test_add_product(self):
        product = {
            'name': 'New Product',
            'description': 'New Product Description',
            'price': 19.99
        }
        response = self.app.post('/products', json=product)
        self.assertEqual(response.status_code, 201)
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(data['name'], product['name'])
        self.assertEqual(data['description'], product['description'])
        self.assertEqual(data['price'], product['price'])


if __name__ == '__main__':
    unittest.main()
