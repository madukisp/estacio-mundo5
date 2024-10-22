const users = require('../models/userModel');

exports.getAllUsers = (req, res) => {
    if (req.user.role !== 'admin') {
        return res.status(403).json({ error: 'Acesso negado.' });
    }

    res.status(200).json({ users });
};
