// Event listener for the DOMContentLoaded event
document.addEventListener('DOMContentLoaded', function () {
	// Calls fetchAccordionData function when the DOM is fully loaded
	fetchAccordionData('http://10.101.40.59/ '); // Replace with your actual API URL
});

// Function to fetch data for the accordion from an API
function fetchAccordionData(apiUrl) {
	// Fetches data from the API URL
	fetch(apiUrl)
		.then((response) => response.json()) // Parses the response as JSON
		.then((data) => populateAccordion(data)) // Calls populateAccordion with the parsed data
		.catch((error) => console.error('Error fetching data:', error)); // Logs errors, if any
}

// Function to populate the accordion with data
const populateAccordion = (data) => {
	const accordionContainer = document.getElementById('accordTemplate');

	// Iterate over each goal area
	Object.keys(data).forEach((goalArea, index) => {
		let subAccordions = '';

		// Iterate over each course within the goal area
		data[goalArea].forEach((courseObject) => {
			const courseName = Object.keys(courseObject)[0];
			const coveredGoals = courseObject[courseName];

			const subAccordionId = `collapseSub${goalArea}${courseName.replace(
				/[^a-zA-Z0-9]/g,
				''
			)}`;

			// Generate sub-accordion items for each course
			subAccordions += `
                <div class="accordion-item">
                    <h2 class="accordion-header" id="subHeading${courseName}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                            ${courseName}
                        </button>
                    </h2>
                    <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${courseName}">
                        <div class="accordion-body">
                            Covered Goals: ${coveredGoals.join(', ')}
                        </div>
                    </div>
                </div>
            `;
		});

		const mainAccordionId = `collapseMain${index}`;

		// Generate main accordion items for each goal area
		const accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${index}">
                    <button class="accordion-button collapsed bg-white text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#${mainAccordionId}" aria-expanded="false" aria-controls="${mainAccordionId}">
                        Goal Area: ${goalArea}
                    </button>
                </h2>
                <div id="${mainAccordionId}" class="accordion-collapse collapse" aria-labelledby="heading${index}">
                    <div class="accordion-body">
                        <div class="accordion" id="subAccordion${index}">
                            ${subAccordions}
                        </div>
                    </div>
                </div>
            </div>
        `;

		accordionContainer.innerHTML += accordionItem;
	});
}