import csv
import time
import tweepy

auth = tweepy.OAuthHandler("Rtje2CGsnPBCRPI2YJUTKzzZE","48GsKiMx4EBibNa3AzjG8WbxKjISEv9kRL7RJ5MC0oTbDsHIjM")
auth.set_access_token("716788507977650178-O4jw6bewxVnesm1MEY8V5TkEnlfvzkL","nythJV5Ap4OVv3A0IwVhhmzRraDCWoNcegbmEZ4TyAWtA")

api = tweepy.API(auth)
danveer_csv = open('data1.csv','w')
spamwriter = csv.writer(danveer_csv,delimiter=',')
danveer_strs = ['AnandDa82055022',
				'mdparmar9850',
				'kamni_dasi',
				'KaniramR',
				'RathodSewa',
				'Aapka__Ankit',
				'sombhusare92605',
				'chandel_dishu',
				'santoshDas2020',
                'sanjudas9502']

for scrn_name in danveer_strs:
	followings = ['followings']
	followers = ['followers']
	user = api.get_user(scrn_name)
	print('1',user.screen_name)
	spamwriter.writerow([scrn_name])
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

