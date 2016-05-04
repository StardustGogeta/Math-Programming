use bignum;print "Enter a number.\n";
$n = <STDIN>;
for ($i=1;$i<=sqrt($n);$i++){
if ($n % $i==0){
print $i,", ",$n/$i,"\n";}}
print "List complete.\n";