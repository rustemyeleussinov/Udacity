SELECT city_data.year, city_data.city, city_data.country, city_data.city, city_data.avg_temp as local_avg_temp, global_data.avg_temp as global_avg_temp
FROM city_data
LEFT JOIN global_data ON city_data.year = global_data.year
WHERE country='United States' and city='San Jose'