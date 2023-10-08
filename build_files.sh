echo "BUILD STARTED"
python3.9 -m pip install -r requirements.txt
echo "BUID ENDED"
echo "MIGRATION STARTED"
python3.9 manage.py makemigrations --noinput

echo "MIGRATING"
python3.9 manage.py migrate --noinput
echo "COLLECTING STATIC FILES"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD SUCCESSFUL!"
echo "SIGNING UP SUPERUSER"
SUPERUSER_USERNAME="abhinav"
SUPERUSER_EMAIL="publicgyawali@gmail.com"
SUPERUSER_PASSWORD="barawa123"

echo "CREATING SUPER USER"
python "$MANAGE_PY_PATH" createsuperuser --username "$SUPERUSER_USERNAME" --email "$SUPERUSER_EMAIL" --noinput


echo "CHANGING PASSWORD"
python manage.py changepassword "$SUPERUSER_USERNAME" "$SUPERUSER_PASSWORD"

echo "Superuser '$SUPERUSER_USERNAME' created successfully."