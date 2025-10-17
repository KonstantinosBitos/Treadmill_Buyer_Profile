--What is the average age of customers for each treadmill type?

SELECT 
  product,
  round(avg(age),2) as Average_age,
  count(*) as Total_customers
FROM aerofit 
GROUP BY product

--What fitness level is associated with each treadmill type?

SELECT 
  product,
  round(avg(fitness),2) as Average_fitness,
  count(*) as Total_customers 
FROM aerofit 
GROUP BY product

--How does income vary by product purchased?

SELECT 
  product, 
  round(avg(income),2) as Average_income, 
  count(*) as Total_customers 
FROM aerofit
GROUP BY product

--What is the gender distribution per product?

SELECT 
    Product, 
    Gender, 
    COUNT(*) AS Count,
    ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY Product), 1) AS Percent
FROM aerofit
GROUP BY Product, Gender;

--Do partnered customers have the same product preferences as single ones?

SELECT 
  Product, 
  MaritalStatus, 
  COUNT(*) AS Count,
  ROUND(100.0 * COUNT(*) / SUM(COUNT(*)) OVER (PARTITION BY Product), 1) AS Percent 
FROM aerofit 
GROUP BY Product, MaritalStatus;
