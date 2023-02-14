# GreenSeed
![Screenshot of  website](static/image/screenshots/home-index.png)
Welcome to GreenSeed, the premier online destination for all of your plant-related needs. At GreenSeed, we are passionate about bringing nature into people's lives and helping them create their own little corner of the world.

Founded over a decade ago, GreenSeed has grown from a small brick and mortar shop into a major player in the world of e-commerce. As a B2C company, our focus is on providing an exceptional shopping experience for our customers.

At GreenSeed, we offer a wide range of products, including everything from seeds to fully grown plants, as well as a variety of plant accessories. With hundreds of plants from around the globe, we have something for everyone, no matter what your style or space.

But GreenSeed is more than just an online shop. We are also committed to sustainability and social responsibility. We use the latest technology in our production process to minimize our environmental impact, and we prioritize sustainable practices in all aspects of our business.

In addition, we are proud to support the GreenSeed Foundation, which sponsors research in renewable technologies and actively drives reforestation efforts in endangered areas around the globe.

So why wait? Start exploring the world of plants today with GreenSeed. We can't wait to help you bring a little bit of nature into your life.

Check out our [Facebook](/documents/facebook.md) page

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

[DB Diagram](/documents/diagram.md)

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

[Wireframes](/documents/wireframes.md)

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

[Back to top](#greenseed)  

## Features

### App Overview


### Navigation and Functionality
<details>
   <summary>Home</summary>

Home page is has clean design with a button that leads to the web shop.

![Screenshot of GreenSeed website](static/image/screenshots/home-index.png)

There are several svg graphics that tell the users benefits of plants:

![Screenshot of GreenSeed website](static/image/screenshots/home-svg.png)

At the bottom there is an option to subscribe to newsletter

![Screenshot of GreenSeed website](static/image/screenshots/newsletter.png)
</details>


<details>
   <summary>Our Plants</summary>

Our plants page contains several pictures and descriptions of how the company sustainably grows and sources their plants.

![Screenshot of GreenSeed website](static/image/screenshots/home-our_plants.png)

It also contains few cards with descriptions of popular plants

![Screenshot of GreenSeed website](static/image/screenshots/plant-description.png)

</details>


<details>
   <summary>About Us</summary>

About us page contains brief history of the company, it also explains company mission and values.

![Screenshot of GreenSeed website](static/image/screenshots/home-about_us.png)

At the bottom of the page is a counter section which provides the visitors some business metrics.

![Screenshot of GreenSeed website](static/image/screenshots/about-counter.png)


</details>

<details>
   <summary>Contact</summary>

Contact page contains the address, email and phone number of the company, it also contains the form to get in touch for any questions the users might have.

![Screenshot of GreenSeed website](static/image/screenshots/home-contact.png)

</details>


<details>
   <summary>Shop</summary>

### Landing Page

Shop landing page has three main sections, top contains large hero image and search bar to help users quickly find what they need.

![Screenshot of GreenSeed website](static/image/screenshots/shop-main-top.png)

Middle section lists different collections (groups) of plants users might be interested in.

![Screenshot of GreenSeed website](static/image/screenshots/shop-main-middle.png)

Bottom part of the site has a big image of current limited time offer and information on shipping and support.

![Screenshot of GreenSeed website](static/image/screenshots/shop-main-bottom.png)

### All Products

Product page contains the product listing, it's possible to fliter products by groups or use the search to quickly find what you need. Search works for product names, groups and description. Each product is shown in a card with image, price, short description, stock availability and rating. If the user is admin then each card also contains a link to edit or delete the product like shown below.

![Screenshot of GreenSeed website](static/image/screenshots/shop-all_products.png)

### Product Details

Product details page gives the full product description, bigger image, price, stock availability and rating. It also shows product reviews.

![Screenshot of GreenSeed website](static/image/screenshots/shop-product_details.png)


### Reviews

Users can only leave a review if they bought the product.
If they did, a button to leave a review will show up.
Review consists of message and a rating, total rating is calculated as a median of all user ratings.

![Screenshot of GreenSeed website](static/image/screenshots/leave-a-review.png)

Write a review and leave a rating.

![Screenshot of GreenSeed website](static/image/screenshots/write-review.png)

In case the already reviewed the product, insted of the button they will see a timestamp.

![Screenshot of GreenSeed website](static/image/screenshots/reviews.png)


</details>

<details>
   <summary>Cart</summary>

Users can add products to cart either directly from the main product listing or from product details page. There is a messaging system implemented so users can see if the product was added or removed successfully.
There is an option to increase or decrease product quantity inside the cart, before checkout.

Total price is calculated on the fly taking into the account eligibility for a free shipping if the total order is larger than 50 euros.
Price shows the price of the single item and total price is calculated on the fly depending on the ammount of particular item.

![Screenshot of GreenSeed website](static/image/screenshots/cart.png)

</details>

<details>
   <summary>Checkout</summary>

Checkout page contains the order summary and a form to fill out the payment and shipping details. Users have the option to save that information to their profile so the process isfaster in the future. If they have a profile on the site then the form will be prefilled with their info.

![Screenshot of GreenSeed website](static/image/screenshots/checkout.png)

Payments are done via Stripe Developement API, to quickly test the functionality you can fill the payment info with number 42 like shown below.

![Screenshot of GreenSeed website](static/image/screenshots/checkout-payment_info.png)

Once the order is finalized, users will be taken to a order summary. This will show them their order number as well as other details concerning order.
Confirmation email containing this information is automatically sent to email the user provided.

![Screenshot of GreenSeed website](static/image/screenshots/checkout-complete.png)


</details>

<details>
   <summary>My Account</summary>

My Account page contains the user information and provides a list of previous purchases. If the user clicks on the order number it will take them to a complete order summary.

![Screenshot of GreenSeed website](static/image/screenshots/my-account.png)

</details>

<details>
   <summary>Add Product</summary>

If a user is admin he will have a "Manage" link in the header which will take him/her to the Add Product page.

Header

![Screenshot of GreenSeed website](static/image/screenshots/header-manage.png)


Add Product

![Screenshot of GreenSeed website](static/image/screenshots/add-product.png)

</details>

<details>
   <summary>Login and Logout</summary

all-auth is used for user authentication

Login

![Screenshot of GreenSeed website](static/image/screenshots/login.png)

Logout

![Screenshot of GreenSeed website](static/image/screenshots/logout.png)


</details>

<br>

[Back to top](#greenseed)  

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
Each app has it's own testing folder.
To run the tests type into terminal:

```
python3 manage.py test app_name.tests
```

[Home App](/documents/unit_testing.md#home-app-home-app) page

[Profiles App](/documents/unit_testing.md#profiles-app-profiles-app) page

[Shop App](/documents/unit_testing.md#shop-app-shop-app) page

Site images found on [Unsplash](https://unsplash.com/)