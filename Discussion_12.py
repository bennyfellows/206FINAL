import unittest
import sqlite3
import json
import os
# Hello
# test
#hey - benny
# Read in and set up the Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

#return the name of the artist from a given album title named 'album_title'
#HINT: JOIN on the tables 'artists' and 'albums'
def get_artist_from_album(cur, conn, album_title):
    curr.execute('SELECT artists.Name FROM albums JOIN artists ON albums.ArtistId=artists.ArtistId WHERE albums.Title= ?',(album_title, ))
    name = cur.fetchone()
    return name
     

#return a list of unique tuples, where each tuple is the name of a customer (FirstName, LastName) who got an invoice for the City = billing_city
#HINT: JOIN on the tables 'invoices' and 'customers'
def get_customers_from_invoice_billing_city(cur, conn, billing_city):
    cur.execute("SELECT customers.FirstName,customers.LastName FROM invoices JOIN customers ON customers.CustomerId=invoices.CustomerId WHERE invoices.BillingCity=?",(billing_city, ))
    custs = cur.fetchall()
    new = set(custs)
    end = list(new)
    return end

#return a list of customer email ids for all invoices generated with the billing postal codes in the set 'postal_codes'
#HINT: JOIN on the tables 'invoices' and 'customers'
def get_emails_from_billing_postal_codes(cur, conn, postal_codes):
    cur.execute('SELECT customers.Email FROM invoices JOIN customers ON invoices.BillingPostalCode=customers.PostalCode WHERE invoices.BillingPostalCode IN (%s)' % ("?," * len(postal_codes))[:-1], postal_codes)
    email = cur.fetchall()
    set1 = set(email)
    return list(set1)

#return a list of tuples, where each tuple is of the format (track_name, media_type), for all music tracks in the table 'tracks'
#HINT: JOIN on the tables 'tracks' and 'media_types'
def get_media_types_and_tracks(cur, conn):
    cur.execute('SELECT tracks.track_name FROM tracks JOIN tracks ON tracks.media_types = tracks.track_name WHERE tracks.track_name IN (%s)' % ("?," * len(postal_codes))[:-1], postal_codes)
    track = cur.fetchall()
    track2 = set(emails)
    return list(track2)

#return a tuple with the format (track_name, album_name, artist_name), for a given music track called 'my_track' from the table 'tracks'
#HINT: This requires a join on 3 tables!
def get_artist_from_track(cur, conn, my_track):
    cur.execute('SELECT tracks.track_name FROM tracks JOIN tracks ON tracks.album_name = tracks.artist_name WHERE tracks.track_name IN (%s)' % ("?," * len(postal_codes))[:-1], postal_codes)
    music = cur.fetchall()
    tracks = set(music)
    return list(tracks)

##########Don't make any changes below this line############

def main():
    cur, conn = setUpDatabase('chinook.db')
    print('--------get_artist_from_album----------')
    print(get_artist_from_album(cur, conn, 'Facelift'))
    print('---------get_customers_from_invoice_billing_city---------')
    print(get_customers_from_invoice_billing_city(cur, conn, 'London'))
    print('--------get_emails_from_billing_postal_codes----------')
    print(get_emails_from_billing_postal_codes(cur, conn, ('1016', '10789', '2113') ))
    print('---------get_media_types_and_tracks---------')
    for tup in get_media_types_and_tracks(cur, conn)[:10]:
        print(tup)
    print('------------------')
    print(get_artist_from_track(cur, conn, 'Evil Walks'))
    
if __name__ == "__main__":
    main()