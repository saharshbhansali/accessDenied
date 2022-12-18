import { Schema, model } from "mongoose";

const socketSchema = new Schema({
    username: String,
    socketId: String
});

const socketModel = model("Socket", socketSchema)

export default socketModel;