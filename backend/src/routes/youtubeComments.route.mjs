import { Router } from "express";
import { fetchYouTubeComments } from "../scraping/youtubeComments.mjs";

const tubeCommentsRouter = Router()

tubeCommentsRouter.route("/")
                    .get(fetchYouTubeComments)

export default tubeCommentsRouter