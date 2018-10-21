# ReferralAPI

An API to implement referrals to users based on their email address.

### Pre-requisites - 
Python 3.7.0 or higher

OS - Windows

### Installation instructions - 

1. Clone the repository

2. Install 'virtualenv' to create a virtual environment for our API

   `pip install virtualenv`

3. Setup the virtual environment

   `virtualenv sample_name_for_virtual_env`

4. Activate the virtual environment

   `sample_name_for_virtual_env\Scripts\activate`

5. Install the dependencies

   `pip install -r requirements.txt`

6. Set up the database (first change to the ReferralAPI directory)

   `python manage.py makemigrations`


   `python manage.py migrate`

7. Create a superuser

   `python manage.py createsuperuser`

8. Run the server (on localhost:8000)

   `python manage.py runserver`

### API reference - 

1. **End point** - api/referral_code?user_id=<value>

**Query parameter(s)** - user_id

**Methods allowed** - GET

   Returns a unique 6 digit referral code for the user passed in the query parameter.



2. **End point** - api/referral?referral_code=<value>&referred_email=<value>

**Query parameter(s)** - referral_code, referred_email

**Methods allowed** - POST, DELETE

   Creates/Deletes a referral for the provided referral_code (from the referrer) and the referred_email (email of the recipient of the reference) after performing some basic checks.



3. **End point** - api/conversion?referral_code=<value>&email=<value>

**Query parameter(s)** - referral_code, email

**Body (Request)** - username (content-type : JSON)

**Methods allowed** - POST

   Converts the reference into an active user of the application.