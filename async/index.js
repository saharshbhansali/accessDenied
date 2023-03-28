const express = require('express')
const app = express()

app.use(express.json())

app.get('/', (req, res) => {
    res.send("server is running")
})

let port = process.env.PORT;
if (port == null || port == "") {
  port = 3000;
}
app.listen(port,() => {
    console.log("running at "+ port);
});
