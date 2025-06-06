# WANGERS

![Wangers](static/documentation/wangers.jpg)
Link to Live Site: [Wangers Website](https://wangers-d543b0386356.herokuapp.com/)

## Index - Table of Contents
* [Introduction](#introduction)
* [User Experience (UX)](#user-experience-ux) 
    * [Site Goals](#site-goals) 
* [Design](#design)
    * [Colour](#colour)
    * [Fonts](#fonts)
    * [Background](#background-image)
    * [Wireframes](#wireframes)
    * [Database Design](#database-design-and-erd)
* [Features](#features)
    * [Logo & Navigation bar](#logo-and-navigation-bar)
    * [Home Page](#home-page)
    * [Menu Page](#menu-page)
    * [Menu Item Detail Page](#menu-item-detail-page)
    * [Review List Page](#review-list-page)
    * [Review Form Page](#review-form-page)
    * [Contact Us Page](#contact-us-page)
    * [Admin Menu Management Pages](#admin-menu-management-pages)
    * [Profile Page](#profile-page)
    * [User Authentication Pages](#user-authentication-pages)
    * [Future Features](#future-features)
* [Marketing & SEO](#marketing--seo)
* [Agile Methodology](#agile-methodology)
* [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)
* [Testing](#testing)
* [Deployment](#deployment)
    * [PostgreSQL Setup](#postgresql-setup)
    * [How This Site Was Deployed](#how-this-site-was-deployed)
    * [How to Clone The Repository](#how-to-clone-the-repository)
* [Credits](#credits)
    * [Photos](#photos)
    * [Code](#code)


## Introduction
The Wangers website is designed as a flavorful destination for chicken wing lovers craving bold, saucy, and crispy delights.

This site serves two main purposes. First, it showcases our mouthwatering menu and irresistible deals to entice new customers to order from Wangers. Second, it provides a smooth, user-friendly platform for customers to place orders, select pickup or delivery, leave reviews and track their order history — making wing cravings easier to satisfy than ever.

As a whole, the site targets wing enthusiasts looking for convenient access to fresh, delicious wings with a side of humor and bold flavor.

## User Experience (UX)

### Site Goals

#### Site Owner Goals

As the site owner, I want to create a website that:
1. is visually bold and on-brand with Wangers’ fun, flavorful identity.  
2. is easy to navigate so customers can quickly find what they need.  
3. showcases our menu in a way that drives online orders and builds customer loyalty.
4. is secure and allows for an easy checkout process for our customers.   

#### User Goals

As a First-Time user I want to:
1. quickly understand what Wangers offers. 
2. easily find key info like menu options, locations, and hours.  
3. be able to check out without an account.
4. easily register for an account if I desire. 

As a Returning User I want to:
1. be able to quickly log in.
2. be able to view my previous orders. 
3. be able to leave a review.
4. easily submit a new order, and receive confirmation that it was successful. 


## Design

### Colour
The Wangers website uses a bold, orange-forward color scheme that reflects the fiery personality of the brand. The dominant shade of orange evokes the color of a flame — a perfect nod to the heat and spice of our signature buffalo wings.

This vibrant color not only grabs attention, but also reinforces the fun, high-energy feel of Wangers. Orange is used strategically throughout the site to highlight key buttons and calls to action, making navigation intuitive and eye-catching. Combined with black, white, and minimal neutral tones, the overall look keeps things clean while letting the brand's personality — and food — shine through.

### Fonts
Google Fonts was used to import the Lato font. Lato was chosen for its clean, modern look that balances readability with personality. Its rounded, friendly feel pairs well with Wangers’ bold and approachable brand voice.

Lato helps maintain a professional appearance while still feeling fresh and energetic.

### Background Image
A background image featuring a plate of crispy, golden chicken wings is used consistently across all pages of the site (with the exception of the homepage where the same image is used as the hero image with call to action button overlay). This visually reinforces the brand’s identity and keeps the focus on what matters most — the wings. 

The mouthwatering image not only sets the tone for the overall experience but also helps create an appetizing and immersive feel for visitors as they browse the site.

### Wireframes

The  wireframes were created in Balsamiq to outline the basic structure of the site. These wireframes were kept simple, reflecting a clean professional minimalist design approach.

<details><summary>Home Page</summary>
<img src="media/readme/wireframes/home.png">
<img src="media/readme/wireframes/home_tablet.png">
<img src="media/readme/wireframes/home_mobile.png">
</details>
<details><summary>Menu Page</summary>
<img src="media/readme/wireframes/menu.png">
<img src="media/readme/wireframes/menu_tablet.png">
</details>
<details><summary>Menu Detail Page</summary>
<img src="media/readme/wireframes/menu_detail.png">
<img src="media/readme/wireframes/menu_detail_tablet.png">
</details>
<details><summary>Review List Page</summary>
<img src="media/readme/wireframes/reviews.png">
<img src="media/readme/wireframes/reviews_tablet.png">
</details>
<details><summary>Review Form Page</summary>
<img src="media/readme/wireframes/review_form.png">
<img src="media/readme/wireframes/review_form_tablet.png">
</details>
<details><summary>Contact Page</summary>
<img src="media/readme/wireframes/contact.png">
<img src="media/readme/wireframes/contact_tablet.png">
</details>
<details><summary>Profile Page</summary>
<img src="media/readme/wireframes/my_profile.png">
<img src="media/readme/wireframes/my_profile_tablet.png">
</details>
<details><summary>Admin Menu Management Page </summary>
<img src="media/readme/wireframes/menu_management.png">
<img src="media/readme/wireframes/menu_management_tablet.png">
</details>


### Database Design and ERD
The databse for the  ***Wangers Website** is designed to efficiently manage customer orders, menu items, sauces, add ons, mailing lists, and user profiles while ensuring flexibility for future development.

The core entities in the database include:

- Users: Users are linked to their respective meal orders.
- 
- 
- 
- 
- 

This relational structure ensures data integrity and allows for efficient retrieval of menu items, optional extras, current & past orders, and dietary restrictions. 

<img src="static/documentation/ERD.jpeg">


## Features

### Logo and Navigation Bar
-
-
-
-
-
- The navigation bar is fully responsive on all screen sizes and collapses to a toggler on smaller screen sizes for ease of use.

<img src="static/documentation/features/navbar.jpg">
<img src="static/documentation/features/navbar_loggedin.jpg">
<img src="static/documentation/features/navbar_collapsed.jpg">

### Home Page
- The Home page conatins a hero image and text overlay that clearly communicates the purpose of the website.
- A button stating "Order Now" is also included in the text overlay as a call to action for the user. This serves as a quick link to the Menu page where users can easily view menu items and add them to their cart for purchase. 

<img src="static/documentation/features/hero.jpg">

- Below the hero image is a small section with some basic information about the company and a few key points to help sell our services. The text is black on a white background for simplicity and a clean look. 

- Below the information section is a final section where users can sign up for a newsletter. It is a simple form with one form field allowing for a quick easy sign up. 

<img src="static/documentation/features/homepage.jpg">

### Menu Page
- 
-


<img src="static/documentation/features/menu.jpg">

### Menu Detial Page
- 
-


<img src="static/documentation/features/menu.jpg">


### User Authentication Pages
- The site contains three main user authentication pages: Registration, Log In, and Log Out.
- They are all styled consistently in a black and white theme.
- They all have sumbission buttons that are styled with the same bold orange color that is seen throughout the site.  
- The sign out feature also contains a buffer page to confirm the user's desire to sign out of their account. 

<img src="static/documentation/features/register.jpg">
<img src="static/documentation/features/sign_in.jpg">
<img src="static/documentation/features/sign_out.jpg">

### Profile Page
- The profile page contains a form where users are able to manipulate backend user data from the portal, including default delivery information. This information can also be updated via a safe information checkbox on the checkout page. 

<img src="static/documentation/features/profile_html.jpg">

### Contact/Feeback Page
- The contact page conatins a form that will allow the user to send an email to the admin team. It is paired with both a confirmation email and a website pop up to inform the user that their message has been submitted. 

<img src="static/documentation/features/contact_html.jpg">

### User Feedback Messages
- Feedback messages are present throughout the site to confirm to a user that they were successful in signing in, signing out, placing an order, updating an order, updating their profile, etc. 

### Future Features
1.  


## Marketing & SEO
For detailed Mareting & SEO research, refer to the [Marketing Documentation](MARKETING.md)


## Agile Methodology

This project was developed using the AGILE Methodology, a [Project Kanban Board](https://github.com/users/MichelleDuda/projects/6), and [Project Milestones](https://github.com/MichelleDuda/wangers-pp5/milestones). This approach helped to create a systematic approach to building my site while allowing for flexibility for priority based decision making. 

In order to effectively manage the development, I utilized GitHub Projects, and was able to break tasks down into user stories for better manageability. As the issues were addressed they were moved from the to-do list to the in progress section, where commit messages were tied to them before they were closed out after the features were tested and deployed. 



## Technologies Used


### Languages
- HTML
- CSS
- Javascript
- Python

### Frameworks, Libraries & Programs Used
- [Heruko](https://www.heroku.com/) was used to deploy this project.
- [Visual Studio](https://code.visualstudio.com/) was the local IDE utilized for development. 
- [GitHub](https://github.com/) was used for version control and code hosting.
- [Google Fonts](https://fonts.google.com) was used for the fonts: Oswald and Lato.
- [Font Awesome](https://fontawesome.com/) was used for various icons in the footer and headings of the pages. 
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Lucid Chart](https://www.lucidchart.com/) was used to creat the Entity Relationship Diagram
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [CSS-Valitador](#https://jigsaw.w3.org/css-validator/) was used for CSS validation
- [W3C](https://validator.w3.org/) was used for HTML validation
- PostgreSQL
- [Django](https://www.djangoproject.com/) was used as the backend framework.
- Bootstrap
- Django AllAuth
- OAuthLib

## Testing
For detailed testing results, refer to the [Testing Documentation](TESTING.md)

## Deployment

### PostgreSQL Setup
1. Create a New Database Instance
2. Retrieve Database URL from your account dashboard.
3. Store the Database URL in env.py file as follows:
        import os
        os.environ["DATABASE_URL"] = "<your_postgres_connection_url>"
4. Ensure your env.py file is in gitignore
5. Add DATABASE_URL to Heroku Config Vars by navigating to Settings>Reveal Config Vars and adding:  
    - Key: `DATABASE_URL`  
    - Value: `<your_postgres_connection_url>`  

### How This Site Was Deployed
This site was deployed via Heroku.
1. Log into Heroku (https://www.heroku.com).
2. Click on Create 'New App' button.
3. Name the app & choose your region. Click 'Create App' button.
4. Go to the Settings Tab.
5. In the Config Vars section, click 'Reveal Config Vars' button.
  - Enter DATABASE_URL in the key field and enter the actual URL in the value field. Then click 'Add' button.
  - Enter SECRET_KEY in the key field and enter the actual secret key in the value field. Then click 'Add' button.
  - ENTER USE_AWS in the key field and enter True in the value field. Then click 'Add' button.
  - Repeat for all variables in the env.py file.
6. Go to the Deploy Tab.
7. Select GitHub in the Deployment Method section.
8. Confirm to connect to GitHub.
9. Search for repository name and click Connect.
10. Make sure branch is set to main and click 'Deploy Branch' button in Manual Deploy section. .

### How to Clone the Repository

To Clone this repository:
1. Navigate to [https://github.com/MichelleDuda/wangers-pp5](https://github.com/MichelleDuda/wangers-pp5).
2. Click on the "<> Code" button.
3. Copy the URL for the repository using HTTPS, SSH, or GitHub CLI. 
4. Open Git Bash.
5. Change the working directory to the location you want to clone the directory to. 
6. Type git clone and paste the URL that was copied earlier. 
7. Press Enter to begin the clone process. 



## Credits

### Photos
1. [hero.webp](https://www.pexels.com/photo/salmon-dish-with-vegetables-1516415/) by Valeria Boltneva from Pexels. 



### Code

1. [TabletoMarkdown.com](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/) was used to convert my additional manual testing table from an excel spreadsheet to markdown.
2. [Djano Documentation](https://docs.djangoproject.com/en/5.1/intro/) was used extensively to create various componenets of this project. 
3. [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used extensively to create various componenets of this project. 
