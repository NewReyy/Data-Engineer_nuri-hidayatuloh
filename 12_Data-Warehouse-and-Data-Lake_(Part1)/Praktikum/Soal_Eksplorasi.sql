#Menampilkan Rata-rata kepuasan Mentor keseluruhan 
SELECT AVG(mentor_satisfaction_score) AS Rata_rata_kepuasan_mentor
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey;

#Menampilkan Rata-rata kepuasan CS keseluruhan
SELECT AVG(cs_satisfaction_score) AS rerata_kepuasan_cs
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey;

#Menampilkan Rata-rata kepuasan mentor untuk "Course A"
SELECT AVG(mentor_satisfaction_score) AS rerata_kepuasan_mentor_CourseA
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey
WHERE course_name = 'Course A';

#Menampilkan nilai terendah dari kepuasan belajar (learning_satisfaction_score) untuk “Course C”.
SELECT AVG(learning_satisfaction_score) AS nilai_terendah_kepuasan_belajar
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey
WHERE course_name = 'Course C';

#Menampilkan nilai tertinggi dari kepuasan CS (cs_satisfaction_score) untuk “Course B”.
SELECT MAX(cs_satisfaction_score) AS nilai_tertinggi_kepuasan_mentor
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey
WHERE course_name = 'Course B';

#Menampilkan nama course dengan rata-rata kepuasan mentor tertinggi.
SELECT course_name, AVG(mentor_satisfaction_score) AS Course_Rerata_Teringgi_Mentor
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey
GROUP BY course_name
ORDER BY Course_Rerata_Teringgi_Mentor DESC
LIMIT 1;

#Menampilkan nama course dengan rata-rata kepuasan belajar tertinggi.
SELECT course_name, AVG(learning_satisfaction_score) AS Kepuasan_Belajar_Tertinggi
FROM eksplorasi-altera-de-b6.Alterra_DE_Batch6.survey GROUP BY course_name
ORDER BY Kepuasan_Belajar_Tertinggi DESC
LIMIT 1;