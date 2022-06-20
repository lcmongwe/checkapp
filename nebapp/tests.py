from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Post,User


# Create your tests here.
class PostTest(TestCase):
    '''
    test class for Post model
    '''
    def setUp(self):
       
        self.new_post = Post(title='blog')
        self.new_post.save_post()
        self.new_post = Post(  image='images/blog.jpg',title='blog',description='this is a blog' )
        self.new_post.save_post()
        self.post2 =Post(  image='images/gallery.jpg',title='gallery',description='this is a gallery' )
        self.post2.save_post()
    def tearDown(self):
     
        Post.objects.all().delete()
        Post.objects.all().delete()
    def test_save_post(self):
        '''
        test method to ensure an post instance has been correctly saved
        '''
        self.assertTrue(len(Post.objects.all()) == 2)
    def test_instances(self):
        '''
         method to test instances created successfully during setUp
        '''
        self.assertTrue(isinstance(self.new_post,Post))
        

    def test_delete_post(self):
        '''
        test method to ensure an post is deleted correctly deleted
        '''
        self.new_post.delete_post()
        self.assertTrue(len(Post.objects.all()) == 1)




class UserTest(TestCase):
    '''
    test class for profile model
    '''
    def setUp(self):
  
        self.new_user =  User(name='lucy',phone='123',email='lucy@gmail.com',image='images/gallery.jpg')
        self.new_user.save_user()

    def tearDown(self):
        '''
        test method to delete Category instance
        '''
        User.objects.all().delete()

    def test_save_user(self):
        '''
        test for profile instance has been correctly saved
        '''
        self.assertTrue(len(User.objects.all()) == 1)

    def test_delete_user(self):
        '''
        test a Category instance has been correctly deleted
        '''
        self.new_user.save_user()
        self.assertTrue(len(User.objects.all()) == 0)


