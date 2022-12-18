const express = require("express");
const app = express();

const http = require("http");

const server = http.createServer(app);

const { Server } = require("socket.io");

export const io = new Server(server);

const mongoose = require("mongoose");
mongoose.connect("mongodb://127.0.0.1/my_database").catch((err) => {
  console.log(err);
});

mongoose.connection.once("open", () => {
  console.log("Connected to MongoDB successfully.");
});

server.listen(3000, () => {
  console.log("Listening on port 3000");
});

io.use((socket, next) => {
  socket.data.username = socket.handshake.auth.username;
  next();
});

io.on("connection", );
