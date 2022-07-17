CREATE SCHEMA `db_ProjectRegistration` DEFAULT CHARACTER SET DEFAULT ;


CREATE TABLE `registration` (
  `codigo` varchar(200) NOT NULL,
  `start_date` varchar(200) NOT NULL,
  `project_name` varchar(200) NOT NULL,
  `project_type` varchar(200) NOT NULL,
  `technologies` varchar(120) NOT NULL,
  `status_` varchar(120) NOT NULL,
  `annotations` varchar(120) NOT NULL,
  `completion_date` varchar(120) NOT NULL,
  PRIMARY KEY (`code`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


INSERT INTO `registration` (`code`,`start_date`,`project_name`,`project_type`,`technologies`,`status_`,`annotations`,`completion_date`) VALUES ('COD-05','15/07/2022','Projeto teste','html','java','ok','teste de lancamento','16/07/2022');
