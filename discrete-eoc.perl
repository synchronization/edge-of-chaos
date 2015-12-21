$numsteps = 3;

$x=0.38;
$x[0]=0.38;

$a = 3.8;

$r = 0;#0.005;

if ($a > 0) {
    $a[0] = $a
}
else {
    $a[0] = 3.8
};

for ($n = 0; $n < $numsteps; $n++) {
    print "----------\n";
    print "x == $x\n";

    $f = $x;

    print "f == $f\n";

    for ($k = 1; $k <= 32; $k++) {
        $x = $a[$n] * $x * (1 - $x);
        print "m: x == $x\n";
    }
    $x = $x + (rand(1) - 0.5) * $r;
    
    print "x == $x\n";

    if ($x > 1) { $x = 0.999 }
    if ($x < 0) { $x = 0.001 }
    
    $f = $f - $x;
    $x[$n] = $x;
    $a[$n+1] = $a[$n] + 0.1 * $f;

    if ($a[$n+1] < 0) {
        $a[$n+1] = 0
    };
    if ($a[$n+1] > 4) {
        $a[$n+1] = 4
    }

    for ($k = 1; $k < 32; $k++) {
        $x = $a[$n] * $x * (1 - $x)
    }
}

print join(", ", @a);
