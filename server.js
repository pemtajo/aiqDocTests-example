/* eslint-disable camelcase */
const express = require('express');
const authController = require('./controllers/authController');
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());


app.get('/health', function (req, res) {
  res.json('Hello World! AiqdocTests-example');
});

app.post('/transfer', authController.middlewareAuth, async (req, res) => {
  res.json({ "data": [{ "success": true }, { "success": false }] });
});



app.listen(process.env.APPLICATION_PORT);
