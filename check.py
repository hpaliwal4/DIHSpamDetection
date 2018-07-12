import csv
import time
import tweepy
##danveer twitter key

auth = tweepy.OAuthHandler("7kqHnqMbfdEuqaEArutYWJXnc","cVfxGeB4zhGlVbH6IOCFbPbT6OjPZJWirpr2dPFiSukZKRB7xj")
auth.set_access_token("1006577385632743424-lYR67hW7iRS9lWwlgtNbFjUlDn1bC9","U2Dij7g1oap5f21gR0j0UqNcAjLGiNedatdYjDE1VoMTl")

api = tweepy.API(auth)
user = api.get_user(179014215)
print(user._json)