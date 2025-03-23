# Flight Bookings
A flight bookings web app using Django and PostgreSQL

## Live deployment

## Product Goals

## Contents

1. [Flight Bookings](#flight-bookings)
  - 
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
  - [Manual Testing](#manual-testing)
9. [Credits](#credits)
  - [Content](#content)


# UX - User Experience

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

## Future Development

[Back to Contents](#Contents)

# Database Schema - Entity Relationship Diagram

[Back to Contents](#Contents)

# Agile Methodologies - Project Management

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

### CSS

### JavaScript

### Python

### LightHouse

### Wave Accessibility Evaluation

## Manual Testing
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
|Register Page|email validation|Entered invalid email (without '@')|Error message - 'Please enter valid email address' and registration fails|no, null email was permitted|
|Register Page|password1|Enter a short password|Error message - 'That password is too short'|yes|
|Register Page|password2|Enter different password to password1 field|Error message - 'You must type the same password each time'|yes|
|Register Page|Sign Up button|Entered valid form data|Redirects to home page - success message displayed|yes|
|Flight Detail|First Name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Flight Detail|Last Name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Flight Detail|Dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Flight Detail|Form success|Fill form, click "Book this Flight", Confirm success in "My Booking"|Flight is booked with the one passenger|yes|
|My Booking|No Bookings|Click "My Booking" when you have no flights booked|Displays nothing, except to prompt you to make a booking|partial (empty, but no prompt)|
|My Booking|Booking Details|Click "Booking Details" on any booking|Takes you to that correct booking|yes|
|My Booking|Booking date order|Have multiple bookings, and go to "My Booking" page|There are multiple bookings, ordered by date with most recent at the top|yes|
|My Booking|Access Control|Change the URL to another user id|You are prompted to login as the correct user for this page|no|
|Booking Passengers|Passengers|Look at the page|The booking is the correct one, and has the passenger details we submitted|yes|
|Booking Passengers|Edit Passenger, first name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Booking Passengers|Edit Passenger, last name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Booking Passengers|Edit Passenger, dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Booking Passengers|Edit Passenger|Edit the passenger details, like name or dietary, and click "Update Customer info"|Stays on same page, message to confirm change was made. Can view change was successful for that passenger|yes|
|Booking Passengers|Add Passenger, first name validation|leave blank|Browser requests you fill in first name field before sending form|yes|
|Booking Passengers|Add Passenger, last name validation|leave blank|Browser requests you fill in last name field before sending form|yes|
|Booking Passengers|Add Passenger, dietary validation|Exceed max length|The text box prevents you from exceeding max length|yes|
|Booking Passengers|Add Passenger|Add a new passenger|Stays on same page, message to confirm passenger was added. Can view passenger was added successfully.|partial, message says "Flight Booked successfully!"|
|Booking Passengers|Delete Passenger|Cancel delete process|Passenger isn't deleted, page doesn't refresh/redirect|yes|
|Booking Passengers|Delete Passenger|Proceed with delete process|Stays on same page, passenger is deleted, message to notify user. Can see passenger is gone from booking|yes|
|Booking Passengers|Delete Booking|Cancel delete process|Booking isn't deleted, page doesn't refresh/redirect|yes|
|Booking Passengers|Delete Booking|Proceed with delete process|Redirect to "My Booking", message to user to confirm delete. Can see booking gone from "My Booking" page|yes|
|Booking Passengers|Access Control|Change the URL to another booking id, but keep your user id|You are prompted to login as the correct user for this page. You are never confirmed if the booking/user exists|partial, 500 error|
|Booking Passengers|Access Control|Change the URL to another user id, but keep your booking id|You are prompted to login as the correct user for this page. You are never confirmed if the booking/user exists|no|
|Booking Passengers|Access Control|Change the URL to another user id, and change to a valid booking id for that user|You are prompted to login as the correct user for this page. You are never confirmed if the booking/user exists|partial, 500 error|


[Back to Contents](#Contents)

## Feature Testing

[Back to Contents](#Contents)

# Credits 

## Content 

[Back to Contents](#Contents)
