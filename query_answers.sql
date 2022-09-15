# Functions for: 

# 1. Year with the most races
SELECT raceYear, COUNT(*) FROM race GROUP BY raceYear ORDER BY raceYear DESC;

# 2. Driver with the most first places
SELECT d.driverName, COUNT(position) count
FROM qualify q JOIN driver d ON q.driverId = d.driverId AND q.position = 1
GROUP BY d.driverName
ORDER BY count DESC;

# 3. Name of the most run circuit
SELECT c.circuitName, COUNT(r.circuitId) Count
FROM race r JOIN circuit c ON r.circuitId = c.circuitId
GROUP BY c.circuitName
ORDER BY Count DESC;

# 4. Driver with the highest number of points in total whose constructor is American or British nationality
SELECT d.driverName, SUM(r.points) total_points
FROM driver d JOIN result r ON d.driverId = r.driverId
JOIN constructor c ON r.constructorId = c.constructorId AND c.nationality IN ("British", "American")
GROUP BY d.driverName
ORDER BY total_points DESC;