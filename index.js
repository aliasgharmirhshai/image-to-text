const express = require('express');
const app = express();
const PORT = process.env.PORT || 5000;
const bodyParser = require('body-parser');

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

const startApp = async () => {
    await app
        .get('/', (req, res) => {
            res.sendFile(__dirname + '/client/index.html');
        })
        .use(express.static(__dirname + '/client'))
        .use(express.json())
        .listen(PORT, () => console.log(`Listening on ${PORT}`));
};

startApp();