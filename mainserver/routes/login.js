import { Router } from "express";

const router = Router();

router.post("/", loginController);

export default router;