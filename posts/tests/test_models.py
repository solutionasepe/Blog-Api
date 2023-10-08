from django.test import TestCase
from django.contrib.auth.models import User
from posts.models import Post

# Create your tests here.
class BlogTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        
        testuser1 = User.objects.create_user(username='solution', password="password123DKJ")
        testuser1.save()

        test_post = Post.objects.create(
            author = testuser1,
            title = "blog",
            body = "content of the post",
        )
        test_post.save()

    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = "{}".format(post.author)
        title = "{}".format(post.title)
        body = "{}".format(post.body)
        self.assertEqual(author, "solution")
        self.assertEqual(title, "blog")
        self.assertEqual(body, "content of the post")