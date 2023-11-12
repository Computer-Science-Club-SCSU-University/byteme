const express = require("express");
const app = express();
const bodyParser = require("body-parser");

const cors = require("cors"); // Import the cors middleware
app.use(cors()); // Use cors middleware to allow cross-origin requests

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

app.post("/save", (req, res) => {
  const { username, password } = req.body;

  // Here, you can save the username and password to a database or file securely.
  // Do not save passwords in plaintext; always hash them before storing.

  // For demonstration purposes, we'll just log the received data.
  console.log("Received Data - Username:", username);
  console.log("Received Data - Password:", password);

  res.send("Data saved successfully");
});

app.listen(3000, () => {
  console.log("Server is running on port 3000");
});
