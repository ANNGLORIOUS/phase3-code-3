from lib.models import Band, Venue, Concert
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random

engine = create_engine('sqlite:///lib/concerts.db')
Session = sessionmaker(bind=engine)
session = Session()

new_band = Band(name="BlackPink", hometown="Las Vegas, Nevada")
new_band = Band(name="BTS", hometown="tokyo ,Japan")
new_band = Band(name="StrayKids", hometown="Eldoret , Canada")
new_band = Band(name="Twice", hometown="New Zealand, Canada")
new_band = Band(name="BigBang", hometown="England, United States")
session.add(new_band)
session.commit()

new_venue = Venue(title="Nyayo Stadium", city="Las Vegas")
new_venue = Venue(title="Parkway Center", city="New York City")
new_venue = Venue(title="MGM Grand", city="New York City")
new_venue = Venue(title="Wembley Stadium", city="London")
new_venue = Venue(title="Empire State Building", city="New York City")
session.add(new_venue)
session.commit()

new_concert = Concert(date="2024-02-11", name="Super Bowl LVIII", band_id=new_band.id, venue_id=new_venue.id)
new_concert = Concert(date="2024-02-18", name="The Voice Live", band_id=new_band.id, venue_id=new_venue.id)
new_concert = Concert(date="2024-02-25", name="The Voice Live", band_id=new_band.id, venue_id=new_venue.id)
new_concert = Concert(date="2024-03-01", name="The Voice Live", band_id=new_band.id, venue_id=new_venue.id)
new_concert = Concert(date="2024-03-08", name="The Voice Live", band_id=new_band.id, venue_id=new_venue.id)
session.add(new_concert)
session.commit()

bands = session.query(Band).all()
venues = session.query(Venue).all()
concerts = session.query(Concert).all()

for band in bands:
    print(band.name)

for venue in venues:
    print(venue.title)

for concert in concerts:
    print(concert.name)