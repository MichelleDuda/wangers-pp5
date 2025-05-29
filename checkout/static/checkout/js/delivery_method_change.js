document.addEventListener('DOMContentLoaded', function() {
    const deliveryRadios = document.querySelectorAll('input[name="delivery_method"]');
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

    function updatePaymentIntent() {
        const selectedMethod = document.querySelector('input[name="delivery_method"]:checked').value;

        fetch(window.createPaymentIntentUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-CSRFToken': csrfToken
            },
            body: new URLSearchParams({
                'delivery_method': selectedMethod
            })
        })
        .then(response => response.json())
        .then(data => {
            // Update client secret
            const clientSecretInput = document.querySelector('#id_client_secret');
            if (clientSecretInput) {
                clientSecretInput.value = data.client_secret;
            } else {
                const hidden = document.createElement('input');
                hidden.type = 'hidden';
                hidden.name = 'client_secret';
                hidden.id = 'id_client_secret';
                hidden.value = data.client_secret;
                document.querySelector('form').appendChild(hidden);
            }

            // Update totals on page
            const orderTotalElem = document.querySelector('#order-total');
            const deliveryCostElem = document.querySelector('#delivery-cost');
            const grandTotalElem = document.querySelector('#grand-total');

            if (orderTotalElem) {
                orderTotalElem.textContent = `$${parseFloat(data.total).toFixed(2)}`;
                orderTotalElem.dataset.total = parseFloat(data.total).toFixed(2);
            }

            if (deliveryCostElem) {
                deliveryCostElem.textContent = `$${parseFloat(data.delivery).toFixed(2)}`;
            }

            if (grandTotalElem) {
                grandTotalElem.textContent = `$${parseFloat(data.grand_total).toFixed(2)}`;
            }

            // Update charge summary text below the submit button
            const chargeSummary = document.querySelector('.submit-button p.small.text-danger span strong');
            if (chargeSummary) {
                chargeSummary.textContent = `$${parseFloat(data.grand_total).toFixed(2)}`;
            }
        });
    }

    deliveryRadios.forEach(radio => {
        radio.addEventListener('change', updatePaymentIntent);
    });

    // Trigger once on page load
    updatePaymentIntent();
});