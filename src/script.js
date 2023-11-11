const displayData = (data) => {
    // Use the jQuery $ function to select the element by ID and set its content
    $('#goals-needed').text(data); // If it's just text
    // OR
    //$('#data-container').html(data); // If you need to insert HTML
};
// Example data from a script
const parsedData = '';

if (parsedData == '') {
    displayData("All goals meet.......");
}
else {
    displayData(parsedData);    
}

