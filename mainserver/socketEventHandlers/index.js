import computationHandler from "./sendUser";
import { io } from "../server";

const onConnection = (socket) => {
    computationHandler(socket, io)
}

export default onConnection;