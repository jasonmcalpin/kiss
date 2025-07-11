<?php; 

require_once __DIR__ . '/vendor/autoload.php';
require_once __DIR__ . '/config.php';
require_once __DIR__ . '/routes.php';
require_once __DIR__ . '/services/ApiService.php';
require_once __DIR__ . '/services/DatabaseService.php';
require_once __DIR__ . '/models/User.php';

$request = $_SERVER['REQUEST_URI'];
$method = $_SERVER['REQUEST_METHOD'];



<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Game</title>
</head>
<body>
  

<?php

echo "Request Method: $method<br>";
echo "Request Path: $request<br>";
?>
<h2>The body of the request:</h2>
<?php

// get contents of post request and convert json to render it in the view
if ($method === 'POST') {
    $postData = json_decode(file_get_contents('php://input'), true);
    // Render the post data in the view
    echo "<pre>" . htmlspecialchars(print_r($postData, true)) . "</pre>";
} else if ($method === 'GET') {
    // For GET requests, you can display query parameters if needed
    $queryParams = $_GET;
    echo "<pre>" . htmlspecialchars(print_r($queryParams, true)) . "</pre>";
} else {
    echo "Unsupported request method.";
}

>
?>

</body>
</html>