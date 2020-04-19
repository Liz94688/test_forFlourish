# Flourish At Home
_Flourish At Home_ is an app designed to provide a small family run business, currently selling houseplants within their local community, with the ability to assist and advise their customer base on basic plant care outside of the shop environment.

Following the sale of any plant, the owners of the shop will direct their customers towards _Flourish At Home_, highlighting the apps existence and advising the customer on the potential benefits of using the app, with the explanation that this service would be free to any customer purchasing a plant from their shop.

_Flourish At Home_ is designed with a local business in mind, offering a way for the business owner to effectively and efficiently communicate with their customer base, once they leave the shop.

Users registered on the _Flourish At Home_ app would also benefit, having access to specific information on every plant they have personally purchased from the shop, as well as advice provided by the local shop owner on how to care and place the plants for maximum enjoyment. 

A link to the finished website can be found [here](https://test-flourish.herokuapp.com/)


## UX
### User Stories:
#### Customers
Through research conducted during the initial design of the _Flourish At Home_ app, interviews were carried out among customers who frequently visited the shop and purchased plants. This was completed in order to establish the customer base, help in the overall design of the app and decide what services and functions were offer to registered users. 

This research helped create the user story listed below.

As a user of this kind of app, I want to be able to:

* Find any plant I end up buying from the shop
* Be able to find the plant easily - sometimes I forget the exact name of the plant, so a handy reference would be helpful
* Be provided with relevant information about the plant - aspects about the plant I'm not aware of or would find useful, like how to look after it once I’ve purchased it
* It’s always nice getting advice from the shop owners about how to care for the plant, this would be welcome in any information provided
* A record of when I purchased the plant
* The ability to add my own notes on the plant
* A clear and simple layout that provides easy access and is easy to navigation
* To be able to keep a separate record of each plant I purchase and to have these records displayed nicely
* To be allowed to edit the records I've added, every plant I’ve bought seems to have all these individual quirks, sometimes you can’t remember them all, so it’d be nice to have a place to store all of this information and be able to add to it when I wanted
* To be able to delete any record, in case I no longer need it anymore

#### Shop Owner
An interview were also conducted with the owners of the shop, asking them what functionality they would prefer to have control over in the app. The following user story was created in relation to this:

As an administrator of the app, I want to be able to complete the following:

* To be able to add new plants to the collection, easily and with as little work as possible
* To be able to delete any plants that are no longer sold by the shop
* To be able to see all of the current plants I have already added to the collection in an simple format
* To be able to see what a registered users has access to

### Wireframes
A link to photos taken of hand-drawn wireframes for the _Flourish At Home_ app can be found [here](https://afbeb705-7c1f-4b1d-bbc0-8f7bff603662.ws-eu01.gitpod.io/mini-browser/workspace/test_forFlourish/static/wireframes/IMG_0015.jpg) and [here](https://afbeb705-7c1f-4b1d-bbc0-8f7bff603662.ws-eu01.gitpod.io/mini-browser/workspace/test_forFlourish/static/wireframes/IMG_0016.jpg):

## Features

### Existing Features
#### Welcome Page
A bold and clear message inside a jumbotron welcomes the user to the _Flourish At Home_ welcome page and directs them on how to navigate through the app. 

The  name of the app is clearly defined at the top of the page and has been designed to act as an anchor point, allowing a user to click on the app name and return to the welcome page at any point throughout their journey.

Users are directed towards options at the top of the page, again, clearly displayed and easy to read, where further actions can be taken to progress through the app. The menu is easy to navigate and understand. 

Users accessing the _Flourish At Home_ app on a mobile device are able to access these options via a smart and recognisable menu icon that allows the available options to drop below the main navigation bar.

The colour scheme and design of the page represents the client’s livelihood and highlights the main purpose of the app to the user - to discover more about plants. A simple but striking image has been chosen to cement this theme and is included throughout the _Flourish At Home_ app.

#### Register Page
The same navigation bar introduced on the Welcome Page runs along the top of every other page after this - providing consistency and familiarity to the user and contributing to a positive user experience. 

The Registration Page has a similar design to the Welcome Page, again, to encourage familiarity with the user and to make the user experience enjoyable.

A form centred in the middle of the page directs the user’s eyes towards the form fields and the specific information needed from them in order to continue. The background of the form mirrors the same colour used on the navigation bar at the top of the page, again, to introduce continuity.

The form needed to be simple and easy to navigate, as such, placeholders have been included in each form field, to provide direction and clarity to the user. Fields are evenly spaced and the button to submit the user information has been designed to stand out.

Individual fields are highlighted when a user clicks on them and validators have been included to confirm the correct information is being included by the user. For example, the ‘Email’ field will not allow the user to submit the form if an email address has not been included. The user is provided with directions if form fields are not completed or completed incorrectly. This contributes to the user experience and guarantees the client and app receive the required information.

The form also includes a clear direction for any users who may have already registered an account on the app and mistakenly navigated to the Register Page. This direction, centred at the bottom of the form, navigates the user to the Login Page with a handy link stating ‘Log in here’. This has been placed here to further improve the user experience and make the registration process as simple as possible. 

Following a successful registration, the user is re-directed to the Login Page and a flash message placed directly below the navigation bar updates the user on the recent action and confirms a user account was successfully registered.

#### Login Page
The design of this page mirrors that of the Registration Page, encouraging familiarity and consistency with the user. 

The form is designed in the same way and includes the same placeholder design and validator expectations.

If a user mistakenly inputs an incorrect ‘Username’ or ‘Password’ in either form field, a flash message appears directly below the navigation bar, informing them of the mistake and re-directing the user back to the Login Page.

Users who have not registered an account are unable to progress any further, the same flash message appears and a direction has been included at the bottom of the form, with a link to the Registration Page.

#### User Account
Users are informed that their log in has been successfully completed via a flash message at the top of the screen.

The navigation bar has been altered to recognise this and options have changed from ‘Register’ and ‘Login’ to ‘My Account’ and ‘Logout’ - this is to allow ease of navigation to the user, setting clear labels for the functions available now they are logged in as a user.

There is also a function that welcomes the user by the username they registered with, adding a personal touch to the app that reflects the treatment they would receive from the local business if they had entered the shop.

Again, the colour scheme and theme continue throughout and are included on this page to encourage familiarity.

Wording is included below the welcome statement, directing users on how them can use the table to find and add their plants.

* Table of plants - Clear and concise. This provides basic information on each plant that is easily recognisable to users, as well as being easy to navigate.

The ‘Reference’ included in the first column was specifically based on the user stories collected during the design process. When buying plants in a shop, not all customers recognise the name or can recall the name after purchasing the plant. The local business has considered this and plants are paired with a memorable ‘reference’ to assist customers.

This reference is included on the plant label and receipt when it is bought in the shop. Users are made aware of this and, as such, would then be able to search for their plant using either the plant reference or plant name.

The table includes a button aligned to each plant, directing the user towards what action to take once they intend to add the plant to their own record.

* Jumbotron_ - A jumbotron provides a clear statement and explanation to the user as to where their individual plant records will be displayed, once created. 

In addition to informing the user about how plant records will be displayed, the jumbotron also provides a clear and visual separation between the function of adding a plant at the top of the page and that of displaying the plant records, located at the bottom of the page.

* Plant Records - Once created, plant records are displayed below the jumbotron. Each record includes a specific amount of information on the plant for easy user navigation, including the ‘Plant Reference’, ‘Plant Name’, a description of the plant, how often the plant needs to be watered and any notes the user has included.

‘Edit’ and ‘Delete’ buttons mirror the design of the ‘Add’ button in the Plant Table, providing continuity to the page and user. The ‘Delete’ button has also been clearly marked in an alternative ‘danger’ colour, to communicate its function and consequences to the user if actioned. 

#### Add Plant Page
The design and layout of the form mirrors those previously mentioned - Register and Login Pages - reinforcing the user’s feelings of familiarity with the app.

The first section of the form is already pre-populated with information input by the client - the local business owners running the plant shop - and includes general information about the plant, how to care for the plant and where to place the plant around the house. 

This information can only be access and updated by the Administrator.

Users are encouraged to completed alternative field on the form, including ‘Date Purchased’, ‘Water Frequency’ and Notes sections. 

* The ‘Date Purchased’ has a calendar function available to the user that appears when they enter into the field and can be access via a clearly displayed icon on the right-hand side of the field.


* The ‘Water Frequency’ field has been designed as a drop-down list that appears when the user enters into that field. A placeholder in the field directs the user to pick an option, encouraging them to click on the field initially.

* The ‘Notes’ field is designed with a multiple number of rows to allow the user to place as many notes as they wish to.

A button is included at the end of the form. Once the button has been clicked, the plant is submitted to the user’s collection and the user is re-directed to the User Account Page and a flash message appears directly underneath the navigation bar, updating the user on the successful inclusion of the plant record. The message is centred and easily recognisable to the user.

#### Edit Plant Page
This is a mirror image of the Add Plant page. The only difference is that any information previously included by the user is pre-populated in each of the form fields, ready for the user to amend or edit.

Once the button has been clicked, the plant record is updated with any new information and the user is re-directed to the User Account Page with a flash message informing them that the plant record was edited successfully.

#### Delete
This button is clearly placed and designed to stand out on each plant record. The button has been clearly marked in an alternative ‘danger’ colour, to communicate its function and consequences to the user if actioned.

Once pressed the record is immediately deleted and the user is redirected back to the User Account page.

#### Administration Only
Provides functionality to the client - the local business owner running their own plant shop - to add new plants to the collection, as well as updating all existing plant records. 

The '/add_admin' route has been designed to create a default admin user. Login in as the Administrator in the following way to navigate the Admin Only pages of the website:
* Username: admin
* Password: admin

#### Admin Acccount
This page mirrors the User Account in relation to design. The navigation bar mirrors the rest of the app, with the addition a third option for administration purposes only.

A jumbotron welcomes the administrator and guides them around the page. A button is centred at the bottom of the jumbotron and clearly displays its functionality to the administrator. 

Below this is the same table included in the User Account, styled in the same way to provide continuity to all users of the app, directing the administrator to search for any existing plants and a clearly defined button helps the administrator navigate to updating a plant record.

#### Admin Add
This page mirrors the design and layout of the ‘Add Plant’ page for the user account and includes separate fields for each piece of information collated and pre-populated in the user’s Add Plant page. 

The form has ben designed so that the administrator has to complete all of the fields before being allowed to submit the new plant. Messages appear in each field that does not hold any content, this acts as a reminder to the administrator that each field requires information for a better user experience.

#### Admin Update
This page mirrors the design and layout of the Edit Plant Page for the user account. Any information previously included by the administrator is pre-populated in each of the form fields, ready for the administrator to amend or edit.

Once the button has been clicked, the plant record is updated with any new information and the user is re-directed to the User Account Page with a flash message informing them that the plant record was edited successfully.

### Features Left to Implement
* General - Password security is not currently supported by the app - this would be a welcome addition, to assist in enhanced the apps security.

* General - a Blog or Articles Page - accessed without having to register an account, can be offered to the client as an additional element. Further advice could be given to users this way. This would also encourage client/user participation when not visiting the shop.

* User Account Page - Table in User Account - redesign as a dropdown list of some kind, or possibly pagination, as the plant records increase. Improves the user experience, tidies up the page, keeps it clear and clutter free.

* User Account Page - An ‘Information only’ route for each plant record - displaying the information already recorded by the user. This would be included so that a user can access the information in the record without having to edit it and would include a button to re-direct them back to the user_account. Improving the flow and user experience and encouraging users to visit the page just to read their records, rather than only visiting when a new plane has been purchased.

* User Account Page - Allow users to add photos to their plant records.

## Technologies Used
HTML, CSS, Javascript, Python, MongoDB

Dependancies: Flask and Flask-PyMongo

The project uses JQuery to simplify DOM manipulation.

#### Version Control System: 
Git was used to track the changes made to the site and push them to Github

#### Hosting: 
Heroku has been used to deploy the website

## Testing
### Register Form:
Go to the "Register" page
If a user tries to submit an empty form, they receive a message relating to each of the fields they need to complete - this occurs for each of the fields on the Register Form.
If the user tries to submit the form with an invalid email address, an error message appears informing the user of the error.
When the user submits the form with each of the form fields holding a valid input, the user is re-directed to the Login screen and a messages flashes up saying the registration was successful.

### Login Form:
Go to the "Login" page
If a user tries to submit an empty form, they receive a message relating to each of the fields they need to complete - this occurs for each of the fields on the Login Form.
If the user tries to submit the form with a username that has not previously been registered, an error message appears informing the user of the error.
If the user tries to submit the form with a password that does not match the username, the form is wiped and the user needs to re-start the form. 
When the user submits the form with each of the form fields holding a valid input, the user is re-directed to the User Account screen and a messages flashes up saying the login was successful.

### Add Plant Form - User:
Go to the “Add Plant" page
The pre-populated information has already pulled through to the record and cannot be amended by the user.
The user has the option to complete 3 additional fields on the form - date-purchased, water-frequency and notes.
The form can be submitted without all of these fields being completed.
Once submitted, the user is re-directed to the User Account screen and a message informs them that the plant was recorded successfully.

### Add Plant Form - Administrator:
Go to the “Admin Add" page
The administrator has to complete all of the forms fields on this form.
If the administrator tries to add a new plant without each field being completed, an error message appears, informing the administrator of the error.
When the administrator submits the form with each of the fields completed, they are re-directed to the Admin Account Page and a message tells them that the new plant was recorded successfully.

### Update Plant Form - User:
Go to the “Edit User Plant Record” page
The pre-populated information has already pulled through to the record and cannot be amended by the user.
The user has the option to edit any of the 3 additional fields on the form - date-purchased, water-frequency and notes.
The form can be submitted without all of these fields being completed or edited.
Once submitted, the user is re-directed to the User Account screen and a message informs them that the plant was edited successfully.

### Update Plant Form - Administrator:
Go to the “Admin Update” page
The information previously input by the administrator is already included in the form fields.
The administrator can update any of these fields, however, they cannot leave a field empty.
If the administrator tries to update the form with any field empty, they receive an error message informing them of the error.
When the administrator submits the form with each of the fields completed, they are re-directed to the Admin Account Page and a message tells them that the plant was edited successfully.

I completed a number of checks on each of the forms listed above - users could be registered, login and use the ‘add’ and ‘update’ forms available to them. Data was recorded correctly, stored and updated when the user completed actioned them. 

The same checks were complete on the administration user - no errors were highlighted.

I also asked a number of friends to complete the same checks on their own devices - all feedback mirrored what I had already verified.

### Additional Testing Completed:
When a user was logged into their account on Google Chrome, the route was copied from the browser and pasted into Safari, to check if the link would open. The link did not open and an error was returned.

## Deployment
The project I created was deployed to Heroku

* After registering an account in Heroku, I created a new app and named it ‘test-flourish’
* Environment variables were set in the ‘Reveal Config Vars’ section, including IP, PORT MONGO_URI, MONGO_DBNAME and SECRET_KEY
* I then connected the Heroku app to the git repository and clicked ‘Deploy Branch’
* The site was then successfully deployed

## Credits
The code for the inclusion of the background image and the code and styling for the card elements used for the individual plant records was taken from the ‘Snippets’ section of [Start Bootstrap](https://startbootstrap.com/snippets/).

The code and standard styling for the navigation bar, jumbotrons, forms, buttons, table and alerts were taken from [Bootstrap](https://getbootstrap.com/).

### General guidance from websites:
* [Code Institute](https://courses.codeinstitute.net/program/FullstackWebDeveloper)
* [Python](https://www.python.org/)
* [Jinja](https://palletsprojects.com/p/jinja/)
* [Stack Overflow](https://stackoverflow.com/)
* [w3schools.com](https://www.w3schools.com/)
* [MongoDB](https://docs.mongodb.com/manual/crud/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)

### Specific guidance from website:
* Python
Functools - guidance on creating a function decorator was found [here](https://docs.python.org/3/library/functools.html#functools.wraps)
* Flask
Decorators - guidance and code on how to create a decorator was found [here](https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/)
* Flask
Message Flashing - guidance and code on how to use found [here](https://flask.palletsprojects.com/en/1.1.x/patterns/flashing/#message-flashing-pattern)

### Media
The background photo used in this site was obtained from [Pexels](https://www.pexels.com/search/plant/).

### Acknowledgements
I received inspiration for this project from the tiny, independent, and local plant shop around the corner from where I live.

All the plant information in the website has been taken from the book ‘The Kew Gardener’s Guide to Growing House Plants’ by Kay Maguire.

Special mention goes to my mentor Guido Cecilia Garcia, for his unlimited amount of guidance and patience while working on this project, as well as helping me with the issues I had surrounding pagination.