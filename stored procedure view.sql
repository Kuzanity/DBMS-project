use db_oragon;
DELIMITER $$ 
create procedure GetProducts()
begin
select *from sales_product;
end $$
DELIMITER ;
call GetProducts()