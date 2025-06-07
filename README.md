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

<img src="media/readme/color_palette.png">

### Fonts
Google Fonts was used to import the Lato font. Lato was chosen for its clean, modern look that balances readability with personality. Its rounded, friendly feel pairs well with Wangers’ bold and approachable brand voice.

Lato helps maintain a professional appearance while still feeling fresh and energetic.

### Background Image
A background image featuring a plate of crispy, golden chicken wings is used consistently across all pages of the site (with the exception of the homepage where the same image is used as the hero image with call to action button overlay). This visually reinforces the brand’s identity and keeps the focus on what matters most — the wings. 

The mouthwatering image not only sets the tone for the overall experience but also helps create an appetizing and immersive feel for visitors as they browse the site.

<img src="media/hero.webp" width="50%">

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

- A simple and interactive Logo and Navigation Bar are located at the top of each page.
- The Logo links back to the homepage from any page throughout the site as this is a behaviour that would be expected by the user.
- The navigation bar is located in the same position on each page and provides links to various pages of the website.
- The navigation bar contains a Cart Icon with a dymanically updting order total so users can easily see how much they are going to spend. 
- A My Account icon is available in the navbar at all times, containing a dropdown that changes based on a user's authentication status.
    - If an unauthenticatied user is visiting the site, the dropdown provides access to the Log In & Registration Pages.
    - If a user is authenticated, the dropdown provides access to the My Profile page and a Sign Out option.
    - If a user is authenticated as a superuser, the dropdown additionally provides access to Menu Management pages. 
- The page that the user is actively using is underlined in the navigation bar to provide a clear view of which page they are currently on. Animation is used on the underline to provide a playful visual experience for the user. 
- The navigation bar is fully responsive on all screen sizes and collapses to a toggler on smaller screen sizes for ease of use.

<img src="media/readme/navbar.jpg">
<img src="media/readme/navbar_tablet.jpg">
    <details><summary>My Account Detail Views</summary>
        <img src="media/readme/navbar_logged_in.jpg">
        <img src="media/readme/navbar_logged_out.jpg">
    </details>


### Home Page
- The Home page conatins a hero image and text overlay that clearly communicates the purpose of the website.
- A button stating "Order Now" is also included in the text overlay as a call to action for the user. This serves as a quick link to the Menu page where users can easily view menu items and add them to their cart for purchase. 

<img src="media/readme/hero_ss.jpg">

- Below the hero image is a small section with some basic information about the company and a few key points to help sell our services. The text is black on a white background for simplicity and a clean look. 

- Below the information section is a final section where users can sign up for a newsletter. It is a simple form with one form field allowing for a quick easy sign up. 

<img src="media/readme/home_ss.jpg">

### Menu Page
- The Menu Page renders all menu items by default and sorts them based on their category into appropriate subheadings. 
- Each item card contains an image of the item, name, and price.
- If a superuser is logged in, the page also contains links to edit and delete the menu items. 
- A search and filter feature have been implemented to help users find what they are looking for more easily as the menu grows in size. 


<img src="media/readme/menu_ss.jpg">

### Menu Detial Page
- The Menu Detail page is where users can add items to their cart. 
- Users will be directed to this page after clicking on a specific item on the Menu page.
- All relevant information about the item is listed here including name, image,description, price, and dietary information.
- Features are availble here to add a Sauce and any relevant Add-Ons, as well as adjust the quantity desired before adding to the Cart.
- There are both Add to Cart and Keep Shopping Buttons at the bottom of the screen for easy navigation. 


<img src="media/readme/menu_detail_ss.jpg">


### User Authentication Pages
- The site contains three main user authentication pages: Registration, Log In, and Log Out.
- They are all styled consistently in a black and white theme.
- They all have sumbission buttons that are styled with the same bold orange color that is seen throughout the site.  
- The sign out feature also contains a buffer page to confirm the user's desire to sign out of their account. 

<img src="media/readme/register_ss.jpg">
<img src="media/readme/login_ss.jpg">
<img src="media/readme/signout_ss.jpg">

### Profile Page
- The profile page contains a form where users are able to manipulate backend user data from the portal, including default delivery information. This information can also be updated via the checkout page.
- The profile page also contains a list of past orders. 

<img src="media/readme/profile_ss.jpg">

### User Reviews Page
- The review page contains a list of all user reviews.
- Search and filter functionality exists so users can find reviews containing specific keywords or linked to a specific menu item.
- There is a like feature implemeneted so authenticated users can interact with the reviews. 
- A button at the bottom of the review page directs users to another page where they can submit a review of their own. 

<img src="media/readme/reviews_ss.jpg">
<img src="media/readme/review_form_ss.jpg">

### Contact/Feeback Page
- The contact page conatins a form that will allow the user to send an email to the admin team. It is paired with both a confirmation email and a website pop up to inform the user that their message has been submitted. 

<img src="media/readme/contact_ss.jpg">

### User Feedback Messages
- Feedback messages are present throughout the site to confirm to a user that they were successful in signing in, signing out, placing an order, updating an order, updating their profile, etc. 

### Future Features
1.  Special Offers & Discounts - A section containing special offers can be used to feature meal deals, game day specials, as well as other coupons and promotions to entice users to order. 

2. Loyalty Reward Program - Another feature can be added to the profile section to track reward points based on users past orders and provide them with free items or money off orders when they reach a certain threshold. 


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
- [Google Fonts](https://fonts.google.com) was used for the fonts: Lato.
- [Font Awesome](https://fontawesome.com/) was used for various icons in the footer and headings of the pages. 
- [Balsamiq](https://balsamiq.com/) was used to create the wireframes.
- [Lucid Chart](https://www.lucidchart.com/) was used to creat the Entity Relationship Diagram
- [CI Python Linter](https://pep8ci.herokuapp.com/)
- [CSS-Valitador](#https://jigsaw.w3.org/css-validator/) was used for CSS validation
- [W3C](https://validator.w3.org/) was used for HTML validation
- PostgreSQL
- [Django](https://www.djangoproject.com/) was used as the backend framework.
- [Bootstrap](https://getbootstrap.com/) was used for responsive front-end styling and layout.  
- [Django Allauth](https://django-allauth.readthedocs.io/en/latest/) was used for user authentication and registration.  
- [OAuthLib](https://oauthlib.readthedocs.io/en/latest/) was used to support OAuth-based authentication flows.  
- [AWS (Amazon Web Services)](https://aws.amazon.com/) was used to host static and media files via AWS S3.  
- [Stripe](https://stripe.com/) was used to handle secure online payment processing. 
- [Django-Crispy-Forms](https://django-crispy-forms.readthedocs.io/en/latest/) – Used to render Django forms elegantly with minimal code.  
- [Gunicorn](https://gunicorn.org/) – A WSGI HTTP server for deploying the Django app on Heroku.  
- [Pillow](https://python-pillow.org/) – Python Imaging Library used for image handling (e.g., profile pictures, product images).   
- [Django-Storages](https://django-storages.readthedocs.io/en/latest/) – Manages media and static file storage via AWS S3.  


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
2. [Buffalo Chicken Wrap](https://www.pexels.com/photo/close-up-shot-of-shawarma-6416559/) by rajdeepcraft from Pexels.  
3. [Apple Pie](https://www.pexels.com/photo/sliced-bread-on-white-ceramic-plate-6148194/) by ROMAN ODINTSOV from Pexels.  
4. [Glass of Milk (Facebook page)](https://www.pexels.com/photo/grayscale-photography-of-glass-of-milk-2198626/) by Alexas Fotos from Pexels.  
5. [Hot Sauce (Facebook)](https://www.pexels.com/photo/red-and-orange-soup-in-a-bowl-on-the-wooden-table-top-5737247/) by RDNE Stock project from Pexels.  
6. Fire tongue (Facebook) — Image created with AI using OpenAI’s DALL·E.  
7. [Facebook Photo](https://www.pexels.com/photo/close-up-on-meat-and-carrot-on-tray-10303259/) by Юлия Чалова from Pexels.  
8. [Facebook Photo](https://www.pexels.com/photo/person-holding-barbecue-chicken-with-white-sauce-12087946/) by Leslie Torres from Pexels.  
9. [Facebook Photo](https://www.pexels.com/photo/wild-wings-wings-photography-27645102/) by Zain Ali from Pexels.  
10. [Chicken Wings with White Sauce](https://www.pexels.com/photo/fried-chicken-legs-in-sweet-glaze-10361458/) by Mohamad Sadek from Pexels.  
11. [Chicken Wings with Dipping Sauce](https://www.pexels.com/photo/meat-with-sauce-24182618/) by Sergio Arreola from Pexels.  
12. [Camera Illustration (for no image file)](https://unsplash.com/illustrations/a-drawing-of-a-camera-on-a-white-background-p_Lvm8TJCZI) by Round Icons on Unsplash.  
13. [Bone-in Wings](https://unsplash.com/photos/fried-chicken-on-black-plate-R-7_ErUOLxw?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) by [Scott Eckersley](https://unsplash.com/@scotteckersley?utm_content=creditCopyText&utm_medium=referral&utm_source=unsplash) on Unsplash.  
14. [Boneless Wings](https://www.pexels.com/photo/a-box-with-fried-chicken-in-it-and-a-dipping-sauce-15029888/) by Shameel Mukkath from Pexels.  
15. [Vegan Buffalo Wings](https://www.pexels.com/photo/cooked-food-on-a-red-tray-5215873/) by Rodrigo Morelos Oseguera from Pexels.  
16. [Fried Chicken Sandwich](https://www.pexels.com/photo/a-chicken-burger-in-close-up-photography-7963144/) by Erwin Quintana from Pexels.  
17. [Chicken Wrap](https://www.pexels.com/photo/close-up-shot-of-shawarma-6416559/) by rajdeepcraft from Pexels.   
18. [Fries](https://www.pexels.com/photo/fried-potatoes-1583884/) by Dzenina Lukac from Pexels.  
19. [Vegan Wings](https://www.pexels.com/photo/cooked-food-on-a-red-tray-5215873/) by Rodrigo Morelos Oseguera from Pexels.  
20. [Sweet Potato Fries](https://www.pexels.com/photo/fries-and-dipping-sauce-1893555/) by Valeria Boltneva from Pexels.  
21. [Facebook Page Wings](https://www.pexels.com/photo/buffalo-wings-with-sesame-seeds-and-dips-on-plastic-containers-11299734/) by Meraj Kazi from Pexels.  
22. Facebook Page Chicken Wing Vector — Image generated by ChatGPT using DALL·E by OpenAI.


### Code

1. [TabletoMarkdown.com](https://tabletomarkdown.com/convert-spreadsheet-to-markdown/) was used to convert my additional manual testing table from an excel spreadsheet to markdown.
2. [Djano Documentation](https://docs.djangoproject.com/en/5.1/intro/) was used extensively to create various componenets of this project. 
3. [Bootstrap Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/) was used extensively to create various componenets of this project.
4. Various sections of my code were modeled off the Code Institute Boutique Ado Walkthrough project. 
