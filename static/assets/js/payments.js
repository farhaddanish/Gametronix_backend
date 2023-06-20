const credit_input = document.getElementById("credit-number");

credit_input.addEventListener("input", function () {
    if (typeof this.value !== typeof 2) {
        this.value = this.value.replace(/\D/g, "");
    }
    let creditCardNumber = this.value.replace(/\s/g, ""); // Remove any existing spaces

    // Add space after every four digits
    creditCardNumber = creditCardNumber.replace(/(\d{4})(?=\d)/g, "$1 ");

    this.value = creditCardNumber;
});

const expiry_input = document.getElementById("expiry-input");
expiry_input.addEventListener("input", function () {
    if (typeof this.value !== typeof 2) {
        this.value = this.value.replace(/\D/g, "");
    }

    let creditCardNumber = this.value.replace(/\s/g, ""); // Remove any existing spaces

    // Add space after every four digits
    creditCardNumber = creditCardNumber.replace(/(\d{2})(?=\d)/g, "$1-");

    this.value = creditCardNumber;
});