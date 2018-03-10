"""Helps get the API without hard coding tokens"""
import tweepy

def get_api_from_tokens(api_key, api_secret, token, token_secret):
    """
    Gets an api object from entered tokens

    Arguments:
        api_key: the oauth api key
        api_secret: the oauth api secret
        token: the twitter access token
        token_secret: the twitter access token secret
    Returns:
        a tweepy api object
    """
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(token, token_secret)

    api = tweepy.API(auth)
    return api
