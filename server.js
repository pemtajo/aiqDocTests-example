/* eslint-disable camelcase */
const express = require('express');
const authController = require('./controllers/authController');
const fileUploadController = require('./controllers/fileUploaController');
const parametersUrlController = require('./controllers/parameterUrlController');
const fileupload = require("express-fileupload");
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(fileupload());

app.get('/health', function (req, res) {
  res.json('Hello World! AiqdocTests-example');
});

app.post('/transfer', authController.middlewareAuth, async (req, res) => {
  res.json({ "data": [{ "success": true }, { "success": false }] });
});

app.post('/file-upload', fileUploadController.store);

app.post('/parameters/:id', authController.middlewareAuth, parametersUrlController);

app.listen(process.env.APPLICATION_PORT);
