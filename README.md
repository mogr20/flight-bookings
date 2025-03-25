# Flight Bookings
A flight bookings web app using Django and PostgreSQL

![flight app on all devices](https://github.com/user-attachments/assets/ddf52129-e8d9-49ba-8f61-9d39c713b959)

[Back to Contents](#Contents)

## Live deployment
[Flight Booking](https://mogr-flight-booking-fe5c31fca0d1.herokuapp.com/)

## Product Goals

[Back to Contents](#Contents)

## Contents

1. [Flight Bookings](#flight-bookings)
  - [Live Deployment](#live-deployment)
  - [Product Goals](#product-goals)
2. [UX/UI](#ux---user-experience)
  - 
3. [Features](#features)
  - 
4. [Database Schema - Entity Relationship Diagram](#database-schema---entity-relationship-diagram)
5. [Agile Methodologies - Project Management](#agile-methodologies---project-management)
  - [MoSCoW Prioritization](#moscow-prioritization)
6. [Deployment](#deployment)
  - [Connecting to GitHub](#connecting-to-github)
  - [Django Project Setup](#django-project-setup)
  - [Cloudinary API](#cloudinary-api)
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
  - 
10. [Credits](#credits)
  - [Content](#content)


# UX - User Experience

![User Flow](https://github.com/user-attachments/assets/5a965c7f-f6d3-4d28-a1c6-e981218acf29)

## User Stories

[Back to Contents](#Contents)

## Design Inspiration

[Back to Contents](#Contents)

### Colour Scheme

```white```  ```rgba(0, 0, 0, 0.518)```

[Back to Contents](#Contents)

### Font

## Wireframes

[Back to Contents](#Contents)

## Deployed App Screenshots

<details open>
    <summary></summary>  
    <img src="">  
    <img src="">  
    <img src="">  
</details>

<details>
    <summary></summary>  
    <img src="">  
</details>

[Back to Contents](#Contents)

# Features 

## Present Features

• **Homepage:** The user first arrives at the site on the homepage. Regardless of being logged in or not, they can see the departure board. We use alternating colours for each row to help highlight and differentiate them for ease of use for reading off a row of flight information.
From here, they can click or tap on any flight to get further details.

If the user is viewing the site from a mobile or tablet device, some of the columns will have disappeared and an expand info button appears to the right of every row.
Clicking (or tapping) this button expands the row and shows the missing information below that flight. Clicking the button again shrinks that row. Clicking a different row's button also shrinks all other rows.

If logged in, below the navbar the user is told they are logged in. Otherwise, they are informed to register or login to book a flight.

• **Flight Details:** When a user clicks (or taps) onto a flight, they are taken to the flight detail page. Here they can see the arrival information for that flight, (which is not displayed on the departure board) which is important in the decision making process of booking a flight as arrival time can be critical for meetings or opening times for venues at their destination.

Below the flight details is a passenger form. Here they can fill out one passenger and book the flight, they can specify any dietary requirements they have and choose what baggage they would like to bring.
A user will only see the passenger form if they are logged in.

Once a flight is booked, a message is displayed below the navbar confirming their booking. They can also navigate to the "My Booking" page to add more passengers or make any other changes to their booking.

• **My Booking:** This page shows the user their most recent booking first, followed by all their other bookings. Like with the homepage, a user can click (or tap) on the expand button to view the full flight details if they are on mobile or tablet.
Unlike the homepage we show the full flight information here, as we do with the flight detail page. This is because the homepage is a departure board page and should focus on the required information for a departure.

Clicking (or tapping) on a booking via the "Booking Detail" button, will send the user to a booking passengers page where they can make further changes to their booking, rather than just view their booking.

• **Booking Details** Once the user has navigated to this page, they can view all of the passengers they have on a booked flight. They can make edits to that passenger or delete them from the booking. Deleting or editing a passenger gives a message to confirm this below the navbar, as well as resending them to this page so they can confirm the changes themself.
They can also delete the entire booking. If they do this, the user is redirected to their "My Booking" page, so they can edit or view the details of another booking and again, also confirm that the booking has successfully deleted. A message regardless is also viewable below the navbar that informs the user that the booking was deleted.

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

![database schema](https://github.com/user-attachments/assets/7387a8df-bba4-49c6-ade6-b51fc522a6a3)

[Back to Contents](#Contents)

# Agile Methodologies - Project Management

[Project Board](https://github.com/users/mogr20/projects/7)

## MoSCoW Prioritization

[Back to Contents](#Contents)

# Deployment

## Cloning from GitHub

[Back to Contents](#Contents)

## Django Project Setup

[Back to Contents](#Contents)

## Cloudinary API 

[Back to Contents](#Contents)

## Heroku deployment

[Back to Contents](#Contents)

# Technologies Used

[Back to Contents](#Contents)

# Testing 
## Validator Testing 

### HTML
Passed
https://validator.w3.org/nu/

### CSS
Passed
https://jigsaw.w3.org/css-validator/

### JavaScript
Passed
https://jsvalidator.com/

### Python

### LightHouse
Above 80 in performance on mobile and across the whole site.

Index Homepage:
![index homepage](https://github.com/user-attachments/assets/c82b35b3-6034-4361-b254-17efb28442f2)
Flight Detail page:
![flight detail page](https://github.com/user-attachments/assets/f9da499e-bdf4-40cf-8c50-b8c2f5cd8a82)
My Bookings page:
![my bookings page](https://github.com/user-attachments/assets/598fdf46-11d1-42de-a1db-86a60424cb6a)
Booking Passenger page:
![booking passenger detail page](https://github.com/user-attachments/assets/8cec76ee-cc51-49cd-a2ef-3c757670d622)

[Back to Contents](#Contents)

### Wave Accessibility Evaluation
Passed
https://wave.webaim.org/

![WAVE](https://github.com/user-attachments/assets/7b8e826c-a63e-4b68-97ed-db721b7ca170)

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
1. General Debugging Assistance
Issue: Various layout and alignment issues in the app.
Steps Taken:
Provided debugging steps using browser developer tools to inspect applied styles.
Suggested isolating the issue with a simplified test case to identify conflicts.
2. Django-Specific Assistance
Issue: Redirecting to a view with reverse caused a TypeError due to incorrect arguments.
Steps Taken:
Corrected the reverse function call by wrapping the booking_id in a list or tuple to ensure it was iterable.
3. Code and Style Improvements
HTML:
Ensured proper structure for the accordion button and its child elements.
Used Bootstrap utility classes (d-flex, ms-1, align-items-center) for consistent styling.
CSS:

4. Collaboration and Iteration
Approach:
Asked targeted questions to gather context and debug effectively.
Iteratively refined solutions based on your feedback and testing results.

[Back to Contents](#Contents)

# Credits 

## Content 

[Back to Contents](#Contents)
