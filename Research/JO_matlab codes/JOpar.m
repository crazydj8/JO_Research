%Calculation of O2,O4,O6
O2=0;
for i=1:1:q
    O2=O2+f(1,i)*y(i,5)
end
O4=0;
for i=1:1:q
    O4=O4+f(2,i)*y(i,5)
end

O6=0;
for i=1:1:q
    O6=O6+f(3,i)*y(i,5)
end