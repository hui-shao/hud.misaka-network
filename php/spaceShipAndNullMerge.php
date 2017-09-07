<?php
/**
 * Created by PhpStorm.
 * User: Aozak
 * Date: 9/6/17 006
 * Time: 下午 9:03
 */
$a = 6;
$b = 2;
echo $a <=> $b;
echo "<br/>";
$c = null;
$d = null;
echo $c ?? $a ?? $d ?? $b;
