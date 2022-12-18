// const express = require("express");
// const app = express();

// const http = require("http");

// const server = http.createServer(app);

// import mongoose from "mongoose";

// mongoose.connect("mongodb://127.0.0.1/my_database").catch((err) => {
//   console.log(err);
// });

// mongoose.connection.once("open", () => {
//   console.log("Connected to MongoDB successfully.");
// });

import { io } from "socket.io-client";

const socket = io(url, {
    auth: {
        username: "user1"   
    }
});

socket.on("computation", (subpassword1) => {
    socket.emit("computation", hashedpassword1, "server2");
})