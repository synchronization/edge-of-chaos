#initial parameter value a=<input name=a size=4>
#(Try 3.2 or 3.8)
#noise level r=<input name=r size=4>
#<input type=submit value="Go">Try 0.0 or 0.005<br>
#<perl>

#print "Test perl script\n";

$x=0.38;
$x[0]=0.38;

# added now
#$a = 3.8;
$a = 3.4;

if ($a > 0) {
    $a[0] = $a
}
else {
    $a[0] = 3.8
};

for ($n=0; $n < 1000; $n++) {
#    print "n == $n\n";

    $f = $x;
    for ($k=1; $k<=32; $k++) {
        $x = $a[$n] * $x * (1-$x)
    }
    $x = $x + (rand(1)-0.5) * $r;
    
    if ($x>1) {$x=.999}
    if ($x<0){$x=0.001}
    
    $f = $f - $x;
    $x[$n] = $x;
    $a[$n+1] = $a[$n] + 0.1 * $f;

    if ($a[$n+1]<0) {
        $a[$n+1] = 0
    };
    if ($a[$n+1]>4) {
        $a[$n+1] = 4
    }

    for ($k=1; $k<32; $k++) {
        $x = $a[$n] * $x * (1-$x)
    }
}

#print "a == $a\n";
print join(", ", @a);
#print "\n";
#print "x == $x\n";

#</perl>
#
#<plot y-values=@a from=2 low=3 high=4
# y-label="parameter a" x-label="time n" width=500>
#<plot y-values=@x from=2 low=0 high=1
# y-label="variable y" x-label="time n" width=500>
