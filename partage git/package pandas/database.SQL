SELECT Orders.OrderID, CustomerID, EmployeeID, OrderDate, ShipCountry
from orders, `order details`
WHERE Orders.OrderID = `order details`.`OrderID`

CREATE VIEW ordesinfos
AS
SELECT Orders.OrderID, CustomerID, EmployeeID,
     OrderDate, ShipCountry
FROM orders, `order details`
WHERE Orders.OrderID = `order details`.OrderID
