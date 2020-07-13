'use strict';

module.exports = {
    async store(req, res) {
        if (! req.files) {
            return res.status(400).json({
                data: {
                    success: false,
                    message: 'File was not found.'
                }
            });
        }

        const uploadedFile = req.files['uploaded_file'];

        if (! uploadedFile) {
            return res.status(400).json({
                data: {
                    success: false,
                    message: 'File was not found.'
                }
            });
        }

        return res.status(200).json({
            data: {
                success: true,
                message: 'Ok!',
                files: req.files
            }
        });
    }
};
