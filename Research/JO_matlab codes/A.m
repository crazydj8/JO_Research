%%Code to calculate A. Make sure to rename the created file every time.
%%Also cancel all the auxiliary variables created so far but q.

e=0;
for n=1:1:1
 prompt = 'J value at excited state ';
    e(n,1)=input(prompt);
   prompt = 'Peak wavelength of emission ';
    e(n,2)=input(prompt);
    e(n,3)=x(n,1);
    e(n,4)=x(n,2);
    e(n,5)=x(n,3);
    e(n,6)=y(n,4);
    e(n,7)= 7.23E10*e(n,6)*((e(n,6)^2+2)/3)^2*tls(1,n)/((2*e(n,1)+1)*(e(n,2)*1E-7)^3);
end
%e(n,7) is the calculated Aed ;
%Check if a Amd occurs for the given transition.

