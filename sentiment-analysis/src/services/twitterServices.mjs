import { TwitterApi } from "twitter-api-v2";
import { PrismaClient } from "@prisma/client";
import dotenv from "dotenv";

dotenv.config();

const prisma = new PrismaClient();

const twitterclient = new TwitterApi({
  appKey: process.env.TWITTER_API_KEY,
  appSecret: process.env.TWITTER_API_KEY_SECRET,
  accessToken: process.env.TWITTER_ACCESS_TOKEN,
  accessSecret: process.env.TWITTER_ACCESS_TOKEN_SECRET,
});

export const fetchTweets = async (query) => {
  try {
    const response = await twitterclient.v2.search(query, { max_results: 100 });
    return response.data;
  } catch (error) {
    console.error("Error fetching tweets", error); //throws an error if the fetch wasn't successful
  }
};

export const saveTweet = async (content) => {
  try {
    await prisma.data.create({
      data: {
        source: "Twitter",
        content: content,
        sentiment: "Neutral",
      },
    });
  } catch (error) {
    console.error("Error saving Tweet", error);
    throw error; //for handling errors
  }
};
