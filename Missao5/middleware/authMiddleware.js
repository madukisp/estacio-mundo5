const jwt = require('jsonwebtoken');

exports.verifyToken = (req, res, next) => {
    const token = req.header('Authorization')?.split(' ')[1]; // Extrai o token do cabeçalho

    if (!token) {
        return res.status(401).json({ error: 'Acesso negado. Token não fornecido.' });
    }

    try {
        const verified = jwt.verify(token, 'chave_secreta');
        req.user = verified;
        next();
    } catch (err) {
        res.status(400).json({ error: 'Token inválido.' });
    }
};
