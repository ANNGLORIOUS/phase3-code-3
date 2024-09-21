# SA. Week 3 Code Challenge: Concerts

#### By **{List of contributors}**
This project was created and is sole property of Annglorious mueni.

## Project Overview
For this assignment, we'll be working with a Concert domain.

We have three models: Band(name and hometown),Venue(title and city), and Concert.

For our purposes, a Band has many Concerts, a Venue has many Concerts, 
and a Concert belongs to a Band and to a Venue.

Band - Venue is a many to many relationship.

### Schema Overview
#### Tables
##### Bands

1. id (Primary Key)
2. name (String)
3. hometown (String)

##### Venues

1. id (Primary Key)
2. title (String)
3. city (String)

##### Concerts

1. id (Primary Key)
2. band_id (Foreign Key referencing Bands)
3. venue_id (Foreign Key referencing Venues)
4. date (String)
#### Relationships
1. A Band can have many Concerts.
2. A Venue can host many Concerts.
3. A Concert belongs to one Band and one Venue.

### Methods
#### Band Methods
- Concerts(): Returns all concerts for the band.
- Venues(): Returns all venues the band has performed at.
- Play_in_venue(venue, date): Creates a new concert for the band.
- All_introductions(): Returns an array of introductions for all concerts.
#### Venue Methods
- Concerts(): Returns all concerts at the venue.
- Bands(): Returns all bands that have performed at the venue.
- Concert_on(date): Finds the first concert on a given date.
- Most_frequent_band(): Returns the band with the most concerts at the venue.
#### Concert Methods
- Band(): Returns the band instance for the concert.
- Venue(): Returns the venue instance for the concert.
- Hometown_show(): Returns true if the concert is in the band's hometown.
- Introduction(): Returns a string introduction for the concert.
##### Class Method
- Band.most_performances(): Returns the band that has played the most concerts.



## Setup/Installation Requirements
* One would need either linux or wsl for window users
* A copy of visual basic code installed
* A github account

1. Open your terminal and go to the directory you wish to work from.
2. Go to the following url using ur github account https://github.com/ANNGLORIOUS/phase3-code-3
3. Go to the code tab and clone the ssh key
4. Go back to the termina and type git clone <-followed by the ssh key you copied /cloned ->
5. Enter your new cloned repository and type in code .
6. On the visual studio code that has now opened, go to the the run tab.
7. Install the requied packages and set up the required database.
## Technologies Used
This program is built purely with python using the visual code environment.

## Support and contact details
For any issues please email me at annglorious.mueni@student.moringaschool.com
### License
Apache License 2.0


