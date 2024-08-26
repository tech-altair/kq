import axios from "axios"; //Axios is used to make HTTP requests to fetch data from URLs
import * as cheerio from "cheerio" // cheerio is  used to parse and manipulate HTML data
import { PrismaClient } from "@prisma/client"; //prisma is used to interact with th database

const prisma = new PrismaClient();

export const fetchTripAdvisorReviews = async (url) => {
  //I used async functions to avoid blocking when pulling data from the database to allow other processes to continue as the tast runs.
  //async/await handles asynchronous operations .
  try {
    const { data } = await axios.get(url); //fetches the contents of the provided url
    const $ = cheerio.load(data); 
    const reviews = [];
    //Extract review texts from the HTML using the cheerio's selector
    $(".review-container").each((index, element) => {
      const reviewText = $(element).find(".partial_entry").text();
      reviews.push(reviewText); //push() method is used to add the contents to the reviews array.
    });

    return reviews; 
  } catch (error) {
    console.error("Error fetching TripAdvisor reviews:", error);
    throw error; //throwing errors
  }
};

export const saveReview = async (content) => {
  try {
    await prisma.data.create({
      data: {
        source: "TripAdvisor",//indicating the source of the reviews
        content: content,//contents saved in the database
        sentiment: "Neutral", //setting the sentiment as "Neutral" which will later be updated
      },
    });
  } catch (error) {
    console.error("Error saving review:", error);
    throw error; //throws an error if it doesn't save successfully.
  }
};
