const express = require('express');
const bodyParser = require('body-parser');
const authController = require('./controllers/authController');
const userController = require('./controllers/userController');
const authMiddleware = require('./middleware/authMiddleware');

const app = express();
app.use(bodyParser.json());

// Rotas públicas
app.post('/api/auth/login', authController.login);

// Rotas protegidas
app.get('/api/users', authMiddleware.verifyToken, userController.getAllUsers);

// Inicializando o servidor
const port = process.env.PORT || 3000;
app.listen(port, () => {
    console.log(`Servidor rodando na porta ${port}`);
});
