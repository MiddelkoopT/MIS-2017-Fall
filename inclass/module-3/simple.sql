-- simple.sql by Timothy Middelkoop Copyright 2017 Timothy Middelkoop
-- Source Code License Apache 2.0, Documentation License CC by SA 3.0.
-- wget -c https://github.com/swcarpentry/sql-novice-survey/raw/gh-pages/files/survey.db
-- sqlite3 -header -csv survey.db < simple.sql > simple.csv

SELECT
  taken, reading
FROM
  Survey
WHERE
  quant="temp";
 
