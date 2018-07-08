import tweepy
import csv


auth = tweepy.OAuthHandler("7kqHnqMbfdEuqaEArutYWJXnc","cVfxGeB4zhGlVbH6IOCFbPbT6OjPZJWirpr2dPFiSukZKRB7xj")
auth.set_access_token("1006577385632743424-lYR67hW7iRS9lWwlgtNbFjUlDn1bC9","U2Dij7g1oap5f21gR0j0UqNcAjLGiNedatdYjDE1VoMTl")

api = tweepy.API(auth)

class Node:

	def __init__(self,id = None,username = None,followings=None,followers=None):
		self.id = id
		self.followings = followings
		self.followers = followers
		self.username = api.get_user(id).screen_name


	def getid(self):
		return self.id

	def getname(self):
		return self.screen_name

	def addfollowers(self,val):
		self.followers.extend(val)

	def addfollowings(self,val):
		self.followings.extend(val)

	def allfollowers(self):
		return self.followers

	def allfollowings(self):
		return self.followings


print(api.get_user('harshpaliwal_cc').id)

datafile = open('data1_danveer.csv','r')
extracter = csv.reader(datafile)

for row in extracter:
	if row[0] == '':
		node = Node(id = api.get_user(name).id,followings=row[2],followers=row[1])
		print(name,len(row[1]),len(row[2]))

	else:
		name = row[0]
