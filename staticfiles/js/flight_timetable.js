const expandButtons = document.getElementsByClassName('expand-btn');
const flightInfoDivs = document.getElementsByClassName('extra-flight-info');

for (let button of expandButtons) {
    button.addEventListener("click", (e) => {
        // Prevent the default behavior of the <a> element
        e.preventDefault();

        let flightDivId = e.target.getAttribute("data-flight_id");
        let flightDiv = document.getElementById(flightDivId);

        // If we are clicking a flight info button that is already open, close it
        if (flightDiv.style.display === "block") {
            flightDiv.style.display = "none";
            return;
        }

        // Hide all flight info divs
        for (let flight of flightInfoDivs) {
            flight.style.display = "none";
        }

        // Display the flight info div associated with the clicked button
        flightDiv.style.display = "block";
    });
}