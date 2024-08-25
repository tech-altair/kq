import { PrismaClient } from "@prisma/client";

const prisma = new PrismaClient();

export const commentsScores = async (req, res) => {
  try {
    const scores = await prisma.comment.findMany({
      select: {
        score: true,
      },
    });

    let positive = 0;
    let negative = 0;
    let neutral = 0;

    // Iterating over the scores and categorizing them
    scores.forEach(({ score }) => {
      if (score > 0) {
        positive++;
      } else if (score < 0) {
        negative++;
      } else {
        neutral++;
      }
    });

    // Prepare the response object
    const categoryCount = { positive, negative, neutral };

    // Send the response
    res.send(categoryCount);
  } catch (error) {
    console.error('Error fetching comment scores:', error);
    res.status(500).send('Error fetching comment scores');
  }
};
