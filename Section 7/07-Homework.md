# SECTION 07 HW 
<br>

## Directions 
1. You will need to open up the SavvyCoders_SQL_EVtables.db for the first part of the HW.
2. If you need to change databases you will be instructed to do so. 
3. Please answer all of the questions in a markdown file. Here is the sample format: 

# Section 7.1 
## Question 1
```SQL

--Write your SQL answers in here 

```
## Question 2 
```SQL

--Write your SQL answers in here 

```
4. You can copy and paste this sample outline into a markdown and then add a new question block for each question within the section and when the new section comes, create a new section block. 
 

<br>

# 7.1 HW Questions 


1. Using EVregistry, Write a query to select the `ModelYear`, `Make`, and `Model` off all of the vehicles in the registry.
2. Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, `ElectricVehicleType`. 
3. Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry. 
4. Using the EVRegistry, wirte a query that returns the `Make` and `Model` of all of the EV's that have a BaseMSRP between 20000 and 35000?  

# Section 7.1 - Answers
## Question 1
Using EVregistry, Write a query to select the `ModelYear`, `Make`, and `Model` off all of the vehicles in the registry.
```SQL

select ModelYear, Make, Model from EVRegistry

```
## Question 2 
Using the EVRegistry table, Write a query that lists all of the unique types of EV's. your reult set should have one column, ElectricVehicleType
```SQL

select distinct ElectricVehicleType from EVRegistry

```
## Question 3
Using the EVRegistry, Write a query that shows all of the information on Battery Electric Vehicles (BEV) that are in the registry.
```SQL

select * from EVRegistry
where ElectricVehicleType = 'Battery Electric Vehicle (BEV)'

```
## Question 4 
Using the EVRegistry, wirte a query that returns the Make and Model of all of the EV's that have a BaseMSRP between 20000 and 35000?
```SQL

select Make, Model from EVRegistry
where BaseMSRP >= 20000 and BaseMSRP <=35000

```

# 7.2 HW Questions 

1. Using EVRegistry, write a query to find a record  where the `City` attribute is NULL. Return all of the available columns. 
2. Write a query to find the `make`, `model`, and `ElectricVehicleType` where the VIN number has  that ends in '3E1EA1J'.
3. Select the `ModelYear`, `make`, `model`, `ElectricVehicleType`, and `range` of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest. 
4. Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records. 
5.  Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. 
# Section 7.2 Answers 
## Question 1
Using EVRegistry, write a query to find a record where the City attribute is NULL. Return all of the available columns.
```SQL

select * from EVRegistry
where city is NULL 

```
## Question 2 
Write a query to find the make, model, and ElectricVehicleType where the VIN number has that ends in '3E1EA1J'.
```SQL

select make, model, ElectricVehicleType from EVRegistry
where VIN like '%3E1EA1J'

```
## Question 3
Select the ModelYear, make, model, ElectricVehicleType, and range of the Tesla vehicles or cheverolet vehicles in the registry. Order the result set by Make and Model year in from newest to oldest.
```SQL

select ModelYear, make, model, ElectricVehicleType, ElectricRange from EVRegistry
where make = 'TESLA' or make = 'CHEVROLET'
order by make desc, ModelYear desc

```
## Question 4 
Using EVCharging, Write a query to find out how many many times those stations were used. Order them by the most used to the least used and limit the output to 5 records.
```SQL

select stationId, count(stationId) as stations_used from EVCharging
group by stationId
order by count(stationId) DESC
limit 5

```
## Question 5
Using EVCharging, For the folks who charged longer than 0.5 hours, show the min and max of the charging time for each user. Your output columns should be userid, minTime, and maxTime. Order this result set by the last two columns respectively.
```SQL

select userid, min(chargeTimeHrs) as minTime, max(chargeTimeHrs)as maxTime from EVCharging
where chargeTimeHrs > 0.5
group by userId
order by min(chargeTimeHrs)asc , max(chargeTimeHrs) desc

```

# Before moving on with the rest of the questions please set up the new database
1. in SQLlite close any open DB
2. file----> Open Database
3. Choose SavvyCoders_SQL_chargeDB.db from the resource repository from this section in the curriculum
4. Make sure that you have 5 tables: 
    - dimDay 
    - dimFacility
    - dimUser
    - factCharge
    - EVCharging


# 7.3 HW Questions

1. Using EVCharging, Which day of the week has the highest average charging time? Round the answer to 2 decimal points.
2. Using, EV charging, Find the total power consumed from charging EV's by each User. Return the `userId` and name the calculated column, `totalPower`. Round the answer to 2 deciaml points and list the out put in highest to lowest order. Limit the order to the top 15 users. 
3. Using dimfacility and factCharge, write a query to find out which type of facility (GROUP BY) has the most amount of charging stations. Return `type Facility` and name the calculated column `numStation`. Order the result set from highest to lowest number of charging stations.  
4. In your own words, Briefly explain Primary Keys and Foreign Keys. 
5. Using EV Charging, For the folks who charged longer than one hour, show the min and max of the charging time for each user. Your output columns should be `userid`, `minTime`, and `maxTime`. Order this result set by the last two columns respectively. HINT: USE `HAVING`

# Section 7.3 Answers
## Question 1
```SQL

select weekday , round(avg((chargeTimeHrs)),2) as avgChargeTime from EVCharging
group by weekday
order by round(avg((chargeTimeHrs)),2)desc
limit 1

```
## Question 2 
```SQL

select userId , round(sum(kwhTotal),2) as totalPower from EVCharging
group by userId
order by round(sum(kwhTotal),2) DESC
limit 15


```
## Question 3
```SQL

select df.typeFacility, max(stationID)as numStation from factCharge fc
join dimFacility df 
on fc.facilityID = df.FacilityKey
group by df.typeFacility
order by max(stationID) desc
limit 1

```
## Question 4 
```SQL

Primary key is a column in a table which is the unique value to identify a row

Foreign key is a column in a table that links to the primary key of another table

```
## Question 5
```SQL

select userId, min(chargeTimeHrs) as minTime, max(chargeTimeHrs)as maxTime from EVCharging
group by userId
having chargeTimeHrs > 1
order by min(chargeTimeHrs), max(chargeTimeHrs) desc

```


## When done with homework

When all the week #3 homework has been completed, do the following...

- Make sure your homework file is well named
- Add the homework to your Homework folder
- Use  `git add .`, `git commit -m "message"`, and `git push` to upload your homework changes to GitHub in the cloud
- Create a JIRA ticket with your homework repo url, to indicate that your Homework is ready for review
