echo "BUILD STARTED"
python3.9 -m pip install -r requirements.txt
echo "BUID ENDED"
echo "MIGRATION STARTED"
python3.9 manage.py makemigrations --noinput --clear

echo "MIGRATING"
python3.9 manage.py migrate --noinput --clear
echo "COLLECTING STATIC FILES"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD SUCCESSFUL!"