document.addEventListener('DOMContentLoaded', function() {
    const addToCartButton = document.querySelector('input[type="submit"][value="Add to Cart"]');
    const addToCartSound = document.getElementById('addToCartSound');

    if (addToCartButton && addToCartSound) {
        addToCartButton.addEventListener('click', function() {
            addToCartSound.play();
        });
    }
});