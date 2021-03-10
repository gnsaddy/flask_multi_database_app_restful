
echo "Exporting the flask app"
export FLASK_APP=app.py

echo "Running the app on development environment"

export FLASK_ENV=development

echo "App is starting..."
flask run

