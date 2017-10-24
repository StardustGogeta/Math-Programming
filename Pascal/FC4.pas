program FC4;
Uses math;

var
n : Integer;
i : Integer;

begin
  writeln ('Enter a number:');
  readln (n);
  for i:=1 to Floor (Sqrt (n)) do
      if (n mod i)=0 then
         writeln (Floor(n/i), ' ', i);
  readln
end.
