import { Schema, model } from "mongoose";

const userSchema = new Schema({
    email: String,
    hash: String
})