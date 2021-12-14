<?php

$lines =  file("input.1");
#$lines =  file("input.test");

function applyrule($polymer, $depth) {
}

$polymer = trim(array_shift($lines)); // first line contains the template

array_shift($lines); // empty line

$rules = array();
foreach ($lines as $line) {
    list($key, $val) = explode(" -> ", $line);
    $rules[$key] = trim($val);
}

function processrule($polymer, $depth) {
    $steps = 10;
    if ($depth > $steps + 1) {
        return "";
    } else {
        $result = "";
        $mid = $GLOBALS['rules'][$polymer];
        $result .= processrule($polymer[0] . $mid, $depth + 1) . $mid . processrule($mid . $polymer[1], $depth + 1);
        return $result;
    }
}

$result = $polymer[0];
for ($i = 0; $i < strlen($polymer) - 1; $i++) {
    $result .= processrule(substr($polymer, $i, 2), 2) . substr($polymer, $i + 1, 1);
}

print($result);

$count = count_chars($result, 1);
print("<br>Outcome: ");
print(max($count) - min($count));
