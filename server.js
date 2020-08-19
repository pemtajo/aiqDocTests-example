/* eslint-disable camelcase */
const express = require('express');
const swaggerUi = require('swagger-ui-express');
const authController = require('./controllers/authController');
const fileUploadController = require('./controllers/fileUploadController');
const parametersUrlController = require('./controllers/parametersUrlController');
const fileupload = require("express-fileupload");
const app = express();

app.use(express.urlencoded({ extended: true }));
app.use(express.json());
app.use(fileupload());

const swaggerDocument = require('./static/swagger.json');
app.use('/docs', swaggerUi.serve, swaggerUi.setup(swaggerDocument));

app.get('/health', function (req, res) {
  res.json('Hello World! AiqdocTests-example');
});

app.post('/transfer', authController.middlewareAuth, async (req, res) => {
  res.json({ "data": [{ "success": true }, { "success": false }] });
});

app.post('/file-upload', fileUploadController.store);

app.get('/parameters/:id', authController.middlewareAuth, parametersUrlController.index);

app.listen(process.env.APPLICATION_PORT);
