document.addEventListener('DOMContentLoaded', () => {
  const deliveryRadios = document.querySelectorAll('input[name="delivery_method"]');
  
  deliveryRadios.forEach(radio => {
    radio.addEventListener('change', async () => {
      const selectedMethod = document.querySelector('input[name="delivery_method"]:checked').value;

      const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

      try {
        const response = await fetch('/cart/update-delivery/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
            'X-CSRFToken': csrfToken,
          },
          body: new URLSearchParams({
            'delivery_method': selectedMethod
          }),
        });
        const data = await response.json();

        if (data.success) {
          // Update the delivery and grand total amounts on the page
          document.querySelector('#delivery-cost').textContent = `$${parseFloat(data.delivery_cost).toFixed(2)}`;
          const total = parseFloat(document.querySelector('#order-total').dataset.total);
          const grandTotal = total + parseFloat(data.delivery_cost);
          document.querySelector('#grand-total').textContent = `$${grandTotal.toFixed(2)}`;
        }
      } catch (error) {
        console.error('Error updating delivery method:', error);
      }
    });
  });
});