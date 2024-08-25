import express from "express"
import dotenv from "dotenv"
import tubeCommentsRouter from "./routes/youtubeComments.route.mjs"

dotenv.config()


const app = express()

app.use('/api', tubeCommentsRouter)

const port = process.env.PORT;
app.listen(port, () => {
  console.log(`server running at ${port}`);
});