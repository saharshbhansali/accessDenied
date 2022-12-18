import { io } from "../server.js";
import socketModel from "../models/sockets.js";

const loginController = async (req, res) => {
  const { email, password } = req.body;
  var id1, id2, id3;
  socketModel.findOne({ username: "server1" }, (err, socketObject) => {
    id1 = socketObject.id;
  });
  socketModel.findOne({ username: "server2" }, (err, id) => {
    id2 = id;
  });
  socketModel.findOne({ username: "server3" }, (err, id) => {
    id3 = id;
  });

  const socket1 = await io.in(id1).fetchSockets()[0];
  const socket2 = await io.in(id2).fetchSockets()[0];
  const socket3 = await io.in(id3).fetchSockets()[0];

  socket1.emit("computation", subpassword1);
  socket2.emit("computation", subpassword2);
  socket3.emit("computation", subpassword3);

};

export default loginController
