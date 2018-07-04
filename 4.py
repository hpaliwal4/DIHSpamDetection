##I'm Importing the Original Spammers we have Collected

import csv
import tweepy
##Danveer
auth = tweepy.OAuthHandler("7kqHnqMbfdEuqaEArutYWJXnc","cVfxGeB4zhGlVbH6IOCFbPbT6OjPZJWirpr2dPFiSukZKRB7xj")
auth.set_access_token("1006577385632743424-lYR67hW7iRS9lWwlgtNbFjUlDn1bC9","U2Dij7g1oap5f21gR0j0UqNcAjLGiNedatdYjDE1VoMTl")

api = tweepy.API(auth, wait_on_rate_limit=True)
datafile = open('original_data.csv','r')
csvreader = csv.reader(datafile)
nodes = []
followers = []
followings = []
for row in csvreader:
    if row[0] != 'followings' and row[0] != 'followers':
        #print(row[0])
        nodes.append(api.get_user(row[0]))
    else:
        if row[0] == 'followings':
            followings.append(row[1:])
        else:
            followers.append(row[1:])


class Node:
	
	def __init__(self,
				user,
				parent_node,
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

ratio = []
for i in range(len(nodes)):
    ratio.append(len(followings[i])/len(followers[i]))
status_count = [] # tweets and Retweets Count
for idx,one in enumerate(nodes):
    status_count.append(one.statuses_count)
all_instances = []

for idx,node in enumerate(nodes):
    user = Node(node,parent_node=node,main_node=1,followers=followers[idx],followings=followings[idx])
    all_instances.append(user)

from collections import defaultdict
import datetime
##making nodes for followers
map_nodes = {}
map_nodes = defaultdict(lambda: None, map_nodes)
followers_instances = []
for idx,node in enumerate(all_instances):
	if idx
    print(idx)
    time = datetime.datetime.now()
    instance = []
    for follower in followers[idx]:
        if map_nodes[follower] == None:
            user__ = api.get_user(follower)
            node = Node(user = user__,parent_node=node)
            map_nodes[follower] = [node]
            instance.append(node)
        else:
            map_nodes[follower].append(node)
    print(datetime.datetime.now() - time)
    followers_instances.append(instance)