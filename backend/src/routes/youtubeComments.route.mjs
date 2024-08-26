import { Router } from "express";
import { commentsScores } from "../controllers/comments.controller.mjs";

const tubeCommentsRouter = Router()

tubeCommentsRouter.route("/")
                    .get(commentsScores)

export default tubeCommentsRouter