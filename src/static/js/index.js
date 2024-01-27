document.addEventListener("DOMContentLoaded", function () {
    // Your form submission code here

    const creditButton = document.getElementById("submit-credit");
    const debitButton = document.getElementById("submit-debit");
    const typeInput = document.getElementById("transaction-type");

    creditButton.addEventListener("click", () => {
        typeInput.value = 1;
    });

    debitButton.addEventListener("click", () => {
        typeInput.value = 0;
    });

    document.getElementById("item-type-input").addEventListener("change", function () {
        const createWalletOption = document.getElementById("create-wallet-option");
        if (this.selectedOptions[0].id === "create-wallet-option") {  // Check if the "Create New Wallet" option is selected
            window.location.href = `${window.location.origin}${this.value}`;  // Redirect to the create wallet URL
        } else {
            const selectedWalletId = this.value;  // Get the ID of the selected wallet
            const tbody = document.getElementById("transactions-table");
            tbody.innerHTML = '';
            // Send an AJAX request to get the transactions and balance for the selected wallet
            fetch(`/transactions/by_wallet/${selectedWalletId}`)
                .then(response => response.json())
                .then(data => {

                    data.transactions.forEach(transaction => {
                        const row = tbody.insertRow();
                        row.innerHTML = `
                <td>${transaction.category}</td>
                <td>${transaction.description}</td>
                <td class="has-text-right">${transaction.amount}${transaction.sign}</td>
                <td class="has-text-right">
                    <span class="icon remove-button">
                        <a href="#">
                            <i class="fas fa-minus-square"></i>
                        </a>
                    </span>
                </td>
            `;
                    });

// Update the balance and currency sign
                    document.getElementById("final-credit").textContent = data.wallet_balance;
                    document.getElementById("sign").textContent = data.wallet_sign;
                })
                .catch(error => {
                    console.error("Error fetching transactions:", error);
                });
        }
    });
    form = document.querySelector("form")
    form.addEventListener("submit", function (event) {
        event.preventDefault();  // Prevent default form submission

        const formData = new FormData(form);  // Collect form data

        fetch(this.action, {
            method: "POST",
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const transactionData = data.transaction;  // Get transaction data from JSON response
                    const sign = transactionData.sign;

                    // Create and populate a new table row with the received data
                    const tbody = document.getElementById("transactions-table");
                    const row = tbody.insertRow(0);
                    row.innerHTML = `
                <td>${transactionData.category}</td>
                <td>${transactionData.description}</td>
                <td class="has-text-right">${transactionData.amount}${transactionData.sign}</td>
                <td class="has-text-right">
                    <span class="icon remove-button">
                        <a href="#">
                            <i class="fas fa-minus-square"></i>
                        </a>
                    </span>
                </td>
            `;
                    this.reset();
                    document.getElementById("final-credit").textContent = data.wallet_balance;
                    document.getElementById("sign").textContent = sign;
                } else {
                    for (const [key, value] of Object.entries(data.errors)) {
                        console.error("Error creating transaction:", `<p>${key}: ${value}</p>`)
                    }
                }
            })
            .catch(error => {
                console.error("Error creating transaction:", error);
            });
    });

});