const express = require('express');
const app = express();
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post('/save', (req, res) => {
  const { username, password } = req.body;

  // Here, you can save the username and password to a database or file securely.
  // Do not save passwords in plaintext; always hash them before storing.

  res.send('Data saved successfully');
});

app.listen(3000, () => {
  console.log('Server is running on port 3000');
});
