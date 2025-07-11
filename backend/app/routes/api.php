<?php
require_once 'controllers/AuthController.php';
require_once 'controllers/NationController.php';
require_once 'controllers/GameController.php';
require_once 'controllers/MapController.php';
require_once 'controllers/TurnController.php';
require_once 'controllers/ChatController.php';

$method = $_SERVER['REQUEST_METHOD'];
$path = parse_url($_SERVER['REQUEST_URI'], PHP_URL_PATH);

// Authentication routes
if ($path === '/api/auth/register' && $method === 'POST') {
    $controller = new AuthController();
    $controller->register();
} elseif ($path === '/api/auth/login' && $method === 'POST') {
    $controller = new AuthController();
    $controller->login();
} elseif ($path === '/api/auth/logout' && $method === 'POST') {
    $controller = new AuthController();
    $controller->logout();
} elseif ($path === '/api/auth/me' && $method === 'GET') {
    $controller = new AuthController();
    $controller->me();
}

// Nation routes
elseif ($path === '/api/nations/create' && $method === 'POST') {
    $controller = new NationController();
    $controller->create();
} elseif (preg_match('/^\/api\/nations\/(\d+)\/name$/', $path, $matches) && $method === 'PUT') {
    $controller = new NationController();
    $controller->updateName($matches[1]);
} elseif (preg_match('/^\/api\/nations\/(\d+)\/flag$/', $path, $matches) && $method === 'PUT') {
    $controller = new NationController();
    $controller->updateFlag($matches[1]);
}

// Game routes
elseif ($path === '/api/games/create' && $method === 'POST') {
    $controller = new GameController();
    $controller->create();
} elseif (preg_match('/^\/api\/games\/join\/(\d+)$/', $path, $matches) && $method === 'POST') {
    $controller = new GameController();
    $controller->join($matches[1]);
} elseif ($path === '/api/games/active' && $method === 'GET') {
    $controller = new GameController();
    $controller->getActive();
}

// Turn routes
elseif (preg_match('/^\/api\/games\/(\d+)\/turns\/submit$/', $path, $matches) && $method === 'POST') {
    $controller = new TurnController();
    $controller->submitTurn($matches[1]);
} elseif (preg_match('/^\/api\/games\/(\d+)\/turns\/current$/', $path, $matches) && $method === 'GET') {
    $controller = new TurnController();
    $controller->getCurrentTurn($matches[1]);
} elseif (preg_match('/^\/api\/games\/(\d+)\/turns\/process$/', $path, $matches) && $method === 'POST') {
    $controller = new TurnController();
    $controller->processTurn($matches[1]);
}

// Map routes
elseif (preg_match('/^\/api\/maps\/(\d+)$/', $path, $matches) && $method === 'GET') {
    $controller = new MapController();
    $controller->getMap($matches[1]);
} elseif ($path === '/api/maps/generate' && $method === 'POST') {
    $controller = new MapController();
    $controller->generate();
}

// Chat routes (if not using WebSocket)
elseif (preg_match('/^\/api\/chat\/(\d+)\/messages$/', $path, $matches) && $method === 'GET') {
    $controller = new ChatController();
    $controller->getMessages($matches[1]);
} elseif (preg_match('/^\/api\/chat\/(\d+)\/send$/', $path, $matches) && $method === 'POST') {
    $controller = new ChatController();
    $controller->sendMessage($matches[1]);
}

else {
    http_response_code(404);
    echo json_encode(['error' => 'Endpoint not found']);
}
?>