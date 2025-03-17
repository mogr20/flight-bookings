const bookingForm = document.getElementById('bookingForm');
const formFirstName = document.getElementById('id_first_name');
const formLastName = document.getElementById('id_last_name');
const formBaggage = document.getElementById('id_baggage_weight');
const formDietary = document.getElementById('id_dietary_requirements');
const passengerForm = document.getElementById('passengerForm');
const submitButton = document.getElementById('submitButton');

const deleteModal = new bootstrap.Modal(document.getElementById('deleteModal'));
const deleteButtons = document.getElementsByClassName('btn-delete');
const deleteBody = document.getElementById('modal-body');
const deleteTitle = document.getElementById('deleteModalLabel');
const editButtons = document.getElementsByClassName('btn-edit');
const deleteConfirm = document.getElementById('deleteConfirm');

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let userId = e.target.getAttribute("data-user_id");
        // If the delete button is a passenger delete button
        if (e.target.hasAttribute("data-passenger_id")) {
            let passengerId = e.target.getAttribute("data-passenger_id");
            let bookingId = e.target.getAttribute("data-booking_id");
            deleteBody.innerText = "Are you sure you want to remove this passenger?\nThis action cannot be undone.";
            deleteTitle.innerText = "Remove Passenger?";
            deleteConfirm.href = `/user/${userId}/booking/${bookingId}/remove_passenger/${passengerId}/`;
            deleteConfirm.innerText = "Remove Passenger";
            deleteModal.show();
        }
        // If the delete button is a journey delete button
        else if (e.target.hasAttribute("data-journey_id")) {
            let journeyId = e.target.getAttribute("data-journey_id");
            deleteConfirm.href = `/user/${userId}/journey/${journeyId}/remove/`;
            deleteModal.show();
        }
    });
}

/**
* Initializes edit functionality for the provided edit buttons.
* 
* For each button in the `editButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Fetches the content of the corresponding comment.
* - Populates the `commentText` input/textarea with the comment's content for editing.
* - Updates the submit button's text to "Update".
* - Sets the form's action attribute to the `edit_comment/{commentId}` endpoint.
*/
for (let button of editButtons) {
    button.addEventListener("click", (e) => {
        if (e.target.hasAttribute("data-passenger_id")) {
            let passengerId = e.target.getAttribute("data-passenger_id");
            let passengerFirstName = document.getElementById(`first_name_${passengerId}`).innerText;
            let passengerLastName = document.getElementById(`last_name_${passengerId}`).innerText;
            let passengerBaggage = document.getElementById(`baggage_${passengerId}`).innerText;
            let passengerDietary = document.getElementById(`dietary_${passengerId}`).innerText;

            formFirstName.value = passengerFirstName;
            formLastName.value = passengerLastName;
            if (passengerDietary != "") {
                console.log("in dietary if: ", passengerDietary);
                formDietary.value = passengerDietary;
            }
            if (passengerBaggage != 0) {
                console.log("in passenger baggage if: ", passengerBaggage);
                formBaggage.value = passengerBaggage;
            }
            submitButton.innerText = "Update Customer info";
            passengerForm.setAttribute("action", `edit_passenger/${passengerId}/`);
        }
        else if (e.target.hasAttribute("data-journey_id")) {
            console.log("in edit else if: journey_id");
            let userId = e.target.getAttribute("data-user_id");
            let bookingId = e.target.getAttribute("data-booking_id");
        }
    });
}

document.querySelector('.carousel-control-prev').addEventListener('click', () => {
    console.log('Previous button clicked');
});

document.querySelector('.carousel-control-next').addEventListener('click', () => {
    console.log('Next button clicked');
});