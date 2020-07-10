function validKeys(client_key, secret_key) {
    if (client_key === process.env.API_KEY &&
        secret_key === process.env.SECRET_KEY) {
        return true;
    }
    return false;
}

const middlewareAuth = (req, res, next) => {
    try {
        console.log('Request logged:', req.method, req.path)
        if (!req.headers.authorization) {
            throw new Error();
        }

        const header = req.headers.authorization.replace('Basic ', ''); // Express headers are auto converted to lowercase
        const s = Buffer.from(header, 'base64').toString('ascii').split(':');

        const apiKey = s[0];
        const secretKey = s[1];

        if (!validKeys(apiKey, secretKey))
            throw new Error();

        return next();
    } catch (err) {
        return res.status(err.code || 401).json({ data: { message: 'You are unauthorized' } });
    }
};


module.exports = {
    middlewareAuth
};
