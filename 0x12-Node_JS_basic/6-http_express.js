const express = require('express');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

const port = 1245;
app.listen(port, () => {
  console.log(`app listening on port ${port}.`);
});
module.exports = app;
