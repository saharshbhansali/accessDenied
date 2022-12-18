import socketModel from "../models/sockets";
const computationHandler = (socket, io) => {
    socketModel.findOne({})
    socket.on("computation", (hashedpassword, receiver) =>{
        socketModel.findOne({ username: receiver}, (err, socketObject) => {
            const receivingSocket = io.in(socketObject.id).fetchSockets()[0];
            receivingSocket.emit("computation", subpassword2, hashedpassword1);
        })
    })
}

export default computationHandler;