document.addEventListener('DOMContentLoaded', function () {
	fetchAccordionData('http://10.101.40.59/info/'); // Replace with your actual API URL
});

function fetchAccordionData(apiUrl) {
	fetch(apiUrl)
		.then((response) => response.json())
		.then((data) => populateAccordion(data))
		.catch((error) => console.error('Error fetching data:', error));
}

function populateAccordion(data) {
	const accordionContainer = document.getElementById('accordTemplate'); // Main accordion ID

	data.forEach((item, index) => {
		const mainAccordionId = `collapseMain${index}`;
		let subAccordions = '';

		for (const key in item) {
			if (item.hasOwnProperty(key) && typeof item[key] === 'string') {
				// Assuming we only create sub-accordions for string properties
				const subAccordionId = `collapseSub${key}${index}`;
				subAccordions += `
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="subHeading${key}${index}">
                            <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                                ${key.charAt(0).toUpperCase() + key.slice(1)}
                            </button>
                        </h2>
                        <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${key}${index}">
                            <div class="accordion-body">
                                ${item[key]}
                            </div>
                        </div>
                    </div>
                `;
			}
		}

		const accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${index}">
                    <button class="accordion-button collapsed bg-white text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#${mainAccordionId}" aria-expanded="false" aria-controls="${mainAccordionId}">
                        ${item.name || 'Item ' + (index + 1)} 
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
