class Node:
	
	def __init__(self,
				user,
				parent_node = None,
				main_node = 0,
				followers = None,
				followings = None,
				spammer = None):
		

		self.user = user
		self.username = user.screen_name
		self.followers_count = user.followers_count
		self.followings_count = user.friends_count
		self.status_count = user.statuses_count ## tweets and retweets count
		self.likes_count = user.favourites_count ## count of likes and favourites
		self.main_node = main_node ##tells us if this is the parent node or not
		self.followers = followers ##list containing ids of all followers
		self.followings = followings ##list containing ids of all followings
		self.parent_node = parent_node ##main_node from which it is derived
		self.spammer = main_node ## if its spammer or not || if it's main node is 1 then its a spammer

	
	def ffratio(self):
		return (self.user.friends_count)/(self.user.followers_count)

	def __str__(self):
		return self.username




