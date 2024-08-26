import express from "express"
import Routes from "./routes/Routes.mjs"
const app = express()

app.use('/api/', Routes)

const port = process.env.PORT || 3000

app.listen(port, ()=>{
    console.log(`Server running on port ${port}`)
})