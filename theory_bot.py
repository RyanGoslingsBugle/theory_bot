#!/usr/bin/env python
 
import twitter, random

api = twitter.Api(consumer_key = xxxxxx,
                  consumer_secret = xxxxxx,
                  access_token_key = xxxxxx,
                  access_token_secret = xxxxxx)

noun_list_file = open('nouns.txt')
noun_list = noun_list_file.readlines()

def get_followers():
    """
    Automatically follows all new followers, and sends them a welcome message.
    """
    following = api.GetFriendIDs()
    followers = api.GetFollowerIDs()

    not_following_back = []
    
    for f in followers:
        if f not in following:
                not_following_back.append(f)

    for user_id in not_following_back:
        try:
            api.CreateFriendship(user_id)
            user = api.GetUser(user_id)
            api.PostUpdate('@' + str(user.GetScreenName()) + ' Proletarian greetings to you, comrade.')
        except Exception as e:
            print("error: %s" % (str(e)))

def post_update():
    api.PostUpdate(create_status())
    
def create_status():
    status = ''
    status = 'Towards a Marxist theory of ' + random.choice(noun_list)
    return status

def start():
    post_update()
    get_followers()

start()
