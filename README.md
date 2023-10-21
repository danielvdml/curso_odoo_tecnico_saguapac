
## Comando para iniciar TDD
docker exec -it -u root <containername> odoo -d <basedatospruebas> --test-tags /<nombremodulo>  -p 8001 --log-level=test --dev all
o
docker exec -it -u root <containername> odoo -d <basedatospruebas> --test-tags /<nombremodulo>:<nombreclase>  -p 8001 --log-level=test --dev all

docker exec -it -u root test.odoo.saguapac odoo -d saguapacdb1 --test-tags /sg_sale_descuentos_sucesivos  -p 8001 --log-level=test --dev all