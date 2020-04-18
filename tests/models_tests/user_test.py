from tests import OhmTestCase


class UserTest(OhmTestCase):
    def test_get_multi(self):
        assert self.chuck.get_multi("PHONE") == ['+14086441234', '+14086445678']
        assert self.justin.get_multi("PHONE") == []

    def test_refactored_below_tier(self):
    	self.chuck.tier = 'Gold'
    	lower_tier = 'Carbon'
    	assert self.chuck.is_below_tier(lower_tier) == False

    	higher_tier = 'Platinum'
    	assert self.chuck.is_below_tier(high_tier) == True

    	same_tier = 'Gold'
    	assert self.chuck.is_below_tier(same_tier) == False