import express from "express"
import dotenv from "dotenv"
import cors from "cors"

import tubeCommentsRouter from "./routes/youtubeComments.route.mjs"

dotenv.config()


const app = express()

app.use(cors())
app.use(express.json())

app.use('/api', tubeCommentsRouter)

const port = process.env.PORT;
app.listen(port, () => {
  console.log(`server running at ${port}`);
});