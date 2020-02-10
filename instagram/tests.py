from django.contrib.auth.models import User
from user.models import Profile
from django.test import TestCase
from .models import Image
class Intagram_TestCases(TestCase):
    def setUp(self):
        self.user1= User(id=1,username='cate',email='catenduku995gmail.com',password='cate1234')
        self.user1.save()
        self.profile = Profile(bio='plucker',profile_path='media/', default='profile_pics/pro.jpg')
        self.profile.save_profile()
        self.new_image = Image(id=1,caption='avechi', author='cate',image_path='media/', default='images/dance.jpg')
        self.new_image.save_image()

    def tearDown(self):
        # Profile.objects.all().delete()
        User.objects.all().delete()
        Image.objects.all().delete()

    def test_is_instance(self):
        self.assertTrue(isinstance(self.user1,User))
        self.assertTrue(isinstance(self.profile,Profile))
        self.assertTrue(isinstance(self.new_image,Image))

    # def test_save_method(self):
    #     self.new_image.save_image()
    #     all_objects = Image.objects.all()
    #     self.assertTrue(len(all_objects)>0)

#     def test_delete_method(self):
#         self.new_image.save_image()
#         filtered_object = Image.objects.filter(author='cate')
#         Image.delete_image(filtered_object)
#         all_objects = Image.objects.all()
#         self.assertTrue(len(all_objects) == 0)

#     def test_display_all_objects_method(self):
#         self.new_image.save_image()
#         all_objects = Image.retrieve_all()
#         self.assertEqual(all_objects.author,'cate')


#     def test_update_single_object_property(self):
#         self.new_image.save_image()
#         filtered_object =Image.update_image('cate')
#         fetched = Image.objects.get(author='cate')
#         self.assertEqual(fetched.author,'cate')
#     def test_get_image_by_id(self):
#         self.new_image.save_image()
#         fetched_image = Image.get_image_by_id(1)
#         self.assertEqual(fetched_image.id,1)
#     def test_search_by_username(self):
#         self.profile.save_profile()        
#         fetch_specific = Profile.objects.get(user=1)
#         self.assertTrue(fetch_specific.id==1)
