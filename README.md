# Training Tracker

## Backend Setup Notes

To fix the ERR_CONNECTION_REFUSED error when the frontend cannot connect to the backend API at 127.0.0.1:8000, please ensure the following:

1. Run the Django backend server binding to all interfaces by using:
```
python manage.py runserver 0.0.0.0:8000
```
This allows the backend to be accessible from other hosts or environments.

2. Set the CORS_ALLOWED_ORIGINS environment variable to include the frontend origin, for example:
```
CORS_ALLOWED_ORIGINS=http://localhost:3000
```
This allows the backend to accept cross-origin requests from the frontend.

3. Restart the backend server after making these changes.

4. Verify the frontend API base URL in `frontend/src/services/api.js` is set to:
```js
const API_BASE_URL = 'http://127.0.0.1:8000/api';
```
or the appropriate backend address accessible from the frontend.

Following these steps should resolve the connection refused error.
