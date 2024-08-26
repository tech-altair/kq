import express from "express";
import { getTweets } from "../controllers/twitterController.mjs";
import { getTripReview } from "../controllers/tripController.mjs";

const router = express.Router();

router.get("/twitter/fetch-tweets/", getTweets);
router.get("/trip/fetch-reviews/", getTripReview)

export default router;
