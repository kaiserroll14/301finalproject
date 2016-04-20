<?php

$shape = "1";
$color = "2";
$size = "3";
$pos = "4";

if($_POST['shape'] == "1") {
  echo "ok";
}
if($_POST['color'] == "1") {
  echo "ok";
}
if($_POST['size'] == "1") {
  echo "ok";
}
if($_POST['pos'] == "1") {
  echo "ok";
}

?>

<html>
 <head>
  <title>PHP Test</title>
 </head>
 <body>
 <?php
 print $shape;
 print $color;
 print $size;
 print $pos;
 ?> 
 </body>
</html>