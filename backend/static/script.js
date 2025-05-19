document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");

    form.addEventListener("submit", function (e) {
        const message = form.querySelector("textarea").value.trim();
        
        if (message === "") {
            e.preventDefault();
            alert("Please enter a feedback message before submitting.");
        } else {
            alert("Thanks for your feedback!");
        }
    });
});
