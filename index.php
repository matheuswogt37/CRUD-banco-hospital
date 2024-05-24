<?php

// Define your routes
$routes = [
    '/' => 'src/home.php',
    '/home' => 'src/home.php',
    '/admin' => 'src/admin.php',
    '/acompanhante' => 'src/acompanhante/acompanhante.php',
    '/cadastro_acompanhante' => 'src/acompanhante/cadastro_acompanhante.php'
];

// Get the current URL path
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Check if the requested route exists in the array
if (array_key_exists($path, $routes)) {
    // If it does, include the corresponding file
    include $routes[$path];
} else {
    // If it doesn't, return a 404 error
    header("HTTP/1.1 404 Not Found");
    echo "404 Not Found";
}