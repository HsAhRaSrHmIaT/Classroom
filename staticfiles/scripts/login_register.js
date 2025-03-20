document.addEventListener('DOMContentLoaded', function() {
    const passwordInput = document.querySelector('#id_password1');
    if (!passwordInput) return; // Only run on register page
    
    const requirements = {
        length: {
            element: document.querySelector('#length'),
            regex: /.{8,}/
        },
        digit: {
            element: document.querySelector('#digit'),
            regex: /\d/
        },
        uppercase: {
            element: document.querySelector('#uppercase'),
            regex: /[A-Z]/
        },
        lowercase: {
            element: document.querySelector('#lowercase'),
            regex: /[a-z]/
        },
        special: {
            element: document.querySelector('#special'),
            regex: /[!@#$%^&*(),.?":{}|<>]/
        }
    };

    function updateRequirement(requirement, value) {
        const icon = requirement.element.querySelector('.icon');
        const isValid = requirement.regex.test(value);
        
        icon.className = isValid ? 'fas fa-check icon valid' : 'fas fa-times icon invalid';
        requirement.element.classList.toggle('valid', isValid);
        requirement.element.classList.toggle('invalid', !isValid);
        
        return isValid;
    }

    passwordInput.addEventListener('input', function() {
        const value = this.value;
        let allValid = true;
        
        // Update each requirement
        Object.values(requirements).forEach(req => {
            if (!updateRequirement(req, value)) {
                allValid = false;
            }
        });

        // Enable/disable submit button based on validation
        const submitButton = document.querySelector('.form-submit');
        submitButton.disabled = !allValid;
    });
});