import { io } from "../server";

const loginController = async (req, res) => {
    const { email, password } = req.body;
    
