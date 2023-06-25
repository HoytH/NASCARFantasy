const cors = require('cors');
const express = require('express');
const app = express();
const pool = require("./routes/dbConfig");
const nfRouter = require("./routes/NascarFantasy");
const PORT = process.env.PORT || 4080;

const corsOptions = {
    origin: 'http://localhost:4200',
    credentials:true,
    optionSuccessStatus:200
}

app.use(cors(corsOptions));
app.use("/NascarFantasy", nfRouter);

app.get("/test", (req, res) =>{ 
    pool.query("SELECT * FROM races;", (err, result) => {
        res.send(result.rows)
    })
})

app.get('/', (req, res) => {
    res.send('Serve is running')
})

app.listen(PORT, () => {
    console.log(`server running on port ${PORT}`)
})