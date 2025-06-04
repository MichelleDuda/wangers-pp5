# DG Catering Student Meal Plan Portal Testing

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
<img src="static/documentation/testing/validator_images/html_validator.jpg">
- index.html [Full Results](static/documentation/testing/validator_results/html_home.pdf)

### CSS Validation
The following files passed through the [CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) with no errors:
<img src="static/documentation/testing/validator_images/css_validator2.jpg">

- base.css [Full Results](static/documentation/testing/validator_results/css_validator.pdf)

### Javascript Validation

- [Javascript Validator](https://jshint.com)
  - Code from script.js passed through JSHint site with no errors. The following Metrics were logged: There are 9 functions in this file. Function with the largest signature take 1 arguments, while the median is 0. Largest function has 7 statements in it, while the median is 2. The most complex function has a cyclomatic complexity value of 2 while the median is 1.


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

    ![Lighthouse results index](static/documentation/testing/lighthouse/lighthouse_home_html.jpg)



## Additional Manual Testing

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