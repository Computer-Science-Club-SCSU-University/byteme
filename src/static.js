document.addEventListener('DOMContentLoaded', function () {
	fetchAccordionData('http://10.101.40.59/template/'); // Replace with your actual API URL
});

function fetchAccordionData(apiUrl) {
	fetch(apiUrl)
		.then((response) => response.json())
		.then((data) => populateAccordion(data))
		.catch((error) => console.error('Error fetching data:', error));
}

function populateAccordion(data) {
	const accordionContainer = document.getElementById('accordTemplate'); // Use the main accordion ID

	data.forEach((item, index) => {
		const mainAccordionId = `collapseMain${index}`;
		const subAccordionId = `collapseSub${index}`;

		const accordionItem = `
            <div class="accordion-item">
                <h2 class="accordion-header" id="heading${index}">
                    <button class="accordion-button collapsed bg-white text-dark" type="button" data-bs-toggle="collapse" data-bs-target="#${mainAccordionId}" aria-expanded="false" aria-controls="${mainAccordionId}">
                        ${item.name} 
                    </button>
                </h2>
                <div id="${mainAccordionId}" class="accordion-collapse collapse" aria-labelledby="heading${index}">
                    <div class="accordion-body">
                        <div class="accordion" id="subAccordion${index}">
                            <div class="accordion-item">
                                <h2 class="accordion-header" id="subHeading${index}">
                                    <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                                        Email
                                    </button>
                                </h2>
                                <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${index}">
                                    <div class="accordion-body">
                                        ${item.email}
                                    </div>
                                </div>
                                <h2 class="accordion-header" id="subHeading${index}">
                                    <button class="accordion-button collapsed mt-3" type="button" data-bs-toggle="collapse" data-bs-target="#${subAccordionId}" aria-expanded="false" aria-controls="${subAccordionId}">
                                        Geo
                                    </button>
                                </h2>
                                <div id="${subAccordionId}" class="accordion-collapse collapse" aria-labelledby="subHeading${index}">
                                    <div class="accordion-body">
                                        ${item.address.geo.lat}
                                        ${item.address.geo.lng}
                                    </div>
                                </div>
                            </div>
                            <!-- Additional details can be added here -->
                        </div>
                    </div>
                </div>
            </div>
        `;

		accordionContainer.innerHTML += accordionItem;
	});
}
