# GreenSeed
![Screenshot of  website](static/image/screenshots/home-index.png)
Welcome to GreenSeed, the premier online destination for all of your plant-related needs. At GreenSeed, we are passionate about bringing nature into people's lives and helping them create their own little corner of the world.

Founded over a decade ago, GreenSeed has grown from a small brick and mortar shop into a major player in the world of e-commerce. As a B2C company, our focus is on providing an exceptional shopping experience for our customers.

At GreenSeed, we offer a wide range of products, including everything from seeds to fully grown plants, as well as a variety of plant accessories. With hundreds of plants from around the globe, we have something for everyone, no matter what your style or space.

But GreenSeed is more than just an online shop. We are also committed to sustainability and social responsibility. We use the latest technology in our production process to minimize our environmental impact, and we prioritize sustainable practices in all aspects of our business.

In addition, we are proud to support the GreenSeed Foundation, which sponsors research in renewable technologies and actively drives reforestation efforts in endangered areas around the globe.

So why wait? Start exploring the world of plants today with GreenSeed. We can't wait to help you bring a little bit of nature into your life.


## Project Description
GreenSeed is a full-featured e-commerce platform for buying and selling all kinds of plants and accessories. Built with Django and Bootstrap, it offers a sleek and intuitive interface for browsing and purchasing products.

Features

* Search: Easily find what you're looking for with our powerful search feature.

* Product grouping and filtering: Find the perfect plant or accessory using our advanced filtering options.

* Checkout: Check out securely using Stripe payments.

* My account page: Manage your orders and account information from a single location.

* Cart: Keep track of the items you want to purchase and adjust quantities as needed.

* Custom admin interface: 
Easily manage your store's products and orders with our custom-built admin interface.

* Role-based authentication: Protect your store with user roles and permissions.

* And more..

### Technical Details

Intent: To create an e-commerce platform for plant enthusiasts to easily buy a wide variety of plants and accessories.

Data: Data privacy is a top priority for us. We use all-auth for authentication and Stripe for payment processing to ensure the security of our customers' personal and financial information.

Security: Our platform implements security measures to ensure the protection of our customers' data. By using all-auth for authentication and Stripe for payment processing, we guarantee the security of all transactions on our platform.


### View the live preview [here](https://greenseed-azelliott.herokuapp.com/)
(NOTE: Hold Ctrl and click the link to open in new tab)

## Table of content: 
 - [Project Description](#project-description)
 - [Look and Color Scheme](#look-and-color-scheme)
 - [Technologies Used](#technologies-used)
 - [Deployment](#deployment)
 - [Features](#features)



## Look and Color Scheme
GreenSeed's color scheme is designed to evoke the natural world and promote a sense of serenity and calm. The main colors used on the site are shades of green and terracotta, with accents of woody and earthy tones.

The top of the site features a vibrant shade of green, which gradually becomes darker and more woody as you scroll down the page. This color transition is meant to mimic the natural progression from the top of a tree down to its roots.

In addition to the main colors, GreenSeed also uses wavy, organic lines to add a sense of movement and liveliness to the site. These lines are meant to evoke the growth and motion of plants, and help to create a cohesive, natural aesthetic.

Overall, the color scheme of GreenSeed is meant to convey the company's commitment to nature and sustainability, while also providing a visually appealing and calming shopping experience for customers.

## Technologies Used

### Core Technologies
This project is built with the following technologies:

* [Django](https://www.djangoproject.com/) 4.1.3 - A web framework for Python
* [Bootstrap](https://getbootstrap.com/) 5.1.3 - A CSS framework for styling and layout
* [PostgreSQL](https://www.postgresql.org/) - Database Engine
* [Stripe](https://stripe.com/) - Payment System

## Deployment

These instructions will get you a copy of GreenSeed up and running on your local machine for development and testing purposes.

### Prerequisites
* Python 3.6 or higher
* Django 3.0 or higher
* PostgreSQL

### Installation


Clone the repository
```
git clone https://github.com/[YOUR_USERNAME]/greenseed.git
```

Navigate to the project directory:
```
cd greenseed
```

Install the dependencies:
```
pip install -r requirements.txt
```

Create a PostgreSQL database and user for the project.

Create a .env file in the root directory and set the following environment variables:

```
DATABASE_URL=postgres://[USERNAME]:[PASSWORD]@localhost:5432/[DATABASE_NAME]
STRIPE_PUBLISHABLE_KEY=[YOUR_STRIPE_PUBLISHABLE_KEY]
STRIPE_SECRET_KEY=[YOUR_STRIPE_SECRET_KEY]
```

Run the migrations:
```
./manage.py migrate
```

Start the development server:
```
./manage.py runserver
```

Open the site at http://localhost:8000.

#### Gitpod

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

```
python3 -m http.server
```

A blue button should appear to click: Make Public,

Another blue button should appear to click: Open Browser.

To run a backend Python file, type python3 app.py, if your Python file is named app.py of course.

A blue button should appear to click: Make Public,

Another blue button should appear to click: Open Browser.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the sudo command in the terminal.


## Features

### Overview


### Home


![Screenshot of GreenSeed website](static/image/screenshots/home-index.png)

### Our Plants


![Screenshot of GreenSeed website](static/image/screenshots/home-our_plants.png)

### About Us


![Screenshot of GreenSeed website](static/image/screenshots/home-about_us.png)


### Contact


![Screenshot of GreenSeed website](static/image/screenshots/home-contact.png)

### Shop


![Screenshot of GreenSeed website](static/image/screenshots/shop-main.png)
![Screenshot of GreenSeed website](static/image/screenshots/shop-main_2.png)



## Testing and Validation

### OS and Browser tests
This project has been tested on the following operating systems and browsers:

* Windows 10 
   - Chrome ver.108.0.5359.98
   - Firefox ver.107.0.1
* Fedora Silverblue Linux 
   - Chrome ver.108.0.5359.98
   - Firefox ver.107.0.1
* iPad OS on iPad Air 
   - Safari ver.16.1
* Android
   - Vivaldi ver.5.5.2805.50

### Unit Testing
Each app has it's own app_name/test repo folder. 




Site images found on [Unsplash](https://unsplash.com/)