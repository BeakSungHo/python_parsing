const express = require('express');
const {spawn} = require('child_process');
const app = express()
const port = process.env.PORT || 5000

app.get('/', (req, res) => {
    let dataToSend;
    const python = spawn('py', ['test_copy.py']);
    python.stdout.on('data', (data) => {
      //console.log(data.toString('utf-8'));
      console.log(typeof data.toString);
     dataToSend = data.toString();
  })
   python.on('close', (code) => {
     res.send(dataToSend);
  })
})

app.listen(port, () => console.log(`Listening on ${port}`))