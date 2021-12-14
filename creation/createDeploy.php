<?php

require ("./creds/config.php");

try {
    
    // connect to db 
    $db = new PDO("mysql:host=$servername;dbname=$dbname", $dbusername, $dbpassword);


    //create the table in the deployment db

    $createDeploy = $db->prepare("CREATE TABLE IF NOT EXISTS `deployControl`(
        deploy_id int auto_increment, 
        `filename` varchar (30) not null,
        `version` int not null,
        grade varchar (30) not null,
        origin varchar (30),
        destination varchar (30),
        sender varchar (30),
        PRIMARY KEY (deploy_id)
        );"
    );

    $createDeploy->execute();





} catch (Exception $e) {
    echo " ERROR --> ";
    echo $e->getMessage();
    echo " unable to make deploy table";
}

?>