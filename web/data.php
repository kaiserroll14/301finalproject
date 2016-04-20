<!DOCTYPE html>
<html>
<body>
<p>
<?php

$servername = "localhost";
$username = "root";
$password = "12345";
$dbname = "db1";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("SELECT * FROM shapes"); 
    $stmt->execute();

    // set the resulting array to associative
    $result = $stmt->setFetchMode(PDO::FETCH_ASSOC); 

    foreach($stmt->fetchAll() as $row) {
        echo $row['shape'].$row['color'].$row['size'].$row['pos']."<br>";
    }
}
catch(PDOException $e) {
     echo "Error: " . $e->getMessage();
}
$conn = null;
?>  
</p>
</body>
</html>
