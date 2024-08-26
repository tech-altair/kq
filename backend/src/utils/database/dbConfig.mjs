import sql from 'mssql'

export const dbConfig = {
    user: "sa",
    password: "mysQl123",
    server: "localhost", 
    database: 'sentimentAnalysisApp',
    options: {
        encrypt: true, 
        trustServerCertificate: true 
    }
};

export const poolPromise = sql.connect(dbConfig)
    .then(pool => {
        console.log('Connected to SQL Server');
        return pool;
    })
    .catch(err => {
        console.error('Database connection failed:', err);
        process.exit(1);
    });