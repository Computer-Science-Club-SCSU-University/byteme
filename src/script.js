// Event listener for the DOMContentLoaded event
document.addEventListener('DOMContentLoaded', function () {
    // Calls fetchAccordionData function when the DOM is fully loaded
    fetchAccordionData('http://10.101.41.235/utils');
});

// Function to fetch data for the accordion from an API
const fetchAccordionData = (apiUrl) => {
	// Fetches data from the API URL
	fetch(apiUrl)
		.then((response) => response.json()) // Parses the response as JSON
		.then((data) => populateAccordion(data)) // Calls populateAccordion with the parsed data
		.catch((error) => console.error('Error fetching data:', error)); // Logs errors, if any
}

/// Function to populate accordion elements with api data
const populateAccordion = (data) => {
	// Selecting the accordion container in the DOM
	const accordionContainer = document.getElementById('accordTemplate');

	// Iterating over each main category in the provided data
	Object.keys(data).forEach((mainCategory, mainIndex) => {
		// Variable to store HTML for sub-accordions
		let subAccordions = '';
		// Creating a unique ID for the main accordion element
		const mainAccordionId = `collapseMain${mainIndex}`;

		// Iterating over each subcategory within the main category
		data[mainCategory].forEach((subCategoryObj) => {
			// Extracting the key (name) of the subcategory
			const subCategoryKey = Object.keys(subCategoryObj)[0];
			// Extracting the data associated with the subcategory
			const subCategoryData = subCategoryObj[subCategoryKey];
			// Creating a unique ID for the sub-accordion element
			const subAccordionId = `collapseSub${mainIndex}${subCategoryKey.replace(
				/[^a-zA-Z0-9]/g,
				''
			)}`;

			// Constructing HTML for each sub-accordion item
			subAccordions += `
                <div class="accordion-item">
                    <h2 class="accordion-header" id="subHeading${subCategoryKey}${mainIndex}">
                        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                           ${subCategoryKey}
                        </button>
                    </h2>
                    <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${subCategoryKey}${mainIndex}">
                        <div class="accordion-body">
                            Goal: ${subCategoryData.join(', ')}
                        </div>
                    </div>
                </div>
            `;
		});

		// Constructing HTML for the main accordion item
		const accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${mainIndex}">
                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${mainAccordionId}" aria-expanded="false" aria-controls="${mainAccordionId}">
                        Goal: ${mainCategory}
                    </button>
                </h2>
                <div id="${mainAccordionId}" class="accordion-collapse collapse" aria-labelledby="heading${mainIndex}">
                    <div class="accordion-body">
                        <div class="accordion" id="subAccordion${mainIndex}${mainCategory}">
                            ${subAccordions}
                        </div>
                    </div>
                </div>
            </div>
        `;

		// Appending the constructed accordion item to the accordion container
		accordionContainer.innerHTML += accordionItem;
	});
}
