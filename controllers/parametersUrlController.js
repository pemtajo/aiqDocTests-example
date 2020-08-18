'use strict';

module.exports = {
    async index(req, res) {
        if (!req.params.id || isNaN(req.params.id)) {
            return res.status(400).json({
                'data': {
                    'message': 'URL parameter was not found.',
                    'success': false
                }
            });
        }

        if (!req.query.type || Object.values(req.query.type) === 0) {
            return res.status(400).json({
                'data': {
                    'message': 'Query parameter was not found.',
                    'success': false
                }
            });
        }
        
        return res.status(200).json({
            'data': {
                'message': 'Ok!',
                'id': parseInt(req.params.id),
                'type': req.query.type,
                'success': true
            }
        });
    }
};
