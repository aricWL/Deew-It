# Deew It

Deew it is an app for medical marijuana patients. The medical marijuana industry has made a lot of advancements in the 
past 5 year or so, however diagnosis doesn't go beyond qualifying for a medical marijuana card.

Medical marijuana licenses get handed out every day without the patients actually getting the specific treatment they need
for their ailments. 

Deew It's goal is to fix this problem. Using matching techniques and database queries, Deew It finds marijuana strains
that best fit the needs of the patient.

Take a look for yourself [here](https://deewit.herokuapp.com) if interested!

## Setup

To get the app running locally, first create a virtual environment and pip install everything in requirements.txt

Next, you need to create a database(deewit). Also, delete the migrations folder, as you will be making your own.

Now it is time to run some commands in the terminal.

1. python manage.py db init
2. python manage.py db migrate
3. python manage.py db upgrade

Good work! Now you need to run the scraper, this will populate our database.

python scraper.py

You're all set! Type "python app.py" and you're good to go.
