import csv
import time
import tweepy

auth = tweepy.OAuthHandler("Rtje2CGsnPBCRPI2YJUTKzzZE","48GsKiMx4EBibNa3AzjG8WbxKjISEv9kRL7RJ5MC0oTbDsHIjM")
auth.set_access_token("716788507977650178-O4jw6bewxVnesm1MEY8V5TkEnlfvzkL","nythJV5Ap4OVv3A0IwVhhmzRraDCWoNcegbmEZ4TyAWtA")

api = tweepy.API(auth)
danveer_csv = open('data1_danveer.csv','w')
spamwriter = csv.writer(danveer_csv,delimiter=',')
danveer_strs = ['VikasKu97729064',
				'ManjuDa46055060',
				'RenuDasi',
				'Rakesh15339929',
				'dass_renu',
				'Seema70591859',
				'RaviKum75576760',
				'PkYesits',
				'AnandRa67560291',
				'AnandDa82055022',
				'mdparmar9850',
				'kamni_dasi',
				'KaniramR',
				'RathodSewa',
				'Aapka__Ankit',
				'sombhusare92605',
				'chandel_dishu',
				'santoshDas2020']

for scrn_name in danveer_strs:
	followings = []
	followers = []
	user = api.get_user(scrn_name)
	print('1',user.screen_name)
	spamwriter.writerow([scrn_name,'followers','followings'])
	for page in tweepy.Cursor(api.friends_ids, screen_name=scrn_name).pages():
	    followings.extend(page)
	    if len(page) == 5000:
	    	time.sleep(60)
	    print('followings done',scrn_name)
	    print(len(page))
	
	for page in tweepy.Cursor(api.followers_ids, screen_name=scrn_name).pages():
	    followers.extend(page)
	    if len(page) == 5000:
	    	time.sleep(60)
	    print('followers done',scrn_name)
	    print(len(page))

	spamwriter.writerow(['',followers,followings])


