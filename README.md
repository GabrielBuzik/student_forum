# student_forum
Student forum written on Django\
The web site is active. Link: https://icef-forum.info/

## About the project
This website has been specifically designed for the students and alumni of the International College of Economics and Finance (ICEF), providing them with a platform to easily connect and engage with one another. Here, individuals can freely share their valuable insights, opinions, and recommendations on various courses, career paths, and esteemed professors. Additionally, students can seek guidance by asking questions, explore employment opportunities, or even hire fellow ICEF students. Through interactive voting systems, the site aims to foster a better understanding of public opinion within the ICEF community.

Currently, the website offers the following key functionalities:
+ Users can sign up on the website by confirming their email address. Upon registration, they receive a unique token via email, which they can use to activate their account. Additionally, registered users have the option to reset their password through email if needed.
+ The website provides open access to various discussions on Professors, Jobs, and Courses. Any visitor can view these discussions. However, registered users have the privilege to create posts within specific pages dedicated to professors, courses, or careers. These posts can contain opinions or questions. Furthermore, posts can be commented on by other users, and they can be ranked on a scale of 1 to 5.
+ A notable feature now available is the ability for registered users to "approve" professors based on their positive experiences interacting with them. This functionality enables the creation of a curated list showcasing the "best professor in ICEF" according to user ratings and feedback.
+ The website also includes professor ratings and post ratings, allowing users to assess the quality and relevance of content.
+ Another significant functionality is the option to publish and view job vacancies. If a job type is specified, users can filter and view vacancies exclusively within their field of interest.

## Set up the web site locally
  - Install python3.10
  ```
    sudo apt install python3.10
  ```
  - Install OS components for running Postgres
  ```
  sudo apt update
  sudo apt install python3-pip python3-dev libpq-dev postgresql postgresql-contrib
  ```
  - Create superuser and tables in the db:
  ```
    sudo -u postgres psql

    CREATE DATABASE icef_forum;
    CREATE USER icef_user WITH PASSWORD 'password';
    ALTER ROLE icef_user SET client_encoding TO 'utf8';
    ALTER ROLE icef_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE icef_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE myproject TO icef_user;
  ```
  - Clone with SSH:
  ```
    git clone git@github.com:javitocor/Affiliate-website-Django.git
  ```
  - Create your own SECRET_KEY, PSQL_PASSWORD, EMAIL_HOST and save it to .env with settings.py
  - Go to this repository and set up vurtual environment
  ```
    python3.10 -m venv venv
  ```
  - Install all the requied libraries
  ```
    pip install -r requirements.txt
  ```
  - Work with migrations
  ```
    cd icef_forum
    python3 manage.py makemigrations
    python3 manage.py migrate
  ```
  - Run the program locally
  ```
    python3 manage.py runserver
  ```
  - If something is wrong, feel free to contact me