import socketModel from "../models/sockets";

const socketConnect = (socket, next) => {
  socketModel.findOne(
    { username: socket.handshake.auth.username },
    (err, socketObject) => {
      socketObject.id = socket.id;
      socketObject.save();
    }
  );
  next();
};

export default socketConnect;