# from task.models import Border
# from django.urls import reverse
# from rest_framework import status
# from rest_framework.test import APITestCase
#
#
# class BorderAPIViewTest(APITestCase):
#     def setUp(self) -> None:
#         self.border = Border(name='name')
#         self.border.save()
#         self.url = reverse('api-border', kwargs={'version': 'v1', 'pk': self.post.pk})
#
#     def get_border(self):
#         response = self.client.get(self.url)
#         self.assertEquals(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#         data = response.json()
#         self.assertEquals(
#             data['pk'],
#             str(self.post.pk)
#         )
#         self.assertEquals(
#             data['name'],
#             self.border.name
#         )
#
#     def update_border(self):
#         response = self.client.get(self.url)
#         self.assertEquals(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#         data = response.json()
#         data['name'] = 'new_name'
#
#         response = self.client.put(self.url, data=data, format='json')
#         self.assertEquals(
#             response.status_code,
#             status.HTTP_200_OK
#         )
#         self.border.refresh_from_db()
#         self.assertEquals(
#             self.border.name,
#             data['name']
#         )
#
#     def delete_border(self):
#         self.assertEquals(
#             Border.objects.count(),
#             1
#         )
#         response = self.client.delete(self.url)
#         self.assertEquals(
#             response.status_code,
#             status.HTTP_204_NO_CONTENT
#         )
#         self.assertEquals(
#             Border.objects.count(),
#             0
#         )
