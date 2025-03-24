const expandButtons = document.getElementsByClassName('expand-btn');
const flightInfoDivs = document.getElementsByClassName('extra-flight-info');

/**
 * Intialises the expansion functionality for the provided expand buttons.
 * 
 * For each button in the `expandButtons` collection:
 * - On click, get the div ID for the flight we are expanding.
 * - If the flight info div is already shown, hide it and return.
 * - Else, we hide all previously expanded flight info divs.
 * - Displays the flight info div associated with the clicked button
 */

for (let button of expandButtons) {
    button.addEventListener("click", (e) => {
        // Prevent the default behavior of the <a> element
        // we don't want to follow the link to book a flight, we want to click the expand button.
        e.preventDefault();

        let flightDivId = e.target.getAttribute("data-flight_id");
        let flightDiv = document.getElementById(flightDivId);

        // If we are clicking a flight info button that is already open, close it
        if (flightDiv.style.display === "block") {
            flightDiv.style.display = "none";
            button.innerText = "+";
            return;
        }

        // Hide all flight info divs
        for (let flight of flightInfoDivs) {
            flight.style.display = "none";
        }

        // Change all expand button text to "+" to show they can be expanded
        for (let button of expandButtons) {
            button.innerText = "+";
        }

        // Display the flight info div associated with the clicked button
        flightDiv.style.display = "block";
        // Change the clicked button text to "-" to show it can be closed
        button.innerText = "-";
    });
}