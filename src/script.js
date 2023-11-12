// Event listener for the DOMContentLoaded event
document.addEventListener('DOMContentLoaded', function () {
    // Calls fetchAccordionData function when the DOM is fully loaded
    fetchAccordionData('http://10.101.41.235/utils');
    // if (!fetchAccordionData('http://10.101.16.250/utils')) {
    //     console.log('Error fetching data');
    // } // Replace with your actual API URL
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
// 
function populateAccordion(data) {
	const accordionContainer = document.getElementById('accordTemplate');

	Object.keys(data).forEach((mainCategory, mainIndex) => {
		let subAccordions = '';
		const mainAccordionId = `collapseMain${mainIndex}`;

		data[mainCategory].forEach((subCategoryObj) => {
			const subCategoryKey = Object.keys(subCategoryObj)[0];
			const subCategoryData = subCategoryObj[subCategoryKey];
			const subAccordionId = `collapseSub${mainIndex}${subCategoryKey.replace(
				/[^a-zA-Z0-9]/g,
				''
			)}`;

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

		accordionContainer.innerHTML += accordionItem;
	});
}