<?php
//Connexion a la base de donnees
$dbh = new PDO("sqlite:/home/pi/project_mansouri/secret_room_security_system/Client/BD/room_management.db");
//Requetes de selection
$sql = "SELECT * FROM history";
// affichage des resultats
echo "<h>history : </h><br>";
foreach ($dbh->query($sql) as $row)
{
    echo $row[time]." | ".$row[user_id]."<br>";
}
$dbh = null;
?>