import csv
import time
import tweepy
##danveer twitter key

auth = tweepy.OAuthHandler("7kqHnqMbfdEuqaEArutYWJXnc","cVfxGeB4zhGlVbH6IOCFbPbT6OjPZJWirpr2dPFiSukZKRB7xj")
auth.set_access_token("1006577385632743424-lYR67hW7iRS9lWwlgtNbFjUlDn1bC9","U2Dij7g1oap5f21gR0j0UqNcAjLGiNedatdYjDE1VoMTl")

api = tweepy.API(auth)
manish_csv = open('data2.csv','w')
spamwriter = csv.writer(manish_csv,delimiter=',')
manish_strs = [ 'VikasKu97729064',
				'ManjuDa46055060',
				'Rakesh15339929',
				'dass_renu',
				'Seema70591859',
				'RaviKum75576760',
				'PkYesits',
				'AnandRa67560291']

for scrn_name in manish_strs:
	followings = ['followings']
	followers = ['followers']
	user = api.get_user(scrn_name)
	print('1',user.screen_name)
	spamwriter.writerow([scrn_name,'followers','followings'])
	for page in tweepy.Cursor(api.friends_ids, screen_name=scrn_name).pages():
	    followings.extend(page)
	    time.sleep(60)
	    print('followings done',scrn_name)
	    print(len(page))
	
	for page in tweepy.Cursor(api.followers_ids, screen_name=scrn_name).pages():
	    followers.extend(page)
	    time.sleep(60)
	    print('followers done',scrn_name)
	    print(len(page))
        
    spamwriter.writerow(followings)
    spamwriter.writerow(followers)
