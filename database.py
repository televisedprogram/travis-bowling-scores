"""Module that gets information from the database"""
import sqlite3

def get_tweet_db():
    """
    """
    conn = sqlite3.connect('tbirdbowls.db')
