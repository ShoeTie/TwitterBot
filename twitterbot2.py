import time
import tweepy
import json
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import os
#import Queue
import datetime

key = 'UpVz6YmeFjrbqQzeAejLreyhE'
secret = 'BrbTpN56hUiTLiboSM0uaaaRcqJSeauX1kSb82T07GXKxvYpMF'
token = '3315681727-nQcqrXQcSw7L1ym9o2sQrVzoA4dMCb1fSIQtD21'
token_secret = 'lZHzYpBCqfORGCvJAe0qU5mGpjw2HAQVhViEvTDvEX63b'
auth = tweepy.OAuthHandler(key, secret)
auth.set_access_token(token, token_secret)
api = tweepy.API(auth)

#follow = Queue.Queue(1950)

#banned_ids = ('HlelileB' or 'jasondh153'or 'KSHP_DB' or 'TwittTesty' or 'JooohnxBuch' or 'pjgurganus' or 'ptn2pnh' or 'sirrabbits' or 'IKEGameShop')

class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        # Need to decode it first
        decoded = json.loads(data)
        try:
            #Main shitty messy filter; clean up later and make giant if statement look good
            if not decoded['text'].startswith('RT') and not "Fifa" in decoded['text'] and not "BET" in decoded['text']  and not "bet" in decoded['text'] and not "Bet" in decoded['text'] and not "Bot" in decoded['text'] and not "bot" in decoded['text'] and not "B0t" in decoded['text'] and not "vote" in decoded['text'] and not "Vote" in decoded['text'] and not "voting" in decoded['text'] and not "Voting" in decoded['text'] and not "b0t" in decoded['text'] and not "Idaban" in decoded['text'] and not "hentai" in decoded['text'] and not 'Streamys' in decoded['text'] and not "streamys" in decoded['text'] and not 'MTV' in decoded['text'] and not decoded['user']['screen_name'] == 'BlueySkyz' and not decoded['user']['screen_name'] == 'jwatson50' and not "FIFA" in decoded['text'] and not "#Win" in decoded['text'] and not '#WIN' in decoded['text'] and not '#win' in decoded['text'] and not 'fifa' in decoded['text'] and not "GiveawayBot" in decoded['text'] and decoded['user']['followers_count'] > 400 and not decoded['text'].startswith('I') and not'premierleague' in decoded['text'] and not ": RT" in decoded['text'] and not "quoted_status_id" in decoded and not decoded['text'].startswith('@') and not decoded['user']['screen_name'] == 'IKEGameShop' and not decoded['user']['screen_name'] == 'KSHP_DB' and not decoded['user']['screen_name'] == 'TwitTesty' and not decoded['user']['screen_name'] == 'jasondh153' and not decoded['user']['screen_name'] =='hargowwong' and not decoded['user']['screen_name'] =='elizamatt51' and not decoded['user']['screen_name'] == 'Becontests' and not decoded['user']['screen_name'] =='justwin4once' and not decoded['user']['screen_name'] == '' and not decoded['user']['screen_name'] == 'JooohnxBuch' and not decoded['user']['screen_name'] == 'SirRabbits' and not decoded['user']['screen_name'] == 'ptn2pnh' and not decoded['user']['screen_name'] == 'iniallersqueen' and not decoded['user']['screen_name'] == 'PJGurganus' and not decoded['user']['screen_name'] == 'misiawisia' and not decoded['user']['screen_name'] == 'jennym1979' and not "vote" in decoded['text'] and not decoded['user']['screen_name'] == 'ballerstat' and not decoded['user']['screen_name'] == 'jamalpaston' and not decoded['user']['screen_name'] == 'daorapvcs' and not 'stojkovic_alex' in decoded['text'] and not decoded['user']['screen_name'] == 'rbrtbrennan' and not '5sos' in decoded['text'] and not '5SOS' in decoded['text'] and not 'justin' in decoded['text'] and not 'Justin' in decoded['text'] and not "WWE" in decoded['text'] and not 'BETA' in decoded['text'] and not 'Beta' in decoded['text'] and not '1D' in decoded['text'] and not 'styles' in decoded['text'] and not decoded['user']['screen_name'] == 'JDing156' and not decoded['user']['screen_name'] == 'Nocreklamozdera' and not decoded['user']['screen_name'] == 'sportvestinews' and not decoded['user']['screen_name'] == 'getprimenow' and not decoded['user']['screen_name'] == 'skpoovalingam' and not 'lomargie' in decoded['text'] and not decoded['user']['screen_name'] == 'mikobhayangkara' and not decoded['user']['screen_name'] == 'lanadelrwwy' and not decoded['user']['screen_name'] == 'austieb7' and not decoded['user']['screen_name'] == 'Maansii_1' and not decoded['user']['screen_name'] == 'tracy1real' and not decoded['user']['screen_name'] == 'daisy_fur' and not decoded['user']['screen_name'] == 'jodieh1131' and not decoded['user']['screen_name'] =='Bjosh9' and not decoded['user']['screen_name'] == 'glogirl3' and not decoded['user']['screen_name'] =='Natalie41783835' and not decoded['user']['screen_name'] == 'taverner86' and not "porn" in decoded['text'] and not "Porn" in decoded['text'] and not decoded['user']['screen_name'] == 'moultoncheryl1' and not decoded['user']['screen_name'] == 'ZerinaGrace' and not decoded['user']['screen_name'] == 'PayPerVi3w' and not decoded['user']['screen_name'] == 'HandbagFash' and not decoded['user']['screen_name'] == 'BostonNewzer' and not decoded['user']['screen_name'] == 'reinaheather' and not decoded['user']['screen_name'] == 'yarbr012' and not decoded['user']['screen_name'] == 'prizewinner1984' and not decoded['user']['screen_name'] == 'aXismagazine' and not decoded['user']['screen_name'] == 'mellysocks' and not decoded['user']['screen_name'] == 'JennaKateKelly' and not decoded['user']['screen_name'] == 'VOETBALSHIRTS16' and not decoded['user']['screen_name'] == 'OGMerlo' and not decoded['user']['screen_name'] == 'iamshhreya' and not decoded['user']['screen_name'] == 'bryster125' and not decoded['user']['screen_name'] == 'explicitdjp' and not decoded['user']['screen_name'] == 'ThisshKn' and not decoded['user']['screen_name'] == 'KatieHempshall' and not decoded['user']['screen_name'] == 'Gdekupiti' and not decoded['user']['screen_name'] == 'NiallFlorence' and not decoded['user']['screen_name'] == 'fredss33' and not "VMA" in decoded['text'] and not decoded['user']['screen_name'] == 'whissocialmedia' and not decoded['user']['screen_name'] == 'freevacation365' and not decoded['user']['screen_name'] == 'armw501'  and not decoded['user']['screen_name'] == 'ShelaineWood' and not decoded['user']['screen_name'] == 'zepahorteiro' and not decoded['user']['screen_name'] == 'JalapenoMama' and not decoded['user']['screen_name'] == 'tdfrgsn' and not decoded['user']['screen_name'] == 'xcourtnieeex' and not decoded['user']['screen_name'] == 'NoteOnabag' and not decoded['user']['screen_name'] == 'trendinghangout' and not decoded['user']['screen_name'] == 'Irapirsun' and not decoded['user']['screen_name'] == 'PornFan991' and not decoded['user']['screen_name'] == 'kellydpa' and not decoded['user']['screen_name'] == '1337invisible' and not decoded['user']['screen_name'] == 'AngelitaDulcee' and not decoded['user']['screen_name'] == 'cwharris617' and not decoded['user']['screen_name'] == 'AerialGriffin'  and not decoded['user']['screen_name'] == 'LadderLeaper' and not decoded['user']['screen_name'] == 'botfuneur' and not decoded['user']['screen_name'] == 'capitalistgamer' and not decoded['user']['screen_name'] == 'UltimateKing22'and not decoded['user']['screen_name'] == 'TheGiveawayBot' and not decoded['user']['screen_name'] == 'HashTagKCMO' and not decoded['user']['screen_name'] == 'ball_news_2013' and not decoded['user']['screen_name'] == 'SassyDemetriaUK' and not decoded['user']['screen_name'] == 'Dollhouse' and not decoded['user']['screen_name'] == 'WatchJesusFilm' and decoded['in_reply_to_screen_name'] == None:
                # Ignoring all bad characters sent by users
                t = time.ctime()
                print ('@%s: %s %s' %(decoded['user']['screen_name'], decoded['text'].encode('ascii', 'ignore'), t))
                print ('')
                api.retweet(decoded['id'])
                #if "Follow" in decoded['text'] and not "Follow @" in decoded['text'] or 'follow' in decoded['text'] and not 'follow @' in decoded['text'] and not "FOLLOW @" in decoded['text'] or "FOLLOW" in decoded['text'] and decoded['user']['followers_count'] > 500:
                    #if follow.qsize() < 100:
                        #follow.put(decoded['user']['id'])
                        #api.create_friendship(decoded['user']['id'])
                        #print follow.qsize()
                    #else:
                        #api.destroy_friendship(follow.get())

        except tweepy.TweepError as e:
            print (e.message[0]['code'])
            print (e.message[0]['message'])
            print (decoded)
        except KeyError as k:
            print ("KeyError")
            print (k)
            return True
        except AttributeError as a:
            print ("AttributeError")
            print (a)
            return True
        except TypeError as t:
            print ("TypeError")
            print (t)
            return True
        except:
            pass


    def on_error(self, status):
        print ("error")


if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(key, secret)
    auth.set_access_token(token, token_secret)
    print ("Showing all new tweets for retweet win:")


    stream = tweepy.Stream(auth, l)
    stream.filter(track=['retweet win', 'retweet to enter', 'rt to win'])
