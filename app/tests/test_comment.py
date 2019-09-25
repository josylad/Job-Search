from app.models import Comment, User
from app import db


def setUp(self):
        self.user_James = User(username = 'James',password = 'potato', email = 'james@ms.com')
        self.new_comment = Comment(post_id=12345,comment='This post is the best thing since sliced bread', user = self.user_James )
  
        
def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
        
def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.post_id,12345)
        self.assertEquals(self.new_comment.comment,'This ppst is the best thing since sliced bread')
        self.assertEquals(self.new_comment.user,self.user_James)
        
        
def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
        
        
def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)
        
        
