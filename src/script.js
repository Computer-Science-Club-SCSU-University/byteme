// JavaScript function to make an AJAX call
const loadData = () => {
	$.ajax({
		url: '[place holder]', // URL of the server-side script
        type: 'GET', // The HTTP method
        dataType: 'json',
		success: function (response) {
			// This function is called if the request was successful.
			$('#result').html(response); // Update the content of a div with id 'result'
		},
		error: function (xhr, status, error) {
			// This function is called if the request failed.
			console.error('Error: ' + error);
		},
	});
}
// Call the function, for example, on a button click
$('#goals-needed').click(loadData);







const displayData = (data) => {
	// Use the jQuery $ function to select the element by ID and set its content
	$('#goals-needed').text(data); // If it's just text
	// OR
	//$('#data-container').html(data); // If you need to insert HTML
};
// Example data from a script
const parsedData = '';

if (parsedData == '') {
	displayData('All goals meet.......');
} else {
	displayData(parsedData);
}
