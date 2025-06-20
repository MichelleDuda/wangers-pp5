document.addEventListener('DOMContentLoaded', function() {
    const pickupRadio = document.getElementById('pickup');
    const deliveryRadio = document.getElementById('delivery');

    const addressFieldIds = [
        'id_postcode',
        'id_town_or_city',
        'id_street_address1',
        'id_street_address2',
        'id_state'
    ];

    function toggleAddressFields() {
        const disable = pickupRadio.checked;
        addressFieldIds.forEach(id => {
            const field = document.getElementById(id);
            if (!field) return;
            field.disabled = disable;
            if (disable) {
                field.classList.add('disabled-field');
                field.value = '';
            } else {
                field.classList.remove('disabled-field');
            }
        });
    }

    pickupRadio.addEventListener('change', toggleAddressFields);
    deliveryRadio.addEventListener('change', toggleAddressFields);

    toggleAddressFields();

    const checkoutForm = document.getElementById('checkout-form');

    if (checkoutForm) {
        checkoutForm.addEventListener('submit', function (e) {
            if (deliveryRadio.checked) {
                const requiredFields = [
                    'id_postcode',
                    'id_town_or_city',
                    'id_street_address1'
                ];

                let valid = true;

                requiredFields.forEach(id => {
                    const field = document.getElementById(id);
                    if (field && !field.value.trim()) {
                        field.classList.add('input-error');
                        valid = false;
                    } else if (field) {
                        field.classList.remove('input-error');
                    }
                });

                if (!valid) {
                    e.preventDefault();
                    alert('Please fill in all required delivery address fields.');
                }
            }
        });
    }
});