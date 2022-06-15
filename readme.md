1. Run in terminal
```fish
echo -e "AIRFLOW_UID=$(id -u)" > .env
docker-compose up
```

2. Login to PostgreSQL (localhost:5050) database using pgAdmin. Check credential file. Add source and destination database in pgAdmin.

3. Execute student-source query in source database.The script will create student table and insert some records. Check records inserted in source db.

4. Execute student-destination query in destination database. This script will create student table include insert timestamp column

5. Login to Apache Airflow (localhost:5884). Check credential file. You will see an error regarding 'postgres_student_migration' .

6. Go to Admin > Connections, add source and destination connection.

7. Once all done the error will dissapear and 'postgres_student_migration' DAG will appear in DAG page

8. The DAG will autorun. Check destination db, the records will be the same as source.

9. Insert more records in source db using student.sql file.

10. New inserted record will appear in destination db.
