# Flight Bookings
A flight bookings web app using Django and PostgreSQL

![all-devices-mockup](planning_files/flight-app-on-all-devices.png)

[Back to Contents](#Contents)

## Live deployment
[Flight Booking - Heroku Live Deployment](https://mogr-flight-booking-fe5c31fca0d1.herokuapp.com/)

## Product Goals
My goal for the website is to be able to book and view flights from any airline and airport, to be able to get anywhere without having to register to several different airlines to book your holiday. This is especially a problem when you are taking more flights than just the standard two-way trip. (transit flights)

A user must be able to view the departures and book a flight, with their passenger requirements.

Expanding from the MVP, a user should be able to pick a date to schedule their flight, as well as pick the seats for their flight. Transit booking should be available.

[Back to Contents](#Contents)

## Contents

1. [Flight Bookings](#flight-bookings)
  - [Live Deployment](#live-deployment)
  - [Product Goals](#product-goals)
2. [UX/UI](#ux---user-experience)
  - [User Stories](#user-stories)
  - [Design Inspiration](#design-inspiration)
    - [Colour Scheme](#colour-scheme)
  - [Design Experiences](#design-experiences)
  - [Wireframes](#wireframes)
  - [Deployed App Screenshots](#deployed-app-screenshots)
3. [Features](#features)
  - [Present Features](#present-features)
  - [Future Development](#future-development)
4. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
5. [Agile Methodologies - Project Management](#agile-methodologies---project-management)
  - [MoSCoW Prioritization](#moscow-prioritization)
6. [Deployment](#deployment)
  - [Cloning from GitHub](#cloning-from-github)
  - [PostgreSQL Database](#postgresql-database)
  - [Heroku deployment](#heroku-deployment)
7. [Technologies Used](#technologies-used)
8. [Testing](#testing)
  - [Validator Testing](#validator-testing)
    - [HTML](#html)
    - [CSS](#css)
    - [JavaScript](#javascript)
    - [Python](#python-validation)
    - [Lighthouse](#lighthouse)
    - [Wave](#wave-accessibility-evaluation)
  - [Feature Testing](#feature-testing)
9. [Use of AI](#use-of-ai)
  - [Code Creation](#code-creation)
  - [Debugging](#debugging)
  - [Performance and User Experience](#performance-and-user-experience)
  - [Automated Test Units](#automated-test-units)
  - [Workflow](#workflow)
10. [Credits](#credits)
11. [Acknowledgements](#acknowledgements)

# UX - User Experience

![User Flow](planning_files/User-Flow.jpg)

[Back to Contents](#Contents)

## User Stories

**Story 1 - Flight Details**

As a trip planner, I want to be able to view what flights are available to book, so I know whether my intended destination is available before I register and login.

**Acceptance Criteria**

• Users that aren't logged in can see a departure board for all the flights, including a status column for delayed, on time, or cancelled status.

---

**Story 2 - User Booking**

As a member of the senior director team, I want to be able to make a booking so I can promptly reach my intended destination.

**Acceptance Criteria**

• Logged in users can create a flight booking from a selection of flights.

---

**Story 3 - User Manage Bookings**

As a family, we want to be able to add more passengers to our booking, and detail our passengers dietary requirements and baggage requirements for our booking.

**Acceptance Criteria**

• Users can view their bookings, and delete the booking.

• Users can update their passenger information, add more passengers, or delete passengers.

---

**Story 4 - User Notifications**

As a late flier, I need to know if my booking has been accepted. The gate is closing in 10 minutes!

**Acceptance Criteria**

• Whenever a user creates, updates, or deletes a booking, they are informed with a message.

• Whenever a user creates, updates, or deletes a passenger, they are informed with a message.

• Booking form has validation, so the user can rest assured that their booking was successful, and their details have been accepted and registered correctly.

• User is notified via message whenever they; register, login, logout.

---

**Story 5 - User Registration and Login**

As a frequent flier, I want to login with my existing account to make my booking.

**Acceptance Criteria**

• Any user can create a user access level account.

• Account registration form has validation.

---

**Story 6 - Admin Bookings and Flights**

As the site owner, I want to be able to populate the flight board, update the flight status, and help a customer with any booking changes they wish to make.

**Acceptance Criteria**

• An admin can login and view bookings and flights.

• An admin can modify or delete bookings and passengers.

• An admin can modify or delete flights.

---

**Story 7 - Responsiveness**

As a flier on the go, I don't have regular access to a laptop or desktop, I need to be able to use the site on my phone.

**Acceptance Criteria**

• The website displays responsiveness across all devices.

• The website has aria labels, acceptable contrasts, and other accessibility features to ensure all users can use the site for their travel needs.

---

**Story 8 - Access Control**

As the site owner, it is my responsibility to ensure that users cannot access each others records, or worse, the admin page!

**Acceptance Criteria**

• Users can see, edit, add, or delete their own bookings/passengers but no one elses. They can select a flight to book, but can't modify a flight.

• Admin have access to see and modify a booking/passengers, and any flight.

• Users that aren't logged in can see flights and their status, but cannot make a booking.

---

[Back to Contents](#Contents)

## Design Inspiration
I shopped around to see what other designs already exist for flight booking sites.

Notably I took a look at airports directly as well to see how they were displaying their departure boards. I then picked out what was good, and what could be improved, and iterated upon these to come up with my own departure boards and design.

[Heathrow Departures](https://www.heathrow.com/departures)

[Bristol Departures](https://www.bristolairport.co.uk/arrivals-and-departures/departures)


### Colour Scheme
For my colour scheme, I used adobe colour and passed some images through to generate a palatte from the image.

![full-palatte](planning_files/final-colour-palatte.png)

My two images I sourced from pexels.com

![space-shuttle](planning_files/colour-scheme-image.webp)

Author: [Kristina Paukshtite](https://www.pexels.com/@kpaukshtite/)

![airplane-on-clear-sky](planning_files/colour-scheme-image-2.webp)

Author: [Allan Carvalho](https://www.pexels.com/@allan-carvalho-264847051/)

This second image went on to inspire my logo choice as well.

```background```  ```#9DC6E0```

```navbar and footer``` ```#035487```

```hover and highlights``` ```#1BB5F1```

```light font colour``` ```#EDF3F7```

```dark font colour``` ```#031D35```

```less dark font colour``` ```#0D2C4D```

![colour-palatte-small](planning_files/mini-colour-palate.png)

[Back to Contents](#Contents)

## Design Experiences
Initally during development, I felt I would have time to have an additional CRUD for flight seating. I would have liked to have been able to show a plane graphic with an overlay table with cell buttons to pick a flight. Some seats would be blocked out or red to indicate they can't be booked.

Early on into the project, that idea was scrapped as a third CRUD and plane seat interactive layout would take far too much time. However, I still had time to design the database for this feature.

[Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)

In the end, our modelling in Django used an object Foreign Key rather than an integer to the id for the Foreign Key. This made object manipulation for our tables possible in the view, and made creating and maintaining the logic much easier.

The flights table didn't end up using the "is_departure" field, as using this boolean would require us to have duplicate flight data: an entry for a flight departing, and another for the same flight but for its arrival time. Instead I added two extra fields into the model; arrival_scheduled_time, and arrival_expected_time. This would allow me to keep the full flight data to one entry, and would make future development for a departure/arrival toggle much easier.

[Back to Contents](#Contents)

## Wireframes

![Flight homepage - wireframe](planning_files/Flight-homepage-wireframe.png)

[Back to Contents](#Contents)

## Deployed App Screenshots

<details open>
    <summary>Every app page</summary>  
    <img src="planning_files/Homepage.png">  
    <img src="planning_files/Flight-detail.png">  
    <img src="planning_files/my-bookings.png">
    <img src="planning_files/booking-passengers.png">
</details>

<details>
  <summary>Added another passenger</summary>
  <img src="planning_files/second-passenger-added.png">
</details>

<details>
  <summary>Auth Login/Register/Logout pages</summary>
  <img src="planning_files/login.png">
  <img src="planning_files/register.png">
  <img src="planning_files/sign-out.png">
</details>

<details>
    <summary>Messages</summary>  
    <img width="250" src="planning_files/signed-in-message.png">
    <img width="250" src="planning_files/signed-out-message.png">
    <img width="250" src="planning_files/flight-booked-message.png">
    <img width="250" src="planning_files/passenger-details-update-message.png">
    <img width="250" src="planning_files/passenger-removed-message.png">
    <img width="250" src="planning_files/booking-removed-message.png">
</details>

[Back to Contents](#Contents)

# Features 

## Present Features

• **Homepage:** The user first arrives at the site on the homepage. Regardless of being logged in or not, they can see the departure board. We use alternating colours for each row to help highlight and differentiate them for ease of use for reading off a row of flight information.
From here, they can click or tap on any flight to get further details.

If the user is viewing the site from a mobile or tablet device, some of the columns will have disappeared and an expand info button appears to the right of every row.
Clicking (or tapping) this button expands the row and shows the missing information below that flight. Clicking the button again shrinks that row. Clicking a different row's button also shrinks all other rows.

If logged in, below the navbar the user is told they are logged in. Otherwise, they are informed to register or login to book a flight.

---

• **Flight Details:** When a user clicks (or taps) onto a flight, they are taken to the flight detail page. Here they can see the arrival information for that flight, (which is not displayed on the departure board) which is important in the decision making process of booking a flight as arrival time can be critical for meetings or opening times for venues at their destination.

Below the flight details is a passenger form. Here they can fill out one passenger and book the flight, they can specify any dietary requirements they have and choose what baggage they would like to bring.
A user will only see the passenger form if they are logged in.

Once a flight is booked, a message is displayed below the navbar confirming their booking. They can also navigate to the "My Booking" page to add more passengers or make any other changes to their booking.

---

• **My Booking:** This page shows the user their most recent booking first, followed by all their other bookings. Like with the homepage, a user can click (or tap) on the expand button to view the full flight details if they are on mobile or tablet.
Unlike the homepage we show the full flight information here, as we do with the flight detail page. This is because the homepage is a departure board page and should focus on the required information for a departure.

Clicking (or tapping) on a booking via the "Booking Detail" button, will send the user to a booking passengers page where they can make further changes to their booking, rather than just view their booking.

---

• **Booking Details** Once the user has navigated to this page, they can view all of the passengers they have on a booked flight. They can make edits to that passenger or delete them from the booking. Deleting or editing a passenger gives a message to confirm this below the navbar, as well as resending them to this page so they can confirm the changes themself.
They can also delete the entire booking. If they do this, the user is redirected to their "My Booking" page, so they can edit or view the details of another booking and again, also confirm that the booking has successfully deleted. A message regardless is also viewable below the navbar that informs the user that the booking was deleted.

[Back to Contents](#Contents)

## Future Development

### Homepage
• **Arrivals Board:** A toggle switch for the homepage to flick between arrivals board, and the departure board.
• **Airport Selector:** Another homepage feature that would allow the user to select another airport to view the departures/arrivals for.
• **Calendar Selector:** This would allow the user to change the date they are viewing flights for, so that they could see and book flights for a future trip.
• **Terminal and Gate:** A user may be viewing the app as they make their way to the airport, or when they are in the airport. Having up to date information for the departure board that showed Terminal and Gate for flights (for current day) would be very useful in this use-case.

### Flight Detail
• **Multiple Passengers:** A more streamlined approach would be to allow a user to fill multiple passenger forms at the same time as they initially make a booking. Rather than currently requiring to go to a specific booking in their "My Booking" section to add these initial passengers.
• **Add to existing booking:** Currently each flight has their own booking, a user may want to book a return trip (which would involve having two flights in the same booking) and often many countries require you to have a return trip booked before you can come to the country on a temporary work visa or holiday visa. This would help streamline the user experience when meeting this legal (and convenient) requirement, and planning their trip.

[Back to Contents](#Contents)

# Database Schema - Entity Relationship Diagram

![database schema](planning_files/database-schema.png)

[Back to Contents](#Contents)

# Agile Methodologies - Project Management
During development, I used GitHub Projects which is a github kanban board. (link below)
In each issue I identified a user requirement and wrote it into a user story, within each issue is then the acceptance criteria for each story that gives a brief on what is needed to fulfill/meet the requirement.

The Kanban board of user stories is split into three columns; Todo, In Progress, and Done.

[GitHub Project Board](https://github.com/users/mogr20/projects/7)

Sprint 1: Database Schema

Sprint 2: Models and Views

Sprint 3: Basic Templates to utilise the views

Sprint 4: UX design and implementation

Sprint 5: Access Control

Sprint 6: Accessibility and finalization

## MoSCoW Prioritization
Within my Kanban board, we have MoSCoW priortization labels. These help identify (from a glance) what tasks should be priortized.
The labels include; must-have, should-have, could-have, and won't have.

[Back to Contents](#Contents)

# Deployment
All code was written in Visual Studio as the IDE. GitHub and Git were used for version control, and the application was deployed to Heroku from GitHub.

## Cloning from GitHub
1. Clone the repository in git bash
```git clone https://github.com/mogr20/flight-bookings.git```
2. Navigate to the project folder
```cd [your project folder here]```
3. Open in VSCode
```code .```

## PostgreSQL Database
4. Create a new PostgreSQL Database
5. Connect your database to your VSCode environment with a env.py file (we are already ignoring this file in the cloned .gitignore)
6. Create a ```os.environ.setdefault``` key-value pair for ```SECRET_KEY``` and ```DATABASE_URL``` in your env.py file
7. Run the command: ```python3 manage.py migrate```
8. Create a super user: ```python3 manage.py createsuperuser```
9. Commit the migrations to your cloned repo: ```git add .```, ```git commit -m [your message here]```, ```git push```

## Heroku deployment
10. Create a new app. Login to Heroku (or make a new account) go to your Dashboard and click "Create New App"
11. Select an appropriate region (I selected Europe for my deployment)
12. In the "Deploy" tab, select GitHub as the deployment method
13. Search for the repository name and click "Connect"
14. Go to the "Settings" tab, and add config var settings for; DATABASE_URL and SECRET_KEY
15. In VSCode, settings.py add the deployed app to ALLOWED_HOSTS
16. Push that update ```git push```
17. Back in Heroku, in the "Deploy" tab connect to your GitHub cloned repo to deploy, and deploy
18. After a successful deployment, a "View" button will appear that will open the live site in a new tab

[Back to Contents](#Contents)

# Technologies Used
**HTML5** - Markup language for the web template structure

**CSS** - Styling language for styling the web templates

**JS** - Web interactivity and DOM manipulation

**Bootstrap** 5.3.3 - Styling and frontend toolkit for rapid design

**Python** 3.12.8 (Django 4.2.20) - Backend web framework, for views, models, and dynamic templates

**PostgreSQL** - Database storage and management, created by django models, and manipulated via django views

**Whitenoise** 5.3.0 - Serves the static files directly from Django

**Heroku**- Online hosting service for the website

[Back to Contents](#Contents)

# Testing 
## Validator Testing 

### HTML
Passed - with warning

https://validator.w3.org/nu/

Warning for aria-label on copyright logo, however WAVE insisted I added this labelling.

![aria-label](planning_files/aria-label-warning.png)

### CSS
Passed

https://jigsaw.w3.org/css-validator/

### JavaScript
Passed

https://jsvalidator.com/

### Python
Passed

https://pep8ci.herokuapp.com/

### LightHouse
Above 80 in performance on mobile and across the whole site.

Index Homepage:

![index homepage](planning_files/index-homepage.png)

Flight Detail page:

![flight detail page](planning_files/flight-detail-page.png)

My Bookings page:

![my bookings page](planning_files/my-bookings-page.png)

Booking Passenger page:

![booking passenger detail page](planning_files/booking-passenger-detail-page.png)

[Back to Contents](#Contents)

### Wave Accessibility Evaluation
Passed
https://wave.webaim.org/

![WAVE](planning_files/WAVE.png)

[Back to Contents](#Contents)

## Feature Testing
| Page | Feature | Action | Effect | Pass? |
|:-----|:--------|:-------|:-------|:------|
|Homepage|Site Logo|Click|Redirects to home page from all pages|yes|
|Homepage|Logged In User Display|Log in as existing user|Username appears below navbar|yes|
|Homepage|Home link|Click|Redirects to home page from all pages|yes|
|Homepage|Logout link|Click|Redirects to confirm signout page|yes|
|Homepage|Confirm logout|Click 'ok'|Redirects to home page|yes|
|Homepage|Login link|Click|Redirects to Sign In Page|yes|
|Homepage|Register link|Click|Redirects to Sign Up Page|yes|
|Homepage|Message on login|Login as user|Successful Signin message appears|yes|
|Homepage|Message on logout|Logout|Successful SignOut message appears|yes|
|Homepage|Flight board|Look at flights table|Shows the departures for Heathrow|yes|
|Homepage|Flight details|Click on a flight|Shows you the flight details, and passenger form|yes|
|Homepage|Expand flight board button|Tap on the button next to a flight (tablets/mobile only)|Show more details about the flight|yes|
|Homepage|Expand flight board button|Tap on the button next to an expanded flight|shrinks that info|yes|
|Homepage|Expand flight board button|Tap on the button next to a flight whilst another is already expanded|shrinks previously opened flight|yes|
|Login Page|Username validation|Enter incorrect username|Error message response - does not specify if username or password failed|yes|
|Login Page|Password validation|Enter incorrect password|Error message response - does not specify if username or password failed|yes|
|Login Page|Remember me button|Checkbox on|Close browser window and reopen - user still logged in|yes|
|Login Page|Sign in button|Click|Redirects to home page, shows successful login message|yes|
|Logout Confirm Page|Sign Out button|Click|Redirects to home page, user logged out|yes|
|Register Page|Reroute to login page|Click "sign up" link|Redirects to login page|yes|
|Register Page|Username validation|Try using existing username|Error message appears - 'A user with that username already exists'|yes|
|Register Page|email validation|Entered invalid email (without '@')|Prevents registering until you enter a valid email address|yes|
|Register Page|password1|Enter a short password|Error message - 'That password is too short'|yes|
|Register Page|password2|Enter different password to password1 field|Error message - 'You must type the same password each time'|yes|
|Register Page|Sign Up button|Entered valid form data|Redirects to home page - success message displayed|yes|
|Flight Detail|First Name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Flight Detail|Last Name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Flight Detail|Dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Flight Detail|Form success|Fill form, click "Book this Flight", Confirm success in "My Booking"|Flight is booked with the one passenger|yes|
|My Booking|No Bookings|Click "My Booking" when you have no flights booked|Displays nothing, except to prompt you to make a booking|yes|
|My Booking|Booking Details|Click "Booking Details" on any booking|Takes you to that correct booking|yes|
|My Booking|Booking date order|Have multiple bookings, and go to "My Booking" page|There are multiple bookings, ordered by date with most recent at the top|yes|
|Booking Passengers|Passengers|Look at the page|The booking is the correct one, and has the passenger details we submitted|yes|
|Booking Passengers|Edit Passenger, first name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Booking Passengers|Edit Passenger, last name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Booking Passengers|Edit Passenger, dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Booking Passengers|Edit Passenger|Edit the passenger details, like name or dietary, and click "Update Customer info"|Stays on same page, message to confirm change was made. Can view change was successful for that passenger|yes|
|Booking Passengers|Add Passenger, first name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Booking Passengers|Add Passenger, last name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Booking Passengers|Add Passenger, dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Booking Passengers|Add Passenger|Add a new passenger|Stays on same page, message to confirm passenger was added. Can view passenger was added successfully.|yes|
|Booking Passengers|Delete Passenger|Cancel delete process|Passenger isn't deleted, page doesn't refresh/redirect|yes|
|Booking Passengers|Delete Passenger|Proceed with delete process|Stays on same page, passenger is deleted, message to notify user. Can see passenger is gone from booking|yes|
|Booking Passengers|Delete Booking|Cancel delete process|Booking isn't deleted, page doesn't refresh/redirect|yes|
|Booking Passengers|Delete Booking|Proceed with delete process|Redirect to "My Booking", message to user to confirm delete. Can see booking gone from "My Booking" page|yes|
|Booking Passengers|Access Control|Change the URL to another booking id|You are prompted to login as the correct user for this page. You are never confirmed if the booking/user exists|yes, 404|
|Admin|Access Control|Home page, append url with "/admin"|You are prompted to login|yes|
|Admin|Access Control|Home page and logged in as a user, append url with "/admin"|You are prompted to login as an admin, and told your current login doesn't have the credentials|yes|

[Back to Contents](#Contents)

# Use of AI
## Code Creation
I utilised AI in helping with the initial fields and tables needed for a flight booking database, after that I was able to make some modifications myself and finialise with tutors. AI here helped me to expedite the initial database structure, saving time and thought on theorising what fields and tables I might initially need, and allow me to focus on refinement rather than initial design.

I also used AI to help me create a django template language loop that could alternate between different background colours for each row. I did not know how to do this in the templating language, however the AI was able to create a modulo function in the index.html page, as well as using cycle to alternate for each iteration of the tables in my_bookings.html. AI here meant I could discover new functionality that is available to me, without having to trawl through the documentation to find the name of something that might help. Once the AI prompted me that something that could solve my table alternating colours problem existed, I could then go to the Django template language documents to customise and throughly utilise what the AI drew my attention to.

## Debugging
AI was vital during debugging. If I didn't understand what a terminal or webpage error was, copilot was there to explain it to me. If I needed then solutions, I would ask the AI for help on a problem, and prompt them to ask me questions to further refine my prompt. This led to concise and correct answers to my problems from the AI, allowing me to continue my developement and learn without having a nasty lengthy roadblock.

Another use was if the AI couldn't provide an answer, it equipped me with the full diagnosis, so I could search through documentation myself, or where time was tight ask a tutor with concise and specific query. This led to prompt responses from my tutors and saved on their valuable time.

Specific use case were with solving; Bootstrap styling bugs, and url reverse strings.

## Performance and User Experience
This is where I struggled to use AI, as it often came back to me with inefficient code. However I did find AI useful during the user experience development, where I could prompts and recieve suggestions. Or better yet, iterate through several mock ups or renditions. This accelerated the design and prototype process considerably.

## Automated test units
I did manual testing here, AI was not used for this.

I could have used AI for my test case statements, however I was comfortable with writing these as I have had SVT and QA experience previously in the tech sector.

## Workflow
As mentioned previously in these other AI topics, I mostly used AI to rapidly discover new functionality within the languages, or to debug my code. Where it could not do this, AI was able to give me succinct information I could use for my own learning and discovery, or to pass onto tutors who could then promptly help with my problems. I was comfortable with coding, however there were times when I was unfamiliar of terminology and didn't know how to respond to a tutors question, another advantage to AI where it could save me some embarassing questions!

Ultimately, AI helped keep me to my timelines and within the confines of my sprints. It enabled me to pick up on unknown functionality of languages and use them in a limited but specific way I needed for this project.

[Back to Contents](#Contents)

# Credits 
The Codestar Blog project I used for my initial javascript functions for edit and delete buttons, as well as the starting template for base.html, and initial code structure for the views, before I heavily modified them for my own use/needs.

[Codestar Blog](https://github.com/Code-Institute-Solutions/blog/tree/main/15_testing)

---

As mentioned previously, the space shuttle and airplane images that I used for my colour palattes.

Pexels Space Shuttle image author: [Kristina Paukshtite](https://www.pexels.com/@kpaukshtite/)

Pexels Airplane image author: [Allan Carvalho](https://www.pexels.com/@allan-carvalho-264847051/)

---

Logo was generated by Deep AI, with prompts being inspired by the Allan Carvalho image of the airplane at an angle.

[DeepAI](https://deepai.org/machine-learning-model/logo-generator)

---

My database relationship diagram was drawn using dbdiagram.io

[DBDiagram.IO](https://dbdiagram.io/home/)

---

My User Flow diagram was created with Miro, using a User Flow template

[Miro User Flow template](https://miro.com/templates/user-flow/)

---

The favicon was generated from a fontawesome icon using the FontIcon tool.

[FontIcon - favicon fontawesome tool](https://gauger.io/fonticon/)

---

# Acknowledgements
I would like to thank; Mathew Isherwood, Aaron Ibbotson, Hannah Mooney, and David Coles, for their help and moral support through this project.

Another thanks to our facilitator and mentor, Alexander Tastad, who helped bring our hopes us and encourage us all through our projects.

A special thanks to my tutors; Kevin Loughrey, John Rearden, and Ruairidh MacArthur. They helped me throughout the project, especially when AI and Google could provide no suitable answers. :D