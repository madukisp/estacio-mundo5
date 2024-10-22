const jwt = require('jsonwebtoken');
const users = require('../models/userModel');

exports.login = (req, res) => {
    const { username, password } = req.body;

    // Busca usuário no banco de dados simulado
    const user = users.find(u => u.username === username && u.password === password);
    if (!user) {
        return res.status(401).json({ error: 'Usuário ou senha incorretos.' });
    }

    // Gera o token JWT
    const token = jwt.sign({ id: user.id, role: user.role }, 'chave_secreta', { expiresIn: '1h' });
    res.status(200).json({ token });
};
