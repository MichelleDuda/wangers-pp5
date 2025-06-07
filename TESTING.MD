# Wangers Testing

* [Validator Testing](#validator-testing)
    * [HTML Validation](#html-validation)
    * [CSS Validation](#css-validation)
    * [Javascript Validation](#javascript-validation)
    * [Python Pep8 Linter](#python-pep8-linter)
* [Lighthouse Testing](#lighthouse-testing)
* [Additional Manual Testing](#additional-manual-testing)
* [User Story Testing](#user-story-testing)
* [Browser Compatibility](#browser-compatibility)
* [Bugs](#bugs)
* [Known Bugs](#known-bugs)

## Validator Testing

### HTML Validation
The following files all passed through the [HTML Validator](https://validator.w3.org/nu/#textarea) with no errors:
<img src="media/testing/html/html_validator.jpg">

- index.html [Full Results](static/documentation/testing/validator_results/html_home.pdf)
- contact.html
- cart.html
- checkout.html
- checkout_success.html
- profile.html
- review_list.html
- review_form.html
- login.html
- signup.html
- logout.html 




### CSS Validation
The following files passed through the [CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors:
<img src="static/documentation/testing/css/css_validator2.jpg">

- base.css [Full Results](static/documentation/testing/validator_results/css_validator.pdf)
- checkout.css
- profile.css

### Javascript Validation

- [Javascript Validator](https://jshint.com)
 - Code from checkout_toggle.js passed through JSHint site with no errors. The following Metrics were logged: There are 3 functions in this file. Function with the largest signature take 1 arguments, while the median is 0. Largest function has 7 statements in it, while the median is 7. The most complex function has a cyclomatic complexity value of 3 while the median is 1.

 - Code from delivery_method_change.js passed through JSHint site with no errors. The following Metrics were logged: There are 5 functions in this file. Function with the largest signature take 1 arguments, while the median is 1. Largest function has 22 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 6 while the median is 1.

 - Code from delivery_method.js passed through JSHint site with no errors. The following Metrics were logged: There are 3 functions in this file. Function with the largest signature take 1 arguments, while the median is 0. Largest function has 11 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 3 while the median is 1.

 - Code from stripe_elements.js passed through JSHint site with no errors. The following Metrics were logged: There are 8 functions in this file. Function with the largest signature take 1 arguments, while the median is 0.5. Largest function has 10 statements in it, while the median is 2.5. The most complex function has a cyclomatic complexity value of 3 while the median is 1

 - Code from cart_sound.js passed through JSHint site with no errors. The following Metrics were logged: There are 2 functions in this file. Function with the largest signature take 0 arguments, while the median is 0. Largest function has 4 statements in it, while the median is 2.5. The most complex function has a cyclomatic complexity value of 3 while the median is 2.


### Python Pep8 Linter
The following files all passed through the [Python PEP8 Linter](https://pep8ci.herokuapp.com/) with no errors:
    <details><summary>urls.py</summary>
    <img src="static/documentation/testing/validator_images/python/py_urls.jpg"> 
    </details>

The following file passed through with no errors on customized code. However, preloaded built in code had a few errors for line length:
    <details><summary>settings.py</summary>
    <img src="static/documentation/testing/validator_images/python/py_settings.jpg"> 
    </details>
 
## Lighthouse Testing
- Lighthouse result for index.html

    ![Lighthouse results index](media/readme/lighthouse/home.jpg)

- Lighthouse result for menu.html

    ![Lighthouse results index](media/readme/lighthouse/menu.jpg)

- Lighthouse result for menu_item_detail.html

    ![Lighthouse results index](media/readme/lighthouse/menu_detail.jpg)

- Lighthouse result for review_list.html

    ![Lighthouse results index](media/readme/lighthouse/reviews_list.jpg)

- Lighthouse result for review_form.html

    ![Lighthouse results index](media/readme/lighthouse/review_form.jpg)

- Lighthouse result for contact_us.html

    ![Lighthouse results index](media/readme/lighthouse/contact.jpg)

- Lighthouse result for Authentication Pages

    ![Lighthouse results index](media/readme/lighthouse/login.jpg)





## Additional Manual Testing

### Navigation - Navbar

| Feature Tested       | Steps                                                                                            | Expected Outcome                                                                                                              | Results |
| -------------------- | ------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ------- |
| Home Link Icon       | While not on the homepage, click the Wangers Logo                                                | User is redirected to the homepage.                                                                                           | Pass    |
| Home Link            | White not on the homepage click "Home"                                                           | User is redirected to the homepage.                                                                                           | Pass    |
| Menu Link            | While not on the menu page click "Menu"                                                          | User is redirected to the Menu page.                                                                                          | Pass    |
| Reviews Link         | While not on the reviews page click "Reviews"                                                    | User is redirected to the Reviews page.                                                                                       | Pass    |
| Contact Us Link      | While not on the contact page click "Contact Us"                                                 | User is redirected to the Contact Us page.                                                                                    | Pass    |
| Cart Link            | While on any bag click the bag/cart icon in the header.                                          | User is redirected to the Cart page                                                                                           | Pass    |
| Cart Link (Toast)    | After adding an item to the cart, click on the "Go to Cart" button on the success message toast. | User is redirected to the Cart page                                                                                           | Pass    |
| Register Link        | While not authenticated click, "My Account" then "Register"                                      | User is redirected to the Sign Up page.                                                                                       | Pass    |
| Login Link           | While not authenticated click "My Account" then "Login"                                          | User is redirected to the Login page.                                                                                         | Pass    |
| Logout Link          | While authenticated click "My Account" then "Logout"                                             | User is directed to a buffer page to confirm logout. Clicking the Logout Button again will log the user out of their account. | Pass    |
| My Profile           | While authenticated click "My Account" then "My Profile"                                         | User is redirected to the Profile Page that includes past orders.                                                             | Pass    |
| Menu Management Link | While authenticated as a superuser click "My Account" then "Menu Management"                     | User is redirected to a page where they can add new menu items.                                                               | Pass    |


### Other Navigation

| Feature Tested         | Steps                                                                                      | Expected Outcome                                                                                                                          | Results |
| ---------------------- | ------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------- | ------- |
| Order Now Button       | While on the homepage click the "Order Now" button                                         | User is redirected to Menu page.                                                                                                          | Pass    |
| Social Media Links     | While on any page navigate to the footer and click on the various social media icons.      | A new tab will open for the appropriate social media website.                                                                             | Pass    |
| Menu Item Navigation   | While on the menu page click on any of the menu item photos.                               | User is redirected to the Menu Item Details page for that particular item, where they can make selections and add the item to their cart. | Pass    |
| Keep Shopping Button   | While on the Menu Items Detail page and the Checkout page, click the Keep Shopping button. | User is redirected to the Menu page.                                                                                                      | Pass    |
| Secure Checkout Button | While on the Cart page, click on the "Secure Checkout" button                              | User is redirected to the checkout page.                                                                                                  | Pass    |
| Adjust Bag Button      | While on the Checkout page, click the "Adjust Bag" button                                  | User is redirected to the Cart page.                                                                                                      | Pass    |
| Back to Menu Button    | While on the Checkout Success page, click the "Back to Menu" button                        | User is redirected back to the menu page                                                                                                  | Pass    |
| Leave a Review Button  | While on the Reviews Page, click the "Leave a Review" button                               | If authenticated the user is redirected to the review form page. If the user is not authenticated, they are redirected to the login page. | Pass    |


###





## Browser Compatibility
This website was tested on the following browsers:
- Google Chrome Version 137.0.7151.56 (Official Build) (64-bit)
- Microsoft Edge Version 136.0.3240.92 (Official build) (64-bit)
- Mozilla Firefox Version 135.0.1 (64-bit)

## Bugs
1. ValueError at /checkout/"<OrderLineItem: 4 x Boneless Wings on order BF5EC0F52BC34F34891256C8FAC356D2>" needs to have a value for field "id" before this many-to-many relationship can be used.
 - Bug caused by trying to access a many-to-many field before a primary ID was saved. 
 - Fixed by changing the save method on OrderLineItems form: 
    def save(self, *args, **kwargs):
        """ Calculate the lineitem total including add-ons """
        base_price = self.menu_item.price * self.quantity
        addons_total = sum(addon.price for addon in self.addons.all()) * self.quantity
        self.lineitem_total = base_price + addons_total
        super().save(*args, **kwargs)

        TO: 

            def save(self, *args, **kwargs):
        """Calculate the lineitem total including add-ons."""
        base_price = self.menu_item.price * self.quantity
        addons_total = 0
        if self.pk:
            addons_total = sum(
                addon.price for addon in self.addons.all()
            )
        self.lineitem_total = base_price + addons_total
        super().save(*args, **kwargs)

2. Unable to Add Items Without Sauce_ID to cart:
    - Fixed by changing cart handling in contexts.py from: 
        for key, item_data in cart.items():
            item_id, sauce_id = key.split('_')
            item_id = int(item_id)
            sauce_id = int(sauce_id) if sauce_id != 'None' else None
            menu_item = get_object_or_404(MenuItem, pk=item_id)
            sauce = get_object_or_404(Sauce, pk=sauce_id) if sauce_id else None

        to:

        for key, item_data in cart.items():
            parts = key.strip('_').split('_')
            item_id = int(parts[0])
            sauce_id = None
            if len(parts) > 1 and parts[1] not in ('None', ''):
                try:
                    sauce_id = int(parts[1])
                except ValueError:
                    sauce_id = None
            menu_item = get_object_or_404(MenuItem, pk=item_id)
            sauce = get_object_or_404(Sauce, pk=sauce_id) if sauce_id else None

3. Duplicate orders were being created by webhooks. Fixed by a typo in checkout view changing strip_id to stripe_id.
4. Cart was not calculating delivery charge in new session by defauly after completing a pickup order. 
    - Fixed by adding the following code to the checkout view to reset the session after the order is saved:
        request.session['delivery_method'] = 'delivery'
        request.session.modified = True 


## Known Bugs
There are no unaddressed known bugs at this time. 