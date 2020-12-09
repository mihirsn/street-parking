from django.test import TestCase


class CreateNewUserTest(TestCase):
    """ Test module for inserting a new User """

    def setUp(self):
        self.valid_payload = {'name': 'Bob', 'phone_number': '1234567890'}
        self.invalid_payload = {
            'name': 'Alice',
        }

    def test_create_valid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.valid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_user(self):
        response = client.post(
            reverse('get_post_users'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
