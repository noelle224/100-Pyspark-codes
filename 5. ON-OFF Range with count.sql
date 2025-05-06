CREATE TABLE device_status (
    id INT PRIMARY KEY,
    event_time TIME,
    status VARCHAR(10)
);

INSERT INTO device_status (id, event_time, status) VALUES
(1, '10:01', 'on'),
(2, '10:02', 'on'),
(3, '10:03', 'on'),
(4, '10:04', 'off'),
(5, '10:07', 'on'),
(6, '10:08', 'on'),
(7, '10:09', 'off'),
(8, '10:11', 'on'),
(9, '10:12', 'off');

SELECT * FROM DEVICE_STATUS


WITH CTE AS (
select
*,
lag(status, 1, status) over(order by event_time) as prevstat
from device_status
)
, GROUPING AS (
select *,
sum(case when status = 'on' and prevstat = 'off' then 1 else 0 end) over(ORDER by event_time) as groups
from CTE
)
select
min(event_time) as Login,
max(event_time) as Logout,
count(*) as counting
from grouping
group by groups