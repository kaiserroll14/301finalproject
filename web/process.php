<?php
$shape = rand(1, 4);
$color = rand(1, 4);
$size = rand(1, 4);
$pos = rand(1, 4);

// Get values
if (isset($_POST['shape'])) {
    if(intval($_POST['shape']) > 0 && intval($_POST['shape']) < 5) {
        $shape = $_POST['shape'];
    }
}
if (isset($_POST['color'])) {
    if(intval($_POST['color']) > 0 && intval($_POST['color']) < 5) {
        $color = $_POST['color'];
    }
}
if (isset($_POST['size'])) {
    if(intval($_POST['size']) > 0 && intval($_POST['size']) < 5) {
        $size = $_POST['size'];
    }
}
if (isset($_POST['pos'])) {
    if(intval($_POST['pos']) > 0 && intval($_POST['pos']) < 5) {
        $pos = $_POST['pos'];
    }
}

$servername = "localhost";
$username = "root";
$password = "12345";
$dbname = "db1";

try {
    $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $stmt = $conn->prepare("INSERT INTO shapes (id, shape, color, size, pos) VALUES (NULL, :shape, :color, :size, :pos);"); 

    $stmt->bindParam(':shape', $shape, PDO::PARAM_INT);
    $stmt->bindParam(':color', $color, PDO::PARAM_INT);
    $stmt->bindParam(':size', $size, PDO::PARAM_INT);
    $stmt->bindParam(':pos', $pos, PDO::PARAM_INT);

    $stmt->execute(); 
}
catch(PDOException $e) {
     echo "Error: " . $e->getMessage();
}
$conn = null;

// $host = 'localhost';
// $db   = 'db1';
// $user = 'root';
// $pass = '12345';
// $charset = 'utf8';

// try {
//     $dsn = "mysql:host=$host;dbname=$db;charset=$charset";
//     $db = new PDO($dsn, $user, $pass);
// } catch (PDOException $e) {
//     echo $e->getMessage()."<br>";
//     die();
// }
// $sql = 'SELECT * from shapes';
// foreach($db->query($sql) as $row) {
//     echo $row['shape']." ".row['size']."<br>";
// }
// $db = null;

// $dbhost = "localhost";
// $dbuser = "root";
// $dbpass = "12345";
// $dbname = "db1";

// // // if($_SERVER['REQUEST_METHOD'] == "POST"){


// // Escape User Input to help prevent SQL Injection
// $shape = mysql_real_escape_string($shape);
// $color = mysql_real_escape_string($color);
// $size = mysql_real_escape_string($size);
// $pos = mysql_real_escape_string($pos);

//Connect to MySQL Server
// $conn = pdo_connect($dbhost, $dbuser, $dbpass);

// // //Select Database
// pdo_select_db($dbname) or die(mysql_error());

// // //Insert into db
// $sql = "INSERT INTO shapes (id, shape, color, size, pos) VALUES (Null, 3, 3, 3, 3)";

// $retval = pdo_query($sql, $conn);

// if(! $retval ) {
//    die('Could not enter data: ' . mysql_error());
// }

// echo "Entered data successfully\n";

// pdo_close($conn);
// // }

// // $shapes[] = array($shape, $color, $size, $pos);

?>

<!-- <html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <p>
1234<br>
4312<br>
4321<br>
 </p>
 </body>
</html> -->